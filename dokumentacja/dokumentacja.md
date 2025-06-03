## Dokumentacja - przywidywanie cen pojazdów

Autorzy:
- Bartłomiej Małek
- Adam Siedlecki s25300

### Opis problemu

#### Krótki opis problemu i jego kontekstu (branża, otoczenie, etc.)

Branża samochodowa w Polsce ma się dobrze, co roku sprzedaje się setki tysięcy samochodów.
Każdy egzemplarz ma swoje cechy, które można wykorzystać w modelu predykcyjnym.
Taki model może być więc wartościowy dla dużej grupy osób.

#### Kto i w jaki sposób może skorzystać z tego modelu?

Wytworzony model może zostać użyty przez osoby chcące sprzedać bądź kupić pojazd,
aby zweryfikować czy jego cena jest rynkowa. Może zostać częścią portalu aukcyjnego,
lub stanowić odrębne narzędzie.

#### Dlaczego problem wydaje się dla Was interesujący?

Ponieważ ma realne zastosowanie i łatwo sobie zwizualizować potencjalnego użytkownika
- większość osób na jakimś etapie ma potrzebę kupna/ sprzedaży pojazdu.

### Dane

#### Źródła danych, ocena ich wiarygodności

Źródłem danych jest zbiór z Kaggle https://www.kaggle.com/datasets/aleksandrglotov/car-prices-poland.
Dane pochodzą z "dobrze znanego serwisu", pozyskane poprzez scraping czyli najpewniej otomoto bądź olx. 
Są wiarygodne, chociaż należy pamiętać, że to ceny ofertowe, a nie transakcyjne.

#### Krótka analiza opisowa danych

Dane zawierają następujące kolumny:
- mark - marka pojazdu
- model - model pojazdu
- generation_name - nazwa generacji
- year - rok produkcji
- mileage - przebieg w kilometrach
- vol_engine - pojemność silnika
- fuel - rodzaj paliwa
- city - nazwa miasta
- province - nazwa województwa

#### Uzasadnienie: w jaki sposób te dane mogą pomóc rozwiązać problem?

Dane takie jak marka, model, rodzaj silnika, rocznik i przebieg mają bezsprzeczny wpływ na cenę.
Dodatkowo wpływ może mieć też miejsce oferty, chociaż nierzadko ludzie pokonują wiele kilometrów
żeby zakupić dokładnie taki pojazd jaki chcą.

### Sposób rozwiązania problemu

Aby utworzyć model, został utworzony projekt w kedro.

#### Krótki opis wybranego modelu wraz z uzasadnieniem
#### Etapy realizacji projektu
#### Miary ewaluacji (oceny jakości) modelu

### Szczegółowy opis aplikacji
#### Wykorzystane narzędzia, struktura, odwołania do ważniejszych części kodu


### Podsumowanie

#### Co się udało?
#### Jakie były problemy? Jak je rozwiązaliśmy?
#### W jaki sposób może być to wykorzystane/rozwinięte w przyszłości?