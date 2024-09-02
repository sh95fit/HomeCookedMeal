from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.login, name='login'),  # 루트 디렉토리
    path('accounts/', include('allauth.urls'))
]
