FROM python:3.9.2

WORKDIR /app

COPY requirements.txt .

RUN  pip install --upgrade pip && pip install -r requirements.txt

COPY . .

EXPOSE 8501

CMD ["sh", "-c", "streamlit run app.py"]