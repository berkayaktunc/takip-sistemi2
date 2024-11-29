# Takip Sistemi 2

## Proje Hakkında

**Takip Sistemi 2** bir [açıklama burada olacak - projenin amacı ve genel işlevselliği] olarak kullanılan bir uygulamadır. Bu sistem, kullanıcıların izin talepleri oluşturmasına, yöneticilerin talepleri onaylamasına ve çeşitli kullanıcıların performanslarını izlemelerine olanak tanır.

- **Teknolojiler**: Django, WebSockets, PostgreSQL, Redis
- **Özellikler**:
  - Kullanıcı kayıt ve giriş sistemi
  - İzin talepleri yönetimi
  - Bildirim sistemleri
  - Yöneticiler için dashboard ve yönetim araçları
  - WebSocket tabanlı gerçek zamanlı bildirimler

## Özellikler

- **Kullanıcı Yönetimi**: Admin ve normal kullanıcı yönetimi.
- **İzin Talepleri**: Kullanıcılar izin talepleri oluşturabilir, yöneticiler bu talepleri onaylayabilir.
- **Bildirim Sistemi**: Gerçek zamanlı bildirimler için WebSocket kullanımı.
- **Veritabanı**: PostgreSQL veritabanı kullanarak veri yönetimi.

## Kurulum

Projenin çalışabilmesi için aşağıdaki adımları takip edebilirsiniz.

### Gereksinimler

Proje aşağıdaki teknolojileri kullanır:

- Python 3.x
- PostgreSQL
- Redis
- Docker (isteğe bağlı)

### Adım 1: Veritabanı Kurulumu

Veritabanını oluşturmak için aşağıdaki SQL komutlarını çalıştırmanız gerekecek. Bu adımı yalnızca PostgreSQL veritabanınız yoksa yapmanız gerekmektedir:

```sql
CREATE DATABASE attendance_db;
CREATE USER attendance_user WITH PASSWORD 'your_password';
GRANT ALL PRIVILEGES ON DATABASE attendance_db TO attendance_user;
```

### Adım 2: Ortam Değişkenlerini Ayarlayın

Aşağıdaki ortam değişkenlerini ayarlamanız gerekebilir:

- **DATABASE_URL** - Veritabanı bağlantı URL'si
- **SECRET_KEY** - Django için güvenlik anahtarı

### Adım 3: Bağımlılıkları Yükleyin

Python bağımlılıklarını yüklemek için şu komutu çalıştırın:

```bash
pip install -r requirements.txt
```

### Adım 4: Veritabanı Migrasyonlarını Çalıştırın

Django veritabanı migrasyonlarını çalıştırarak gerekli veritabanı tablolarını oluşturun:

```bash
python manage.py makemigrations
python manage.py migrate
```

### Adım 5: WebSocket Desteğini Aktifleştirme (Opsiyonel)

Eğer WebSocket üzerinden bildirim almayı istiyorsanız, Redis ve Channels ayarlarını doğru şekilde yapılandırdığınızdan emin olun. WebSocket kullanımı için ek ayarlamalar yapılması gerekebilir.

### Adım 6: Test Veritabanı Kullanıcıları Oluşturun

Test kullanıcılarını oluşturmak için aşağıdaki komutu çalıştırabilirsiniz:

```bash
python manage.py runscript create_test_users
```

Bu komut, **admin** ve **asd** adlı test kullanıcılarını oluşturur.

### Adım 7: Sunucu Çalıştırma

Django geliştirme sunucusunu başlatmak için aşağıdaki komutu kullanabilirsiniz:

```bash
python manage.py runserver
```

### Docker ile Çalıştırma

Projeyi Docker kullanarak çalıştırmak için aşağıdaki komutu çalıştırabilirsiniz:

```bash
docker-compose up --build
```

Bu komut, uygulamanızı Docker container'ları içinde çalıştırır.

## Swagger API Belgelendirmesi

Projenin API'lerini test etmek için Swagger UI entegrasyonu yapılmıştır. Aşağıdaki adımlarla Swagger UI'ye erişebilirsiniz:

### Swagger UI'ye Erişim

Swagger UI'ye şu [URL](http://localhost:8000/swagger/) üzerinden erişebilirsiniz:
