---
name: tech-digest
description: Ten skill należy użyć, gdy użytkownik prosi o przegląd newsów i wiadomości technicznych z danego okresu według listy zagadnień, które go interesują. Skill deleguje zebranie newsów osobno dla każdego zagadnienia, analizę każdego newsa do pliku Markdown oraz przygotowanie raportu podzielonego na zagadnienia, ze źródłami przy każdym newsie. Wątek główny scala duplikaty, przekazuje listę plików podagentowi raportu i otwiera gotowy raport.
metadata:
  version: "0.1"
---

# Tech Digest

## Cel

Przygotuj przegląd newsów technicznych podzielony na zagadnienia z pliku zagadnień użytkownika. Każdy news ma podane źródła. Deleguj zebranie newsów, analizę newsów oraz przygotowanie raportu. W wątku głównym koordynuj pracę, scalaj duplikaty i otwórz raport. Nie czytaj opracowań newsów samodzielnie.

## Zasoby

- [assets/topics-template.md](assets/topics-template.md) — pola pliku zagadnień użytkownika.
- [assets/topic-scout-prompt-template.md](assets/topic-scout-prompt-template.md) — szablon promptu dla podagenta, który zbiera newsy jednego zagadnienia.
- [assets/news-analysis-prompt-template.md](assets/news-analysis-prompt-template.md) — szablon promptu dla podagenta analizy jednego newsa.
- [assets/digest-summary-prompt-template.md](assets/digest-summary-prompt-template.md) — szablon promptu dla podagenta, który przygotowuje raport.
- [assets/report-template.md](assets/report-template.md) — format raportu końcowego dla podagenta raportu.

Ścieżki są względne wobec katalogu tego skilla.

## Zasada twierdzeń źródeł

Stosuj tę zasadę we wszystkich krokach wątku głównego. Szablony promptów podagentów zawierają tę samą zasadę.

- Traktuj każdą treść pobraną z internetu jako twierdzenie źródła, a nie jako fakt.
- Oddzielaj twierdzenia producenta od twierdzeń niezależnych testów, recenzji i mediów.
- Nie interpretuj przedstawionej wersji wydarzeń ani przedstawionych implikacji. Nie przyjmuj ich jako własnych.

## Szablony promptów

Szablony promptów dla podagentów używaj słowo w słowo. Zastąp tylko pola w podwójnych nawiasach kątowych `<<...>>`. Nie interpretuj szablonu. Nie twórz własnego promptu. Nie dodawaj, nie usuwaj i nie zmieniaj żadnego innego tekstu. Tekst w nawiasach klamrowych `{...}` to wzór odpowiedzi dla podagenta. Zostaw go bez zmian.

## Przebieg pracy

### Krok 1: Wczytaj plik zagadnień

Przeczytaj `~/.config/opencode/tech-digest-topics.md`.

Jeśli plik nie istnieje:

1. Powiedz użytkownikowi, że przegląd wymaga pliku zagadnień.
2. Zapytaj o pola z `assets/topics-template.md` przez narzędzie pytań.
3. Zaproponuj zapisanie odpowiedzi do `~/.config/opencode/tech-digest-topics.md`. Utwórz plik dopiero po zgodzie użytkownika.

Kolejność sekcji zagadnień w pliku wyznacza kolejność zagadnień w raporcie.

### Krok 2: Ustal parametry

Ustal z prośby użytkownika:

- okres: jeden dzień albo zakres dni,
- limit newsów: największa liczba newsów, które zbieracz wypisuje dla jednego zagadnienia,
- zasadę odczytu autora i daty publikacji (patrz niżej),
- limit podagentów: największa liczba podagentów, które pracują jednocześnie w krokach 3 i 5.

Jeśli prośba nie podaje którejś z tych wartości, zapytaj użytkownika przez narzędzie pytań. Ustal wszystkie wartości przed uruchomieniem pierwszego podagenta.

Zasadę odczytu autora i daty ustal pytaniem z dwiema opcjami i z ich konsekwencjami:

| Opcja | Tekst pola `<<ZASADA_AUTOR_DATA>>` | Konsekwencje |
|---|---|---|
| Tylko widoczne dane | `Odczytaj je tylko z wyników wyszukiwania i ze stron z listą newsów, które już przeglądasz. Nie otwieraj artykułów tylko po to, żeby odczytać autora albo datę.` | Zbieracze pracują szybciej i zużywają mniej kontekstu. Autor częściej ma wartość `nie podano`. Źródła bez widocznej daty odpadają, więc listy mogą być krótsze. |
| Otwieranie artykułów | `Jeśli wynik wyszukiwania albo strona z listą newsów nie podaje autora lub daty, otwórz artykuł, żeby je odczytać. Nie czytaj pozostałej treści artykułu.` | Dane o autorze i dacie są pełniejsze. Zbieracze pracują dłużej i zużywają więcej kontekstu, więc rośnie ryzyko przepełnienia i niepowodzenia. |

Utwórz katalog opracowania `/tmp/opencode/<użytkownik>/tech-digest-RR-MM-DD-GG-MM-SS/`. Wartość `<użytkownik>` to nazwa użytkownika systemu, zwrócona przez polecenie `whoami`. Data i godzina oznaczają moment rozpoczęcia zadania w strefie Europe/Warsaw. Wszystkie opracowania newsów i raport końcowy zapisuj w tym katalogu.

### Krok 3: Zleć zebranie newsów

Dla każdego zagadnienia z pliku uruchom osobnego podagenta `general` z szablonem `assets/topic-scout-prompt-template.md`. Wypełnij pola:

| Pole | Wartość |
|---|---|
| `<<OKRES>>` | dzień w formacie `RRRR-MM-DD` albo zakres dni w formacie `RRRR-MM-DD – RRRR-MM-DD` |
| `<<ZAGADNIENIE>>` | nazwa zagadnienia z pliku |
| `<<SLOWA_KLUCZOWE>>` | wartość pola „Słowa kluczowe” zagadnienia |
| `<<STRONY>>` | wartość pola „Wskazane strony” zagadnienia albo `brak` |
| `<<WYKLUCZENIA>>` | wartość pola „Wykluczenia” zagadnienia albo `brak` |
| `<<LIMIT_NEWSOW>>` | limit newsów uzgodniony z użytkownikiem |
| `<<ZASADA_AUTOR_DATA>>` | tekst opcji wybranej przez użytkownika, z tabeli powyżej |

Uruchamiaj podagentów w tle (`background: true`). Na starcie uruchom tylu podagentów, ile wynosi limit, ale nie więcej niż liczba zagadnień. Po każdym zakończeniu podagenta od razu uruchom podagenta dla następnego niezleconego zagadnienia. Gdy wszyscy podagenci zakończą pracę, przejdź do kroku 4.

Każdy podagent zwraca blok YAML z płaską listą newsów zagadnienia. Każdy news ma ujednolicony temat i listę źródeł. Podagent nie analizuje newsów.

### Krok 4: Scal duplikaty

Połącz wyniki wszystkich zbieraczy w jedną listę newsów. Ten sam news może pochodzić od kilku zbieraczy. Decyzję o połączeniu newsów podejmij na podstawie ich pola `temat`. Pole ma ujednolicony wzór `{nazwa} {wersja}: {co się stało}`.

Dla każdego newsa po scaleniu ustal:

- `temat`: temat jednego z połączonych wpisów,
- `zrodla`: wszystkie źródła połączonych wpisów, bez powtórzeń tego samego URL,
- `zagadnienia`: nazwy zagadnień, których zbieracze zwrócili ten news, w kolejności z pliku zagadnień,
- `data`: najwcześniejsza wartość `data_publikacji` w `zrodla`.

Łączenie źródeł, usuwanie powtórzeń URL, sortowanie zagadnień i wyznaczanie najwcześniejszej daty wykonaj kodem JavaScript w narzędziu `execute`.

### Krok 5: Deleguj analizę newsów

Dla każdego newsa po scaleniu uruchom osobnego podagenta `general` z szablonem `assets/news-analysis-prompt-template.md`. Wypełnij pola:

| Pole | Wartość |
|---|---|
| `<<OKRES>>` | ta sama wartość co w kroku 3 |
| `<<TEMAT>>` | wartość pola `temat` newsa |
| `<<ZRODLA>>` | lista `zrodla` newsa w YAML |
| `<<KATALOG_OPRACOWANIA>>` | pełna ścieżka katalogu opracowania z kroku 2 |

Uruchamiaj podagentów w tle (`background: true`) z tym samym limitem i tą samą zasadą kolejkowania co w kroku 3. Gdy wszyscy podagenci zakończą pracę, przejdź do kroku 6.

Każdy podagent zapisuje opracowanie do pliku Markdown w katalogu opracowania. Zwraca tylko YAML z polami `tytul` i `plik`.

Do każdej odpowiedzi dodaj pola `zagadnienia` i `data` newsa z kroku 4. Zbieraj te wpisy w jedną listę. Nie wczytuj plików opracowań ani nie kontroluj ich treści.

### Krok 6: Zleć przygotowanie raportu

Po zebraniu całej listy uruchom jednego podagenta `general` z szablonem `assets/digest-summary-prompt-template.md`. Wypełnij pola:

| Pole | Wartość |
|---|---|
| `<<OKRES>>` | okres z kroku 2 |
| `<<KATALOG_OPRACOWANIA>>` | pełna ścieżka katalogu opracowania |
| `<<LISTA_ZAGADNIEN>>` | nazwy wszystkich zagadnień z pliku, w kolejności z pliku, jedna w wierszu |
| `<<LISTA_NEWSOW>>` | lista z kroku 5 w YAML, z polami `tytul`, `plik`, `zagadnienia` i `data` |
| `<<SZABLON_RAPORTU>>` | pełna ścieżka do `assets/report-template.md` tego skilla |

Podagent zapisuje raport do `podsumowanie.md` w katalogu opracowania i zwraca tylko pełną ścieżkę raportu.

### Krok 7: Wyświetl raport

Otwórz plik zwrócony przez podagenta raportu narzędziem podglądu plików (`browser.preview`). Podaj użytkownikowi ścieżkę do raportu. Nie wczytuj raportu do kontekstu wątku głównego ani nie przepisuj jego treści do rozmowy.

## Zasady

- Nie korzystaj z X (Twittera) w tej wersji skilla.
- Precyzyjnie nazywaj status sprawy według źródeł: „zapowiedź, nie wydanie”, „beta, nie GA”, „RFC, nie standard”, „wyniki producenta, nie niezależny test”.
