from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('add/', views.add_news, name='add_news'),
    path('edit/<int:news_id>/', views.edit_news, name='edit_news'),
    path('delete/<int:news_id>/', views.delete_news, name='delete_news'),
]