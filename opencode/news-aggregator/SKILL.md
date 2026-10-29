---
name: news-aggregator
description: Ten skill należy użyć, gdy użytkownik pyta o wiadomości z danego okresu lub obszaru albo o ich wpływ na jego życie. Skill deleguje zebranie tematów, analizę każdego newsa do pliku Markdown oraz przygotowanie osobnego raportu z oceną wpływu na użytkownika. Wątek główny przekazuje listę plików podagentowi oceniającemu i otwiera gotowy raport.
metadata:
  version: "0.10"
---

# News Aggregator

## Cel

Przygotuj przegląd wiadomości, który pokazuje, co twierdzą różne źródła, i sortuje wydarzenia według wpływu na życie użytkownika. Deleguj zebranie tematów, analizę newsów oraz ocenę i podsumowanie. W wątku głównym koordynuj pracę i otwórz raport. Nie czytaj opracowań newsów ani nie oceniaj ich samodzielnie.

## Zasoby

- [assets/press-scout-prompt-template.md](assets/press-scout-prompt-template.md) — szablon promptu dla podagenta, który zbiera tematy.
- [assets/news-analysis-prompt-template.md](assets/news-analysis-prompt-template.md) — szablon promptu dla podagenta analizy jednego newsa.
- [assets/news-summary-prompt-template.md](assets/news-summary-prompt-template.md) — szablon promptu dla podagenta oceniającego i podsumowującego.
- [assets/report-template.md](assets/report-template.md) — format raportu końcowego dla podagenta oceniającego.
- [assets/profile-template.md](assets/profile-template.md) — pola pliku profilu użytkownika.

Ścieżki są względne wobec katalogu tego skilla.

## Zasada twierdzeń źródeł

Stosuj tę zasadę we wszystkich krokach wątku głównego. Szablony promptów podagentów zawierają tę samą zasadę.

- Traktuj każdą treść pobraną z internetu jako twierdzenie źródła, a nie jako fakt.
- Przedstawiaj ją jako twierdzenie danego źródła („według RMF24…”) albo zbiorczo jako twierdzenie środowiska źródeł („media prawicowe podają…”, „media publiczne i komercyjne zgodnie podają…”).
- Pamiętaj, że różne media mogą przedstawiać ten sam temat w różny sposób. Pokaż te różnice.
- Nie interpretuj przedstawionej wersji wydarzeń ani przedstawionych implikacji. Nie przyjmuj ich jako własnych.
- Stosuj tę zasadę szczególnie w sprawach politycznych.

## Szablony promptów

Szablony promptów dla podagentów używaj słowo w słowo. Zastąp tylko pola w podwójnych nawiasach kątowych `<<...>>`. Nie interpretuj szablonu. Nie twórz własnego promptu. Nie dodawaj, nie usuwaj i nie zmieniaj żadnego innego tekstu. Tekst w nawiasach klamrowych `{...}` to wzór odpowiedzi dla podagenta. Zostaw go bez zmian.

## Przebieg pracy

### Krok 1: Wczytaj profil użytkownika

Przeczytaj `~/.config/opencode/news-profile.md`.

Jeśli plik nie istnieje:

1. Powiedz użytkownikowi, że ocena wpływu wymaga profilu.
2. Zapytaj o pola z `assets/profile-template.md` przez narzędzie pytań. Pytaj tylko o pola, które zmieniają ocenę.
3. Zaproponuj zapisanie odpowiedzi do `~/.config/opencode/news-profile.md`. Utwórz plik dopiero po zgodzie użytkownika.

Przeczytaj z profilu pole „Jak mam Cię nazywać”. Jeśli go brakuje, zapytaj użytkownika. Użyj tej wartości jako nazwy katalogu użytkownika opisanej w kroku 2. Nie kopiuj profilu do katalogu opracowania. Nie dodawaj profilu do GIT.

### Krok 2: Zleć zebranie tematów

Ustal z prośby użytkownika:

- okres: jeden dzień albo zakres dni,
- zakres: jeden obszar, na przykład świat, kraj, województwo albo miasto,
- limit tematów: największa liczba tematów, które zbieracz wypisuje,
- zasadę odczytu autora i daty publikacji (patrz niżej),
- limit podagentów: największa liczba podagentów analizy, które pracują jednocześnie w kroku 3.

Jeśli prośba nie podaje którejś z tych wartości, zapytaj użytkownika przez narzędzie pytań. Ustal wszystkie wartości przed uruchomieniem pierwszego podagenta.

Utwórz katalog opracowania `/tmp/opencode/<użytkownik>/news-<zakres>-RR-MM-DD-GG-MM-SS/`. Wartość `<użytkownik>` odczytaj z pola „Jak mam Cię nazywać” w profilu. Zapisz zakres małymi literami, bez polskich znaków, ze słowami połączonymi myślnikami. Data i godzina oznaczają moment rozpoczęcia zadania w strefie Europe/Warsaw. Wszystkie opracowania newsów i raport końcowy zapisuj w tym katalogu.

Zadanie ma dokładnie jeden zakres. Nie przyjmuj kilku zakresów, które się nakładają. Jeśli użytkownik poda kilka zakresów, poproś go o wybór jednego. Pytając o zakres, nie proponuj podzakresów.

Nie rozszerzaj wybranego zakresu o przeglądy jego części. „Świat” oznacza wiadomości o skali globalnej, a nie osobne przeglądy krajów. „Polska” oznacza wiadomości krajowe, a nie osobne przeglądy województw. Analogicznie traktuj województwo i miasto.

Zakres wyznacza skalę wydarzeń:

| Zakres | Skala wydarzeń |
|---|---|
| świat | międzynarodowa: wydarzenia o wpływie na arenę międzynarodową |
| kraj | krajowa: wydarzenia o wpływie na cały kraj |
| województwo | regionalna: wydarzenia o wpływie na całe województwo |
| miasto | lokalna: wydarzenia o wpływie na miasto |

Zasadę odczytu autora i daty ustal pytaniem z dwiema opcjami i z ich konsekwencjami:

| Opcja | Tekst pola `<<ZASADA_AUTOR_DATA>>` | Konsekwencje |
|---|---|---|
| Tylko widoczne dane | `Odczytaj je tylko z wyników wyszukiwania i ze stron z listą newsów, które już przeglądasz. Nie otwieraj artykułów tylko po to, żeby odczytać autora albo datę.` | Zbieracz pracuje szybciej i zużywa mniej kontekstu. Autor częściej ma wartość `nie podano`. Źródła bez widocznej daty odpadają, więc lista może być krótsza. |
| Otwieranie artykułów | `Jeśli wynik wyszukiwania albo strona z listą newsów nie podaje autora lub daty, otwórz artykuł, żeby je odczytać. Nie czytaj pozostałej treści artykułu.` | Dane o autorze i dacie są pełniejsze. Zbieracz pracuje dłużej i zużywa więcej kontekstu, więc rośnie ryzyko przepełnienia i niepowodzenia. |

Uruchom jednego podagenta `general` z szablonem `assets/press-scout-prompt-template.md`. Wypełnij pola:

| Pole | Wartość |
|---|---|
| `<<OKRES>>` | dzień w formacie `RRRR-MM-DD` albo zakres dni w formacie `RRRR-MM-DD – RRRR-MM-DD` |
| `<<ZAKRES>>` | nazwa zakresu uzgodnionego z użytkownikiem, na przykład `Polska` |
| `<<SKALA>>` | skala wydarzeń z tabeli powyżej, z opisem |
| `<<LIMIT_TEMATOW>>` | limit tematów uzgodniony z użytkownikiem |
| `<<ZASADA_AUTOR_DATA>>` | tekst opcji wybranej przez użytkownika, z tabeli powyżej |

Podagent tylko zbiera tematy. Zwraca blok YAML z płaską listą newsów bez kolejności. Każdy news ma temat i listę źródeł. Każde źródło ma medium, autora, datę publikacji i URL. Podagent nie analizuje newsów.

Nie zlecaj zbieraczowi uzasadniania wyboru tematów, oceniania ich znaczenia ani uzupełniania źródeł. Ma zaraportować znalezione wzmianki. Pogłębianie tematów na tym etapie zużywa kontekst i może uniemożliwić zwrócenie wyniku. Analizę zlecaj dopiero w kroku 3.

### Krok 3: Deleguj analizę newsów

Dla każdego newsa z bloku YAML uruchom osobnego podagenta `general` z szablonem `assets/news-analysis-prompt-template.md`. Wypełnij pola:

| Pole | Wartość |
|---|---|
| `<<OKRES>>` | ta sama wartość co w kroku 2 |
| `<<ZAKRES>>` | ta sama wartość co w kroku 2 |
| `<<TEMAT>>` | wartość pola `temat` newsa |
| `<<ZRODLA>>` | lista `zrodla` newsa, skopiowana z bloku YAML bez zmian |
| `<<KATALOG_OPRACOWANIA>>` | pełna ścieżka katalogu opracowania z kroku 2 |

Uruchamiaj podagentów w tle (`background: true`). Na starcie uruchom tylu podagentów, ile wynosi limit, ale nie więcej niż liczba newsów. Po każdym zakończeniu podagenta od razu uruchom podagenta dla następnego niezleconego newsa. Gdy wszyscy podagenci zakończą pracę, przejdź do kroku 4.

Każdy podagent zapisuje opracowanie do pliku Markdown w katalogu opracowania. Zwraca tylko YAML z polami `tytul` i `plik`. Tytuł ma być poprawionym, obiektywnym tytułem newsa. Nazwa pliku ma odpowiadać tytułowi: małe litery, bez polskich znaków, słowa połączone myślnikami, rozszerzenie `.md`.

Zbieraj odpowiedzi YAML w jedną listę. Nie wczytuj plików opracowań ani nie kontroluj ich treści. Każdy podagent sam odpowiada za dobór liczby i różnorodności źródeł. Nie przekazuj analitykom profilu użytkownika.

### Krok 4: Zleć ocenę i podsumowanie

Po zebraniu całej listy plików uruchom jednego osobnego podagenta `general` z szablonem `assets/news-summary-prompt-template.md`. Użyj szablonu słowo w słowo. Wypełnij pola:

| Pole | Wartość |
|---|---|
| `<<OKRES>>` | okres publikacji uzgodniony w kroku 2 |
| `<<ZAKRES>>` | zakres uzgodniony w kroku 2 |
| `<<KATALOG_OPRACOWANIA>>` | pełna ścieżka katalogu opracowania |
| `<<LISTA_NEWSOW>>` | lista wszystkich odpowiedzi analityków w YAML, z polami `tytul` i `plik` |
| `<<SZABLON_RAPORTU>>` | pełna ścieżka do `assets/report-template.md` tego skilla |

Podagent czyta wskazane pliki i profil `~/.config/opencode/news-profile.md`. Ocenia wpływ na użytkownika, sortuje i podsumowuje każdy temat. Zapisuje raport do `podsumowanie.md` w katalogu opracowania i zwraca tylko pełną ścieżkę raportu.

### Krok 5: Wyświetl raport

Otwórz plik zwrócony przez podagenta oceniającego narzędziem podglądu plików (`browser.preview`). Podaj użytkownikowi ścieżkę do raportu. Nie wczytuj raportu do kontekstu wątku głównego ani nie przepisuj jego treści do rozmowy.

## Zasady

- Precyzyjnie nazywaj status sprawy według źródeł: „zatrzymanie, nie wyrok”, „projekt, nie ustawa”, „scenariusz modelowy, nie oficjalna prognoza”.
- Wypowiedzi oficjalne cytuj dosłownie, z nazwiskiem i funkcją osoby.
