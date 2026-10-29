---
name: knowledge-database
description: Ten skill należy użyć, gdy użytkownik wraca do problemu, który wystąpił już na tej maszynie, pracuje z lokalnym projektem albo gdy sesja wypracowała wiedzę wartą zachowania: obserwacje, wnioski, wyniki researchu lub praktyczne porady. Skill przeszukuje lokalną bazę wiedzy przez codebase_search i proponuje zapis nowej wiedzy do tej bazy.
metadata:
  version: "0.1"
---

# Knowledge Database

## Cel

Baza `/mnt/e/workspace/wiedza` przechowuje wiedzę z poprzednich sesji na tej maszynie. Korzystaj z niej przed rozwiązywaniem znanych problemów. Uzupełniaj ją o wiedzę wypracowaną w sesji.

## Odczyt

1. Gdy pytanie dotyczy tej maszyny lub lokalnego projektu, wywołaj `codebase_search` z `projectPath: "/mnt/e/workspace/wiedza"`. Zrób to przed własną analizą.
2. Użyj najwyżej 3 zapytań. Sformułuj je po polsku i po angielsku. Brak wyników nie dowodzi, że bazie brakuje tematu.
3. Otwórz plik z wyniku i przeczytaj potrzebny fragment. Nie opieraj się na samym fragmencie z wyszukiwania.
4. Notatka opisuje stan z dnia zapisu. Przed podaniem poleceń sprawdź aktualny stan systemu, jeśli może się on różnić.
5. Podaj w odpowiedzi ścieżkę wykorzystanej notatki.
6. Jeśli MCP zwraca błąd, zgłoś to użytkownikowi. Nie diagnozuj go i nie naprawiaj.

## Zapis

Rodzaje wpisów:

- obserwacja: polecenie, wynik i środowisko,
- wniosek: co z obserwacji wynika i na jakiej podstawie,
- research: źródła z linkiem i datą pobrania,
- porada: krótka instrukcja „jak zrobić X” albo „uważaj na Y”.

Reguły:

1. Na końcu zadania, które wypracowało nową wiedzę, zaproponuj zapis. Podaj ścieżkę docelową i streszczenie w 2–3 punktach. Zapisz dopiero po zgodzie użytkownika.
2. Najpierw poszukaj istniejącej notatki o tym temacie przez `codebase_search` i listę katalogów. Uzupełnij ją zamiast tworzyć duplikat.
3. Nowy temat umieść w katalogu `<temat-kebab-case>/` z plikiem `README.md`.
4. Na początku notatki podaj datę, środowisko (sprzęt i wersje oprogramowania) oraz cel.
5. Oddziel obserwacje od wniosków i porad. Wniosek bez obserwacji lub źródła oznacz jako hipotezę.
6. Pisz notatki po polsku. Polecenia, ścieżki, nazwy i cytaty zostaw w oryginale.
7. Nie zapisuj sekretów: tokenów, haseł, kluczy API ani prywatnych danych.
8. Nie uruchamiaj indeksowania ani aktualizacji indeksu. SocratiCode robi to sam.
