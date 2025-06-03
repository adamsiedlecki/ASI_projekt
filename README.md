Źródło danych: https://www.kaggle.com/datasets/aleksandrglotov/car-prices-poland/data

Zbudowanie kontenera z kedro (ze względu na zależności długotrwałe, u mnie za pierwyszym razem prawie 1h, potem cache dockera skraca czas): 
```cmd
docker build . -t asi
```

Uruchomienie kontnera z kedro na windows (${PWD} powinno działać w powershellu)
```cmd
docker run -p 4141 -v ${PWD}\kedro-asi-cars\data:/app/data asi
```

Po uruchomieniu rozpoczyna się kedro run && kedro viz, czyli po pełnym przebiegu powinniśmy móc zobaczyć pipeline
pod adresem http://localhost:4141