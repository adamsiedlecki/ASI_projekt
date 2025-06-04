FROM openjdk:slim

# Instaluj zależności systemowe
RUN apt-get update && apt-get install -y python3 && apt-get install -y pip && apt-get install -y \
    git build-essential curl 
    # && rm -rf /var/lib/apt/lists/*

# Ustaw katalog roboczy w kontenerze
WORKDIR /app

# Skopiuj tylko pliki zależności (dla lepszego cache)
COPY pyproject.toml requirements.txt* ./

# Zainstaluj Kedro i zależności
RUN pip install --upgrade pip \
    && pip install kedro

RUN pip install -r requirements.txt

# Skopiuj cały projekt
COPY . .

# Eksponuj port dla kedro viz
EXPOSE 4141

# Domyślny shell
 CMD ["/bin/bash"]

#CMD ["sh", "-c", "kedro run && /bin/bash"]

# && kedro viz
