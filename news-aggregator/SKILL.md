---
name: news-aggregator
description: Ten skill należy użyć, gdy użytkownik pyta, co wydarzyło się dziś lub w danym dniu, prosi o wiadomości z kraju, regionu, miasta lub tematu albo pyta, które bieżące wydarzenia mają znaczenie dla jego życia. Skill zleca podagentowi zebranie tematów ze źródłami z okresu zadania, deleguje analizę każdego newsa do osobnego podagenta, który przedstawia twierdzenia źródeł z przypisaniem do mediów, a następnie w wątku głównym sortuje wydarzenia według wpływu na życie użytkownika w aspektach i horyzontach czasowych, na podstawie pliku profilu.
metadata:
  version: "0.8"
---

# News Aggregator

## Cel

Przygotuj przegląd wiadomości, który pokazuje, co twierdzą różne źródła, i sortuje wydarzenia według wpływu na życie użytkownika. Podagenci zbierają i przypisują twierdzenia źródeł. Wątek główny ocenia wpływ na użytkownika i sortuje wydarzenia.

## Zasoby

- [assets/press-scout-prompt-template.md](assets/press-scout-prompt-template.md) — szablon promptu dla podagenta, który zbiera tematy.
- [assets/news-analysis-prompt-template.md](assets/news-analysis-prompt-template.md) — szablon promptu dla podagenta analizy jednego newsa.
- [assets/report-template.md](assets/report-template.md) — format raportu końcowego w wątku głównym.
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

Nie zapisuj danych osobowych w żadnym innym miejscu. Nie dodawaj profilu do GIT.

### Krok 2: Zleć zebranie tematów

Ustal z prośby użytkownika:

- okres: jeden dzień albo zakres dni,
- zakres: jeden obszar, na przykład świat, kraj, województwo albo miasto,
- limit tematów: największa liczba tematów, które zbieracz wypisuje,
- zasadę odczytu autora i daty publikacji (patrz niżej),
- limit podagentów: największa liczba podagentów analizy, które pracują jednocześnie w kroku 3.

Jeśli prośba nie podaje którejś z tych wartości, zapytaj użytkownika przez narzędzie pytań. Ustal wszystkie wartości przed uruchomieniem pierwszego podagenta.

Zadanie ma dokładnie jeden zakres. Nie przyjmuj kilku zakresów, które się nakładają. Jeśli użytkownik poda kilka zakresów, poproś go o wybór jednego. Pytając o zakres, nie proponuj podzakresów.

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

### Krok 3: Deleguj analizę newsów

Dla każdego newsa z bloku YAML uruchom osobnego podagenta `general` z szablonem `assets/news-analysis-prompt-template.md`. Wypełnij pola:

| Pole | Wartość |
|---|---|
| `<<OKRES>>` | ta sama wartość co w kroku 2 |
| `<<ZAKRES>>` | ta sama wartość co w kroku 2 |
| `<<TEMAT>>` | wartość pola `temat` newsa |
| `<<ZRODLA>>` | lista `zrodla` newsa, skopiowana z bloku YAML bez zmian |

Uruchamiaj podagentów w tle (`background: true`). Na starcie uruchom tylu podagentów, ile wynosi limit, ale nie więcej niż liczba newsów. Po każdym zakończeniu podagenta od razu uruchom podagenta dla następnego niezleconego newsa. Gdy wszyscy podagenci zakończą pracę, przejdź do kroku 4.

Nie przekazuj podagentom profilu użytkownika. Ocena wpływu na użytkownika należy do wątku głównego.

Nie kontroluj wyników podagentów w wątku głównym. Każdy podagent sam odpowiada za dobór liczby i różnorodności źródeł, które razem dają obiektywny obraz sytuacji.

### Krok 4: Oceń wpływ na użytkownika

Dla każdego newsa oceń wpływ na użytkownika na podstawie profilu i wyniku podagenta. Użyj aspektów i horyzontów poniżej.

**Aspekty:**

| Aspekt | Zakres |
|---|---|
| Finanse | ceny, podatki, raty, świadczenia, koszty życia |
| Prawo i obowiązki | nowe prawa, obowiązki, terminy formalne, zakazy |
| Bezpieczeństwo | bezpieczeństwo fizyczne, ochrona ludności, zagrożenia |
| Codzienność | transport, pogoda, usługi, zakupy, logistyka dnia |
| Praca i kariera | rynek pracy, branża, miejsca pracy w regionie użytkownika |
| Zdrowie | zdrowie, usługi medyczne, NFZ |
| Rodzina | dzieci, edukacja, opieka |

**Horyzonty czasowe** (moment, w którym wpływ zaczyna dotyczyć użytkownika):

| Horyzont | Znaczenie |
|---|---|
| H1 | dziś lub jutro |
| H2 | do miesiąca |
| H3 | do roku |
| H4 | 1–5 lat |
| H5 | ponad 5 lat albo tylko kontekst |

Dla każdego newsa zapisz:

- aspekty, których dotyczy, każdy z konkretnym skutkiem dla użytkownika (na przykład „+6,50 zł za bak 50 l”),
- horyzont,
- czy wpływ jest bezpośredni, czy pośredni,
- pola profilu, na których opiera się ocena,
- twierdzenia źródeł, na których opiera się ocena, z przypisaniem do źródła lub środowiska źródeł.

Jeśli ocena zależy od twierdzenia tylko jednego źródła, od twierdzenia spornego między źródłami albo od brakującego pola profilu, zaznacz to. Nie przedstawiaj skutku założenia jako faktu.

### Krok 5: Posortuj i napisz raport

Sortuj newsy najpierw według horyzontu (H1 przed H5). W tym samym horyzoncie wpływ bezpośredni umieść przed pośrednim, a potem newsy dotyczące większej liczby aspektów przed newsami dotyczącymi mniejszej liczby.

Napisz raport według `assets/report-template.md`, w języku użytkownika. Zakończ krótkim podsumowaniem 1–3 newsów najważniejszych dla użytkownika.

## Zasady

- Nie pomijaj newsa z powodu małego wpływu. Umieść go w ostatnim horyzoncie.
- Precyzyjnie nazywaj status sprawy według źródeł: „zatrzymanie, nie wyrok”, „projekt, nie ustawa”, „scenariusz modelowy, nie oficjalna prognoza”.
- Wypowiedzi oficjalne cytuj dosłownie, z nazwiskiem i funkcją osoby.
