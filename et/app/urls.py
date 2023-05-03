from django.urls import path , include
from . import views
from django.views.generic import TemplateView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.login_page,name="login"),
    path('add/', views.add,name="add"),
    path('display/', views.display,name="display"),
    path('edit/', views.edit,name="edit"),
    path('homepage/', views.homepage,name="homepage"),
    path('month/', views.month_view,name="month"),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('news/',views.news,name="news"),
]