from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('allauth.urls')), # 꼭 밑에 넣어야 함.
    path('boards/', include('boards.urls')),
    path('admin/', admin.site.urls),
]
