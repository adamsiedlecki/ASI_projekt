Źródło danych: https://www.kaggle.com/datasets/aleksandrglotov/car-prices-poland/data

## Część kedro

Zbudowanie kontenera z kedro (ze względu na zależności długotrwałe, u mnie za pierwyszym razem prawie 1h, potem cache dockera skraca czas): 
```cmd
docker build . -t kedro
```

Uruchomienie kontnera z kedro na windows (${PWD} powinno działać w powershellu)
```cmd
docker run -p 4141:4141 -it -v ${PWD}\:/app/ kedro
```

Po uruchomieniu otwiera się konsola, można zrobić kedro run && kedro viz, czyli po pełnym przebiegu powinniśmy móc zobaczyć pipeline
pod adresem http://localhost:4141

Po kedro run w data/06_models powinien pojawić się plik best_model_with_pipeline.pkl
Należy go umieścić w folderze app

## Część aplikacyjna

Zbudowanie obrazu
```cmd
docker build . -t asi-app
```

uruchomienie
```cmd
docker run -p 8501:8501 asi-app
```

Aplikacja powinna być widoczna w: http://localhost:8501/