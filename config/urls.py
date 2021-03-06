"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
import shop.views

# from rest_auth.views import (
#     LoginView, LogoutView, PasswordChangeView,
#     PasswordResetView, PasswordResetConfirmView
# )

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('cart/', include('cart.urls')),
    path('coupon/', include('coupon.urls')),
    path('order/', include('order.urls')),
    path('users/', include('users.urls')),
    path('search/', include('search.urls')),
    path('', include('shop.urls')),

    # path('login',shop.views.func2)
]
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('accounts/', include('allauth.urls')),
#     path('cart/', include('cart.urls')),
#     # path('coupon/', include('coupon.urls')),
#     # path('order/', include('order.urls')),
#     path('', include('shop.urls')),
# ]
