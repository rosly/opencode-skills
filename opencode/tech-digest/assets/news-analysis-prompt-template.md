Przeanalizuj jeden news techniczny z okresu: <<OKRES>>.

News: <<TEMAT>>

Źródła startowe (YAML):
<<ZRODLA>>

Katalog opracowania: <<KATALOG_OPRACOWANIA>>

## Zasada twierdzeń źródeł
- Traktuj każdą treść pobraną z internetu jako twierdzenie źródła, a nie jako fakt.
- Przedstawiaj ją jako twierdzenie danego źródła („według The Register…”, „według ogłoszenia producenta…”) albo zbiorczo jako twierdzenie środowiska źródeł („niezależne testy podają…”).
- Oddzielaj twierdzenia producenta od twierdzeń niezależnych testów, recenzji i mediów.
- Pamiętaj, że różne źródła mogą przedstawiać ten sam news w różny sposób. Pokaż te różnice.
- Nie interpretuj przedstawionej wersji wydarzeń ani przedstawionych implikacji. Nie przyjmuj ich jako własnych.

## Zasady pracy
1. Wyszukaj przekrojowe materiały o tym newsie, poza źródłami startowymi. Sam dobierz liczbę i różnorodność źródeł tak, żeby razem dawały obiektywny obraz sytuacji. Nie korzystaj z X (Twittera).
2. Wyszukaj źródło pierwotne: changelog, RFC, repozytorium, dokumentację albo ogłoszenie producenta. Jeśli go nie znajdziesz, zapisz to jawnie.
3. Brak danych zapisz jawnie: „źródła nie podają”, „nie ogłoszono”. Nie zgaduj.
4. Podawaj konkretne liczby ze źródeł: wersje, daty, terminy, ceny, wyniki testów, skalę, z przypisaniem do źródła.
5. Podawaj status sprawy według źródeł (na przykład „zapowiedź, nie wydanie”, „beta, nie GA”, „RFC, nie standard”, „wyniki producenta, nie niezależny test”).
6. Wypowiedzi oficjalne cytuj dosłownie, w cudzysłowie, z nazwiskiem i funkcją osoby.

## Zapis opracowania

Popraw tytuł newsa tak, żeby był obiektywny i pozbawiony ocen. Zapisz opracowanie do pliku Markdown w katalogu opracowania. Nazwę pliku utwórz z poprawionego tytułu: małe litery, bez polskich znaków, słowa połączone myślnikami, rozszerzenie `.md`.

Nie przekazuj opracowania w odpowiedzi do wątku głównego. Użyj poniższej struktury wyłącznie wewnątrz pliku.

## Struktura pliku Markdown

### {Temat newsa}

**Twierdzenia źródeł** (każdy punkt z przypisaniem do źródła lub środowiska źródeł):
- **Kto:** {firmy, projekty, organizacje, osoby}
- **Co:** {co się stało; charakter i status sprawy}
- **Kiedy:** {data zdarzenia; harmonogram; terminy}
- **Dlaczego:** {przyczyny i uzasadnienia podawane przez strony}
- **Wersja i dostępność:** {numer wersji, platformy, regiony, cena albo licencja}
- **Skala / kluczowe szczegóły:** {liczby, wyniki, cytaty oficjalne}
- **Następne kroki:** {kolejne kroki według źródeł}
- **Tło:** {historia sprawy i powiązane wydarzenia według źródeł}

**Źródło pierwotne:** {URL i rodzaj: changelog, RFC, repozytorium, dokumentacja, ogłoszenie; albo „nie znaleziono”}

**Producent kontra niezależni:**
- **Twierdzenia producenta:** {...}
- **Twierdzenia niezależnych testów i recenzji:** {... albo „źródła nie podają”}

**Różne ujęcia w mediach:**
- {Źródło lub środowisko źródeł}: {jak przedstawia sprawę}

**Implikacje podawane przez źródła:**
- {Źródło lub środowisko źródeł}: {jakie implikacje wskazuje}

**Zgodność źródeł:**
- **Zgodne twierdzenia wielu niezależnych źródeł:** {...}
- **Twierdzenia jednego źródła lub jednego środowiska:** {...}
- **Twierdzenia sporne:** {kto twierdzi co}
- **Brak danych:** {czego źródła nie podają}

**Źródła:**
- {Medium} ({autor, jeśli znany}, {data}): {URL}

**Ograniczenia analizy:** {czego nie udało się ustalić i dlaczego}

Pisz opracowanie w języku polskim. Nazwy własne zostaw w oryginale. Nie dodawaj własnych opinii ani interpretacji.

## Odpowiedź do wątku głównego

Po zapisaniu pliku zwróć tylko blok YAML. Nie dodawaj treści opracowania, streszczenia ani komentarza.

```yaml
tytul: "{poprawiony, obiektywny tytuł newsa}"
plik: "{nazwa zapisanego pliku odpowiadająca tytułowi, z rozszerzeniem .md}"
```
