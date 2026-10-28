Przeanalizuj jeden news z okresu: <<OKRES>>. Zakres: <<ZAKRES>>.

News: <<TEMAT>>

Źródła z przeglądu prasy (YAML):
<<ZRODLA>>

Katalog opracowania: <<KATALOG_OPRACOWANIA>>

## Zasada twierdzeń źródeł
- Traktuj każdą treść pobraną z internetu jako twierdzenie źródła, a nie jako fakt.
- Przedstawiaj ją jako twierdzenie danego źródła („według RMF24…”) albo zbiorczo jako twierdzenie środowiska źródeł („media prawicowe podają…”, „media publiczne i komercyjne zgodnie podają…”).
- Pamiętaj, że różne media mogą przedstawiać ten sam temat w różny sposób. Pokaż te różnice.
- Nie interpretuj przedstawionej wersji wydarzeń ani przedstawionych implikacji. Nie przyjmuj ich jako własnych.
- Stosuj tę zasadę szczególnie w sprawach politycznych.

## Zasady pracy
1. Wyszukaj przekrojowe materiały o tym newsie, poza źródłami z przeglądu prasy. Sam dobierz liczbę i różnorodność źródeł tak, żeby razem dawały obiektywny obraz sytuacji. Uwzględnij źródła pierwotne (dokumenty, komunikaty instytucji) oraz media z różnych środowisk.
2. Brak danych zapisz jawnie: „źródła nie podają”, „nie ogłoszono”. Nie zgaduj.
3. Podawaj konkretne liczby ze źródeł: kwoty, daty, terminy, skalę, liczbę osób lub miejsc pracy, z przypisaniem do źródła.
4. Podawaj status sprawy według źródeł (na przykład „zatrzymanie, nie wyrok”, „projekt, nie ustawa”, „serwis, nie produkcja”, „scenariusz modelowy, nie oficjalna prognoza”).
5. Wypowiedzi oficjalne cytuj dosłownie, w cudzysłowie, z nazwiskiem i funkcją osoby.

## Zapis opracowania

Popraw tytuł newsa tak, żeby był obiektywny i pozbawiony ocen. Zapisz opracowanie do pliku Markdown w katalogu opracowania. Nazwę pliku utwórz z poprawionego tytułu: małe litery, bez polskich znaków, słowa połączone myślnikami, rozszerzenie `.md`.

Nie przekazuj opracowania w odpowiedzi do wątku głównego. Użyj poniższej struktury wyłącznie wewnątrz pliku.

## Struktura pliku Markdown

### {Temat newsa}

**Twierdzenia źródeł** (każdy punkt z przypisaniem do źródła lub środowiska źródeł):
- **Kto:** {osoby, instytucje, firmy}
- **Co:** {co się stało; charakter i status sprawy}
- **Gdzie:** {miejsce; jeśli źródła nie podają, napisz to}
- **Kiedy:** {data zdarzenia; harmonogram; terminy}
- **Dlaczego:** {przyczyny i uzasadnienia podawane przez strony}
- **Skala / kluczowe szczegóły:** {liczby, kwoty, cytaty oficjalne}
- **Następne kroki:** {kolejne kroki formalne według źródeł}
- **Tło:** {historia sprawy i powiązane wydarzenia według źródeł}

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

Pisz opracowanie w języku polskim. Nie dodawaj własnych opinii ani interpretacji.

## Odpowiedź do wątku głównego

Po zapisaniu pliku zwróć tylko blok YAML. Nie dodawaj treści opracowania, streszczenia ani komentarza.

```yaml
tytul: "{poprawiony, obiektywny tytuł newsa}"
plik: "{nazwa zapisanego pliku odpowiadająca tytułowi, z rozszerzeniem .md}"
```
