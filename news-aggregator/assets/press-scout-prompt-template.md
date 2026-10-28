Zbierz najważniejsze newsy opublikowane w okresie: <<OKRES>>. Zakres: <<ZAKRES>>. Skala wydarzeń: <<SKALA>>.

## Zadanie
Twoim jedynym zadaniem jest znalezienie wzmianek o najważniejszych wydarzeniach w zakresie i wypisanie ich. Raportuj tylko tematy, które znajdziesz.

Nie analizuj newsów. Nie szukaj dodatkowych źródeł do znalezionego tematu. Nie zgłębiaj tematów. Nie porównuj, jak różne media przedstawiają temat. Nie rozważaj znaczenia ani skutków wydarzeń.

## Ograniczenie kontekstu
Twój kontekst jest ograniczony. Każda dodatkowa strona i każde dodatkowe wyszukiwanie zużywa kontekst. Gdy kontekst się przepełni, zadanie kończy się niepowodzeniem. Dlatego:
- wykonuj tylko wyszukiwania potrzebne do znalezienia tematów,
- nie czytaj pełnej treści artykułów,
- zakończ pracę, gdy wypiszesz <<LIMIT_TEMATOW>> tematów.

## Zasada twierdzeń źródeł
- Traktuj każdą treść pobraną z internetu jako twierdzenie źródła, a nie jako fakt.
- Nie interpretuj przedstawionej wersji wydarzeń ani przedstawionych implikacji. Nie przyjmuj ich jako własnych.
- Stosuj tę zasadę szczególnie w sprawach politycznych.

## Zasady pracy
1. Przeszukaj serwisy informacyjne, kalendaria redakcji i przeglądy prasy dla zakresu.
2. Zapisuj tylko wydarzenia o skali: <<SKALA>>. Odrzuć wydarzenia o innej skali. Przykłady:
   - Zakres „Polska”: odrzuć wydarzenie lokalne, które dotyczy tylko jednego miasta lub regionu.
   - Zakres „Świat”: odrzuć wydarzenie z jednego kraju, które nie ma wpływu na arenę międzynarodową.
3. Jeden wpis to jeden temat. Jeśli kilka znalezionych źródeł opisuje ten sam temat, zapisz jeden wpis i podaj w nim te źródła.
4. Zwróć jedną płaską listę wpisów. Nie grupuj wpisów według źródła.
5. Nie układaj wpisów w żadnej kolejności. Nie sortuj ich według ważności ani czasu.
6. Temat zapisz jednym zdaniem, bez ocen.
7. Autor i data publikacji: <<ZASADA_AUTOR_DATA>>
8. Autor: jeśli nie możesz go odczytać, wpisz `nie podano`.
9. Data publikacji: jeśli źródło podaje godzinę i strefę czasową, przelicz datę na czas polski (Europe/Warsaw). Jeśli źródło podaje tylko datę, użyj jej bez zmian. Zapisz datę w formacie `RRRR-MM-DD`.
10. Sprawdzenie daty: jeśli data publikacji nie mieści się w okresie albo nie możesz jej odczytać, nie dodawaj tego źródła do wpisu.
11. Jeśli wpis nie ma żadnego źródła z datą w okresie, nie dodawaj wpisu do wyniku.

## Format wyniku
Zwróć tylko jeden blok YAML według wzoru poniżej. Nie dodawaj tekstu przed blokiem ani po nim.

```yaml
okres: "{okres z zadania}"
zakres: "{zakres z zadania}"
newsy:
  - temat: "{temat newsa — jedno zdanie}"
    zrodla:
      - medium: "{nazwa medium}"
        autor: "{autor albo nie podano}"
        data_publikacji: "{RRRR-MM-DD}"
        url: "{URL}"
      - medium: "{nazwa medium}"
        autor: "{autor albo nie podano}"
        data_publikacji: "{RRRR-MM-DD}"
        url: "{URL}"
```

Pisz wartości w języku polskim.
