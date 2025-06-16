## Dokumentacja - przywidywanie cen pojazdów

Autorzy:
- Bartłomiej Małek
- Adam Siedlecki s25300

Linki: 
- GitHub https://github.com/adamsiedlecki/ASI_projekt
- Demo można zobaczyć tutaj: https://asi.cars.asiedlecki.net/
(wdrożone na własnym serwerze, który jest czasami restartowany więc może się zdarzyć że jest niedostępne)

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
Co więcej, pochodzą z 2022 roku, więc minęło już trochę czasu i realia rynkowe się zmieniły.
Aby taki model był użyteczny, musiałby być trenowany na bieżąco nowymi danymi.

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

Został zrobiony preprocessing, w wyniku którego zostały usunięte niektóre kolumny, nazwa
modelu pojazdu została znormalizowana do lowercase, zostały utworzone nowe zmienne, takie jak wiek
oraz średnioroczny przebieg. Została podjęta też próba usunięcia outlierów, choć nie miała zbyt dużego wpływu.

Do uczenia został wykorzystany pycaret. Wyprodukowany przez niego model został uruchomiony w aplikacji
napisanej przy użyciu streamlita. Aplikacja podaje nie tylko przewidzianą wartość ceny, ale 
także przedział 0.95 * cena - 1.05 * cena.

#### Krótki opis wybranego modelu wraz z uzasadnieniem

TODO

#### Etapy realizacji projektu

1. Utworzenie projektu w kedro
2. Preprocessing, utworzenie dodatkowych zmiennych
3. Próba wpasowania autogluona w kedro.
4. Próba wpasowania pycaret w kedro.
5. Dobór odpowiednich algorytmów w pycaret (niektóre powodowały bardzo długi czas uczenia i ciężkie modele - danych jest sporo)
6. Zapis modelu w strukturze kedro
7. Utworzenie aplikacji w streamlit i uruchomienie w jej ramach modelu
8. Poprawki wyglądu aplikacji końcowej, prezentowanie przedziału cen, opcje do wyboru
9. Wdrożenie aplikacji na własny serwer, z wykorzystaniem konfiguracji docker, ssl proxy, nadanie subdomeny https://asi.cars.asiedlecki.net/

#### Miary ewaluacji (oceny jakości) modelu

TODO

### Szczegółowy opis aplikacji
#### Wykorzystane narzędzia, struktura, odwołania do ważniejszych części kodu

TODO

### Podsumowanie

#### Co się udało?

Udało się z powodzeniem wykorzystać narzędzia poruszane i wspomniane na zajęciach,
takie jak kedro (pipeline, wizualizacja) pycaret (uczenie modelu), streamlit (integrowanie modelu w aplikację webową).

Ponadto wytworzony model został wdrożony na serwer i jest widoczny publicznie z internetu.

#### Jakie były problemy? Jak je rozwiązaliśmy?

1. Dane nie są aktualne. Aby uzyskiwać lepsze wyniki, należałoby regularne scrapować dane z internetu i trenować
model na najbardziej aktualnych danych. Jeszcze lepszym pomysłem byłoby pozyskanie danych transakcyjnych, ale to wymagałoby
integracji z jednostkami rządowymi (może Urząd Skarbowy?). Ta kwestia została rozwiązana poprzez pogodzenie się z jakością danych jakie mamy.
2. Autogluon posiada zależności które utrudniają integrację z kedro.
Straciłem dużo czasu na próbie ich pogodzenia (wolny internet miał w tym swój udział). Problem został rozwiązany
poprzez zastosowanie pycareta.
3. Pycaret domyślnie próbuje uczyć wieloma algorytmami, co jest niewydajne dla dużego datasetu. Została ograniczona 
lista używanych algorytmów, co przyspieszyło proces.
4. Problem z zapisem modelu zgodnie z 'flow' kedro. Przekazanie z węzła treningowego kedro 'return best_model' nie jest tożsame
z ręcznym zapisaniem 'save_model(best_model, 'data/06_models/best_model_with_pipeline')'. W przypadku ręcznego zapisania, zapisuje się pipeline,
który jest potrzebny do uruchomienia modelu. Rozwiązaniem jest ręczne wołanie save_model.
5. Problem z uruchomieniem aplikacji ze stramlitem w środowisku 'paraprodukcyjnym' - stosowanie oprogramowania ssl proxy
powodowało pierwotnie problem, ponieważ funkcjonalność websocketów była w nim domyślnie wyłączona. Okazało się,
że streamlit ją wykorzystuje i trzeba było ją włączyć.

#### W jaki sposób może być to wykorzystane/rozwinięte w przyszłości?

Aplikację można rozwinąć, stosując zautomatyzowany system dostarczania danych, który mógłby działać w następujący sposób:
- scraper zbiera nowe dane i dodaje do datasetu
- stare dane są usuwane z datasetu
- model jest uczony (np. codziennie, albo co 10k nowych rekordów)
- po uczeniu jakiś mechanizm, np Jenkins wrzuca nowy model do odpowiedniego katalogu, przebudowuje kontener z aplikacją streamlit, uruchamia ją ponownie