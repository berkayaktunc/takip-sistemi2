from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login as auth_login
from db.models import LeaveRequest
from django.contrib import messages
from django.http import HttpResponseForbidden
from .forms import SignupForm, LeaveRequestForm

def logout_view(request):
    logout(request)
    return redirect('core:login')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            auth_login(request, user)
            return redirect('core:home')
        else:
            messages.error(request, 'Kullanici adi veya şifre hatali!')
    
    return render(request, 'core/login.html')  # template yolunu düzelttik


@login_required(login_url='/login')
def home(request):
    if request.user.is_authenticated:
        if request.user.is_staff:
            return redirect('core:admin_dashboard')
        else:
            return render(request, 'core/home.html')
    return redirect('core:login')


def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            messages.success(request, 'Kayıt başarılı!')
            return redirect('core:home')
        else:
            messages.error(request, 'Lütfen formu doğru doldurunuz!')
    else:
        form = SignupForm()
    
    return render(request, 'core/signup.html', {'form': form})

def admin_dashboard(request):
    if request.user.is_authenticated and request.user.is_staff:
        return render(request, 'core/admin_dashboard.html')  # Admin için özel sayfa
    return redirect('core:home')  # Yetkili değilse home page'e yönlendirme


def admin_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None and user.is_staff:  # Sadece yetkili kullanıcıları kabul et
            auth_login(request, user)
            return redirect('core:admin_dashboard')
        else:
            messages.error(request, 'Yetkili girişi başarısız!')
    
    return render(request, 'core/admin_login.html')

def admin_logout(request):
    logout(request)
    return redirect('core:admin_login')

@login_required
def leave_requests(request):
    if request.user.is_staff:
        requests = LeaveRequest.objects.all()
        return render(request, 'core/leave_requests.html', {'requests': requests})
    return redirect('core:home')

@login_required
def create_leave_request(request):
    if request.method == 'POST':
        # Formu al
        form = LeaveRequestForm(request.POST)
        
        if form.is_valid():
            # Form geçerliyse, yeni izin talebi oluştur
            leave_request = form.save(commit=False)
            leave_request.user = request.user  # Kullanıcıyı izin talebine bağla
            leave_request.status = 'Pending'
            leave_request.save()  # Veritabanına kaydet

            # Kullanıcıya başarılı mesajı göster
            messages.success(request, 'İzin talebiniz başarıyla gönderildi.')

            # Ana sayfaya veya ilgili bir sayfaya yönlendir
            return redirect('core:home')
        else:
            # Form hatalıysa, hata mesajı göster
            messages.error(request, 'Formda hata var. Lütfen tekrar deneyin.')

    else:
        # GET isteği ise, formu boş bir şekilde göster
        form = LeaveRequestForm()

    return render(request, 'core/create_leave_request.html', {'form': form})


@login_required
def izin_talepleri(request):
    # Admin olup olmadığını kontrol et
    if not request.user.is_staff:
        return HttpResponseForbidden("Bu sayfayı görüntüleme yetkiniz yok.")  # Admin değilse, erişim yasak

    # Admin için tüm izin taleplerini al
    leave_requests = LeaveRequest.objects.all()

    if request.method == 'POST':
        # POST isteği ile gelen izin talebi güncellemeleri
        request_id = request.POST.get('request_id')
        new_status = request.POST.get('status')

        if request_id and new_status:
            try:
                leave_request = LeaveRequest.objects.get(id=request_id)
                leave_request.status = new_status
                leave_request.save()  # Yeni statusu kaydet
            except LeaveRequest.DoesNotExist:
                pass  # İzin talebi bulunamazsa bir şefrom django.shortcuts import render, redirect, get_object_or_404y yapma

        return redirect('core:izin_talepleri')  # Güncelleme sonrası aynı sayfaya geri yönlendir

    # İzin taleplerini ve mevcut durumu admin sayfasına gönder
    return render(request, 'core/izin_talepleri.html', {'leave_requests': leave_requests})

@login_required
def update_status(request, request_id, new_status):
    # LeaveRequest modelinden ilgili izni al
    leave_request = get_object_or_404(LeaveRequest, id=request_id)
    
    # Yalnızca adminlerin durumu değiştirmesine izin ver
    if request.user.is_staff:
        # Durumun yeni değeri geçerli seçeneklerden biri olmalı
        if new_status in ['approved', 'rejected', 'pending']:
            leave_request.status = new_status
            leave_request.save()  # Değişiklikleri kaydet
    return redirect('core:izin_talepleri')  # Yeniden izin talepleri sayfasına dön