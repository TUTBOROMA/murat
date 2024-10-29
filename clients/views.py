from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.db.models import Count
from .models import Service, Campaign  # Убедитесь, что Campaign определён в models.py
from .forms import ServiceForm
from django.shortcuts import render
from django.shortcuts import redirect
def home_view(request):
    return redirect('shop_view')  # Перенаправление на shop_view
def shop_view(request):
    # Здесь вы можете добавить логику для отображения товаров в магазине
    return render(request, 'clients/shop.html')  # Убедитесь, что у вас есть этот шаблон

# Отображает детальную информацию о сервисе
def service_detail(request, pk):
    service = get_object_or_404(Service, pk=pk)
    return render(request, 'clients/service_detail.html', {'service': service})

# Редактирует выбранный сервис
def service_edit(request, pk):
    service = get_object_or_404(Service, pk=pk)
    if request.method == 'POST':
        form = ServiceForm(request.POST, instance=service)
        if form.is_valid():
            form.save()
            return redirect('service_detail', pk=service.pk)
    else:
        form = ServiceForm(instance=service)
    return render(request, 'clients/service_edit.html', {'form': form})

# Отображает список всех сервисов
def service_list(request):
    services = Service.objects.all()
    return render(request, 'clients/service_list.html', {'services': services})

def service_create(request):
    if request.method == 'POST':
        form = ServiceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('service_list')  # Перенаправление на список услуг
    else:
        form = ServiceForm()
    return render(request, 'clients/service_form.html', {'form': form})

# Регистрация нового пользователя
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('service_list')
    else:
        form = UserCreationForm()
    return render(request, 'clients/register.html', {'form': form})

# Статистика по кампаниям
def campaign_statistics(request):
    statistics = Campaign.objects.annotate(
        num_clients=Count('potentialclient')
    ).values('name', 'num_clients')
    return render(request, 'clients/campaign_statistics.html', {'statistics': statistics})
