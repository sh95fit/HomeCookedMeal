from django.urls import path

from .views import views

urlpatterns = [
    path('', views.index),  # 루트 디렉토리
]
