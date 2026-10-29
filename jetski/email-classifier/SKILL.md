---
name: email-classifier
description: Klasyfikuje nieprzeczytane emaile według bazy generycznych tematów w ~/.gemini/email_topics.json, deleguje ocenę i wykonanie akcji podagentom (ważność urgency + class_weight * content_score liczy deterministyczny skrypt) i przedstawia raport zbiorczy; waliduje bazę tematów względem pomocy CLI gmail. Use when użytkownik prosi o klasyfikację, ocenę ważności lub porządkowanie nieprzeczytanych maili według tematów, o dodanie klasy tematu albo o walidację bazy tematów email. Don't use for czytania, wyszukiwania lub wysyłania pojedynczych maili (use gmail) ani do triażu skrzynki bez bazy tematów (use email-triage).
metadata:
  version: "0.8"
---

# Email Classifier

## Cel

Sklasyfikuj nieprzeczytane wiadomości według bazy tematów `~/.gemini/email_topics.json`. Deleguj ocenę wiadomości i wykonanie akcji podagentom. Przedstaw raport zbiorczy. Utrzymuj bazę tematów i waliduj ją po każdej zmianie.

## Zasoby

- [assets/email-topics-template.json](assets/email-topics-template.json) — szablon pustej bazy tematów (pusta lista klas).
- [assets/subagent-prompt-template.md](assets/subagent-prompt-template.md) — szablon promptu podagenta.
- [scripts/evaluate_dispositions.py](scripts/evaluate_dispositions.py) — skrypt oceny; wywołuje go wyłącznie podagent.
- [scripts/validate_topics.py](scripts/validate_topics.py) — skrypt walidacji bazy tematów.
- [requirements.md](requirements.md) — wymagania skilla; przeczytaj przed każdą zmianą skilla.

Ścieżki są względne wobec katalogu tego skilla.

## Baza tematów

Baza to obiekt JSON z listą klas pod kluczem `topics`. Pola klasy:

| Pole | Znaczenie |
|---|---|
| `id` | unikalny; tylko wielkie litery A–Z, cyfry, `_` i `-`, bez spacji (np. `TOPIC-01`, `CODE_REVIEW`); nie może być `UNKNOWN` |
| `name`, `description` | nazwa i zakres generycznej klasy |
| `class_weight` | waga klasy, 0.0–1.0 |
| `content_scoring_prompt` | instrukcja oceny `content_score` dla klasy; może być pustym tekstem |
| `autonomy_threshold` | próg działania autonomicznego, 0.00–2.00 |
| `action_auto` | akcja dla ważności `<= autonomy_threshold` |
| `action_escalated` | akcja dla ważności `> autonomy_threshold` |

Akcja to lista wpisów. Pusta lista `[]` oznacza brak akcji. Każdy wpis to:
- `gmail: <argumenty CLI gmail>` — skrypt oceny wykonuje go przez `/google/bin/releases/gemini-agents-gmail/gmail`. Jedynym parametrem jest `{ID}`; skrypt zastępuje go przez `MESSAGE_ID`.
- `prompt: <opis>` — skrypt oceny zwraca go podagentowi, który wykonuje opisaną operację.

## Model oceny

`importance = urgency + (class_weight * content_score)`

- Ważność liczy wyłącznie skrypt oceny.
- `urgency` (pilność, 0.0–1.0) i `content_score` (ocena treści, 0.0–1.0) ocenia podagent według [assets/subagent-prompt-template.md](assets/subagent-prompt-template.md). Podagent przyznaje `urgency` tylko wartości 0.2, 0.5 lub 1.0; skrypt przyjmuje cały przedział 0.0–1.0.
- Domyślną listę oceny `content_score` stosuje się wyłącznie wtedy, gdy klasa nie ma `content_scoring_prompt`, tj. `content_scoring_prompt = ""`.
- `importance <= autonomy_threshold` → tryb `AUTONOMOUS`, akcja `action_auto`.
- `importance > autonomy_threshold` → tryb `ESCALATED`, akcja `action_escalated`.

## Zasady wątku głównego

- Nie pobieraj i nie cytuj treści maili. Przekazuj podagentom wyłącznie `MESSAGE_ID`.
- Nie wywołuj skryptu oceny. Wywołuje go podagent.
- Zadawaj każde pytanie do użytkownika wyłącznie narzędziem `ask_question`. Podaj gotowe opcje. Oznacz pierwszą opcję prefiksem `(Recommended)`.

## Workflow: triaż skrzynki

Copy this checklist and track progress:

- [ ] Krok 0: Sprawdź stan bazy tematów
- [ ] Krok 1: Policz nieprzeczytane maile i ustal zakres
- [ ] Krok 2: Deleguj ocenę podagentom
- [ ] Krok 3: Zbierz wyniki podagentów
- [ ] Krok 4: Dodaj nowe klasy
- [ ] Krok 5: Przedstaw raport zbiorczy
- [ ] Krok 6: Przetwórz kolejną paczkę

### Krok 0: Sprawdź stan bazy tematów

1. Sprawdź, czy plik istnieje:
   ```bash
   test -f ~/.gemini/email_topics.json && echo EXISTS || echo MISSING
   ```
2. Jeśli `MISSING` → utwórz bazę z pustą listą klas, kopiując szablon:
   ```bash
   cp <katalog-skilla>/assets/email-topics-template.json ~/.gemini/email_topics.json
   ```
   Przy pustej bazie każdy mail trafia do kroku 4 (nowe klasy).
3. Jeśli `EXISTS` → nie zmieniaj pliku.

### Krok 1: Policz nieprzeczytane maile i ustal zakres

1. Pobierz listę identyfikatorów:
   ```bash
   /google/bin/releases/gemini-agents-gmail/gmail readonly search "is:unread in:inbox" --max 500 --json
   ```
2. Policz zwrócone pozycje (N) poleceniem `python3 -c`.
3. Jeśli N > 50 i użytkownik nie podał liczby maili → zapytaj:
   ```json
   {
     "questions": [
       {
         "question": "Masz ponad 50 nieprzeczytanych wiadomości (łącznie: <N>). Ile najnowszych maili przetworzyć?",
         "options": [
           "(Recommended) Wyłącznie 50 najnowszych wiadomości",
           "100 najnowszych wiadomości",
           "Wszystkie (<N> wiadomości), w paczkach po 50 na jeden obrót pętli wątku głównego"
         ],
         "is_multi_select": false
       }
     ]
   }
   ```
4. Jeśli użytkownik wybrał wszystkie wiadomości → podziel je na paczki po 50. W pozostałych przypadkach wybrane wiadomości tworzą jedną paczkę.
5. Przetwórz pierwszą paczkę w krokach 2–5.

### Krok 2: Deleguj ocenę podagentom

1. Podziel paczkę na grupy po 5–10 `MESSAGE_ID`.
2. Dla każdej grupy wypełnij szablon [assets/subagent-prompt-template.md](assets/subagent-prompt-template.md):
   - zastąp `<MESSAGE_IDS>` listą identyfikatorów grupy,
   - zastąp `<SKILL_DIR>` bezwzględną ścieżką katalogu tego skilla.
3. Uruchom podagenta narzędziem `invoke_subagent` z `TypeName: "self"` i `Model: "inherit"`.
4. Zapisz, który podagent (identyfikator konwersacji) ocenia które `MESSAGE_ID`. Krok 4 tego wymaga.

### Krok 3: Zbierz wyniki podagentów

1. Czekaj na wiadomości od podagentów. Nie odpytuj ich w pętli.
2. Zbierz z każdej odpowiedzi listę JSON w formie z punktu 10 szablonu promptu.
3. Jeśli podagent nie zwrócił wyniku dla `MESSAGE_ID` ze swojej grupy → dopisz to do błędów wykonania raportu.

### Krok 4: Dodaj nowe klasy

Dla każdej pozycji z `mode` = `UNKNOWN_TOPIC` wykonaj 4a, w razie potrzeby 4b, a potem 4c.

#### 4a. Wyszukiwanie kontekstowe

1. Zapytaj użytkownika:
   ```json
   {
     "questions": [
       {
         "question": "Email '<Temat>' (od: <Nadawca>) nie pasuje do żadnej klasy. Czy wyszukać w historii skrzynki podobne maile, aby zaproponować bardziej generyczną klasę?",
         "options": [
           "(Recommended) Tak, wyszukaj podobne maile w historii",
           "Nie, pokaż od razu 3 propozycje klasy"
         ],
         "is_multi_select": false
       }
     ]
   }
   ```
2. Jeśli „Nie” → przejdź do 4b.
3. Wyślij narzędziem `send_message` do podagenta, który ocenił wiadomość: `MESSAGE_ID` i polecenie wyszukiwania kontekstowego (punkt 12 szablonu promptu).
4. Zapytaj użytkownika o zestaw. Każdy znaleziony mail to osobna opcja `<data> | <nadawca> | <temat>`, wszystkie zaznaczalne:
   ```json
   {
     "questions": [
       {
         "question": "Zaznacz maile podobne do '<Temat>', które mają trafić do analizy reguł nowej klasy. Odznacz błędne dopasowania.",
         "options": ["<data> | <nadawca> | <temat>", "..."],
         "is_multi_select": true
       }
     ]
   }
   ```
5. Jeśli podagent nie znalazł żadnego maila albo użytkownik nie zaznaczył żadnego → przejdź do 4b.
6. Wyślij narzędziem `send_message` do tego samego podagenta zaznaczone `MESSAGE_ID` i polecenie analizy (punkt 13 szablonu promptu).
7. Przedstaw użytkownikowi propozycję klasy z analizy (`id`, `name`, `description`, `class_weight`, `content_scoring_prompt`, `autonomy_threshold`, `action_auto`, `action_escalated`) i zapytaj:
   ```json
   {
     "questions": [
       {
         "question": "Czy zaakceptować propozycję klasy <id> z analizy podobnych maili?",
         "options": [
           "(Recommended) Akceptuję propozycję",
           "Odrzucam, pokaż 3 standardowe propozycje klasy"
         ],
         "is_multi_select": false
       }
     ]
   }
   ```
8. Jeśli użytkownik zaakceptował → przejdź do 4c z tą propozycją. Jeśli odrzucił → przejdź do 4b.
9. Nie wykonuj żadnych akcji na mailach znalezionych w wyszukiwaniu.

#### 4b. Propozycje standardowe

1. Zapytaj użytkownika. Wypełnij opcje propozycjami z `new_class_proposals`:
   ```json
   {
     "questions": [
       {
         "question": "Email '<Temat>' (od: <Nadawca>) nie pasuje do żadnej klasy. Wybierz nową generyczną klasę:",
         "options": [
           "(Recommended) <Propozycja 1: id> — <name>: <description>",
           "<Propozycja 2: id> — <name>: <description>",
           "<Propozycja 3: id> — <name>: <description>"
         ],
         "is_multi_select": false
       },
       {
         "question": "Wybierz parametry i akcje dla nowej klasy:",
         "options": [
           "(Recommended) Z wybranej propozycji: class_weight=<W>, autonomy_threshold=<T> | action_auto: <lista> | action_escalated: <lista> | content_scoring_prompt: <tekst>",
           "Niski priorytet: class_weight=0.2, autonomy_threshold=0.40 | action_auto: [\"gmail: mutate mark-read {ID}\"] | action_escalated: [\"prompt: powiadom użytkownika o wiadomości\"]",
           "Średni priorytet: class_weight=0.5, autonomy_threshold=0.55 | action_auto: [\"prompt: odnotuj wiadomość w raporcie\", \"gmail: mutate mark-read {ID}\"] | action_escalated: [\"prompt: wypisz wymagane działania i terminy\"]",
           "Wysoki priorytet: class_weight=0.9, autonomy_threshold=0.50 | action_auto: [] | action_escalated: [\"prompt: przeanalizuj wątek szczegółowo i zaproponuj odpowiedź\"]"
         ],
         "is_multi_select": false
       }
     ]
   }
   ```
2. Jeśli użytkownik wybrał profil priorytetu → weź `content_scoring_prompt` z wybranej propozycji klasy.

#### 4c. Zapis klasy

Wykonaj dla propozycji zaakceptowanej w 4a albo wybranej w 4b.

1. Sprawdź każdy wpis `gmail: …` wybranych akcji w pomocy polecenia:
   ```bash
   /google/bin/releases/gemini-agents-gmail/gmail <przestrzeń> <polecenie> --help
   ```
2. Jeśli polecenie, flaga lub liczba argumentów nie zgadza się z pomocą → popraw wpis według pomocy i zapytaj użytkownika o zatwierdzenie poprawionego wpisu.
3. Użyj `id` z propozycji klasy.
4. Dopisz klasę do listy `topics` w `~/.gemini/email_topics.json` ze wszystkimi polami z sekcji „Baza tematów”.
5. Wykonaj procedurę „Walidacja bazy tematów”.
6. Jeśli walidacja zakończy się błędem → popraw klasę, zapytaj użytkownika o zatwierdzenie poprawki i wróć do punktu 5.
7. Wyślij narzędziem `send_message` do podagenta, który ocenił wiadomość: `MESSAGE_ID` i nowy `topic_id`.
8. Zastąp pozycję wiadomości wynikiem zwróconym przez podagenta.

### Krok 5: Przedstaw raport zbiorczy

1. Przedstaw tabelę z jednym wierszem na każdą przetworzoną wiadomość, z kolumnami: `message_id`, nadawca i temat, `topic_id`, `formula`, `autonomy_threshold`, wykonane akcje (`gmail_results` i `prompt_results`).
2. Pod tabelą przedstaw sekcję „Błędy wykonania” ze wszystkimi `execution_errors` od podagentów i błędami z kroku 3. Jeśli błędów nie ma → napisz „Brak błędów wykonania”.

### Krok 6: Przetwórz kolejną paczkę

1. Jeśli zostały nieprzetworzone paczki → wróć do kroku 2 z następną paczką.
2. Jeśli nie zostały → zakończ.

## Procedura: walidacja bazy tematów

Uruchom tę procedurę:
- na prośbę użytkownika, np. po ręcznej edycji bazy,
- po każdej zmianie `~/.gemini/email_topics.json` wykonanej przez skill.

1. Uruchom skrypt walidacji:
   ```bash
   python3 <katalog-skilla>/scripts/validate_topics.py
   ```
2. Jeśli kod wyjścia = 0 → poinformuj użytkownika, że baza jest poprawna.
3. Jeśli kod wyjścia ≠ 0 → przedstaw użytkownikowi wszystkie wypisane problemy.

## Definition of done

- [ ] Każde przetworzone `MESSAGE_ID` ma wiersz w raporcie z kroku 5.
- [ ] Żaden wiersz raportu nie ma `mode` = `UNKNOWN_TOPIC`.
- [ ] Sekcja „Błędy wykonania” zawiera każdy `execution_errors` zwrócony przez podagentów.
- [ ] Po każdej zmianie bazy wykonanej przez skill `validate_topics.py` zakończył się kodem 0.
- [ ] Wszystkie paczki ustalone w kroku 1 są przetworzone.
