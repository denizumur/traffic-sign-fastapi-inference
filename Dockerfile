# Python tabanlı bir imajdan başla
FROM python:3.10-slim

# Çalışma dizinini oluştur
WORKDIR /app

# Bağımlılıkları kopyala ve yükle
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Uygulama dosyalarını kopyala
COPY app ./app

# Servisi başlat
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "7001"]
