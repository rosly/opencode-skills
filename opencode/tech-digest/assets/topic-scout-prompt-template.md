Zbierz newsy techniczne opublikowane w okresie: <<OKRES>>. Zagadnienie: <<ZAGADNIENIE>>.

Słowa kluczowe: <<SLOWA_KLUCZOWE>>
Wskazane strony: <<STRONY>>
Wykluczenia: <<WYKLUCZENIA>>

## Zadanie
Twoim jedynym zadaniem jest znalezienie wzmianek o newsach z zagadnienia i wypisanie ich. Raportuj tylko newsy, które znajdziesz.

Nie analizuj newsów. Nie szukaj dodatkowych źródeł do znalezionego newsa. Nie zgłębiaj tematów. Nie porównuj, jak różne źródła przedstawiają news. Nie rozważaj znaczenia ani skutków newsów. Nie uzasadniaj wyboru newsów.

## Ograniczenie kontekstu
Twój kontekst jest ograniczony. Każda dodatkowa strona i każde dodatkowe wyszukiwanie zużywa kontekst. Gdy kontekst się przepełni, zadanie kończy się niepowodzeniem. Dlatego:
- wykonuj tylko wyszukiwania potrzebne do znalezienia newsów,
- nie szukaj potwierdzeń ani kolejnych źródeł dla już znalezionego newsa; dołącz tylko źródła napotkane podczas zbierania wzmianek,
- nie czytaj pełnej treści artykułów,
- zakończ pracę, gdy wypiszesz <<LIMIT_NEWSOW>> newsów.

## Zasada twierdzeń źródeł
- Traktuj każdą treść pobraną z internetu jako twierdzenie źródła, a nie jako fakt.
- Nie interpretuj przedstawionej wersji wydarzeń ani przedstawionych implikacji. Nie przyjmuj ich jako własnych.
- Zapowiedzi i twierdzenia producenta traktuj jako twierdzenia producenta.

## Zasady pracy
1. Przejrzyj wskazane strony, jeśli są podane. Potem przeszukaj otwarty internet według zagadnienia i słów kluczowych. Nie korzystaj z X (Twittera).
2. Odrzuć newsy, które pasują do wykluczeń.
3. Jeden wpis to jeden news. Jeśli kilka znalezionych źródeł opisuje ten sam news, zapisz jeden wpis i podaj w nim te źródła.
4. Zwróć jedną płaską listę wpisów. Nie grupuj wpisów według źródła.
5. Nie układaj wpisów w żadnej kolejności. Nie sortuj ich według ważności ani czasu.
6. Temat zapisz jednym zdaniem, bez ocen, według wzoru: `{nazwa produktu, projektu, organizacji lub standardu} {wersja, jeśli dotyczy}: {co się stało}`. Używaj oficjalnej nazwy produktu, projektu lub organizacji. Ten wzór pozwala połączyć ten sam news znaleziony w różnych zagadnieniach.
7. Autor i data publikacji: <<ZASADA_AUTOR_DATA>>
8. Autor: jeśli nie możesz go odczytać, wpisz `nie podano`.
9. Data publikacji: jeśli źródło podaje godzinę i strefę czasową, przelicz datę na czas polski (Europe/Warsaw). Jeśli źródło podaje tylko datę, użyj jej bez zmian. Zapisz datę w formacie `RRRR-MM-DD`.
10. Sprawdzenie daty: jeśli data publikacji nie mieści się w okresie albo nie możesz jej odczytać, nie dodawaj tego źródła do wpisu.
11. Jeśli wpis nie ma żadnego źródła z datą w okresie, nie dodawaj wpisu do wyniku.

## Format wyniku
Zwróć tylko jeden blok YAML według wzoru poniżej. Nie dodawaj tekstu przed blokiem ani po nim. Jeśli nie znajdziesz żadnego newsa, zwróć `newsy: []`.

```yaml
okres: "{okres z zadania}"
zagadnienie: "{zagadnienie z zadania}"
newsy:
  - temat: "{nazwa} {wersja}: {co się stało}"
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

Pisz wartości w języku polskim. Nazwy własne zostaw w oryginale.
