# Base image olarak Python 3.9 kullanıyoruz
FROM python:3.9-slim

# Çalışma dizini oluşturuluyor
WORKDIR /app

# Gereksinim dosyasını kopyalayın
COPY requirements.txt /app/

# Gereksinimleri yükleyin
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Uygulamanın kaynak dosyalarını kopyalayın
COPY . /app/

# Django ortamını ayarlayın
ENV PYTHONUNBUFFERED 1

# Django'nun çalışabilmesi için gerekli portu açın
EXPOSE 8000

# Django uygulamasını başlatmak için komut
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
