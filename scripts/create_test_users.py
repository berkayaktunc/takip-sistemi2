from db.models import CustomUser

# Admin kullanıcısını oluştur
if not CustomUser.objects.filter(username='admin').exists():
    admin_user = CustomUser.objects.create_superuser('admin', 'admin@example.com', 'admin')
    admin_user.save()
    print("Admin kullanıcı 'admin' başarıyla oluşturuldu.")
else:
    print("Admin kullanıcı zaten mevcut.")

# Normal kullanıcı (asd) oluştur
if not CustomUser.objects.filter(username='asd').exists():
    normal_user = CustomUser.objects.create_user('asd', 'randomemail@example.com', 'Asd1234.')
    normal_user.save()
    print("Normal kullanıcı 'asd' başarıyla oluşturuldu.")
else:
    print("Normal kullanıcı zaten mevcut.")
