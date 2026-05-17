from django.shortcuts import render

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from .forms import RegisterForm, LoginForm, NewsForm
from .models import News


def main_page(request):
    # Получаем все новости
    all_news = News.objects.all()

    # 6 новостей на страницу
    paginator = Paginator(all_news, 6)
    page_number = request.GET.get('page', 1)
    news_list = paginator.get_page(page_number)

    return render(request, 'newsapp/main_page.html', {'news_list': news_list})


def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('main_page')
    else:
        form = RegisterForm()
    return render(request, 'newsapp/auth.html', {'form': form, 'mode': 'register'})


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('main_page')
    else:
        form = LoginForm()
    return render(request, 'newsapp/auth.html', {'form': form, 'mode': 'login'})


def logout_view(request):
    logout(request)
    return redirect('main_page')


@login_required
def add_news(request):
    if request.method == 'POST':
        form = NewsForm(request.POST, request.FILES)
        if form.is_valid():
            news = form.save(commit=False)
            news.author = request.user
            news.save()
            return redirect('main_page')
    else:
        form = NewsForm()
    return render(request, 'newsapp/add_edit_news.html', {'form': form, 'title': 'Добавить новость'})


@login_required
def edit_news(request, news_id):
    news = get_object_or_404(News, id=news_id)
    if news.author != request.user:
        return redirect('main_page')

    if request.method == 'POST':
        form = NewsForm(request.POST, request.FILES, instance=news)
        if form.is_valid():
            form.save()
            return redirect('main_page')
    else:
        form = NewsForm(instance=news)
    return render(request, 'newsapp/add_edit_news.html', {'form': form, 'title': 'Редактировать новость'})


@login_required
def delete_news(request, news_id):
    news = get_object_or_404(News, id=news_id)
    if news.author == request.user:
        news.delete()
    return redirect('main_page')