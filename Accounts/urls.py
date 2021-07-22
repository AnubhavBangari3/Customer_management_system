from django.urls import path
from .views import *

from django.contrib.auth import views as auth_views

urlpatterns=[
    path('register/',registerPage,name="register"),
    path('',login_view,name="login"),
    path('logout/',logout_view,name="logout"),
    path('home/',home,name="home"),
    path("about",about,name="about"),
    path("product",product,name="product"),
    path("customer/<str:pk>",customer,name="customer"),
    path('create_order/<str:pk>',createOrder,name="create_order"),
    path('update_order/<str:pk>',updateOrder,name="update_order"),
    
    path('delete_order/<str:pk>',deleterOrder,name="delete_order"),
    path('password_reset/',auth_views.PasswordResetView.as_view(),name="password_reset"),
    
    path('password_reset_done/',auth_views.PasswordResetDoneView.as_view(),name="password_reset_done"),
    
    path('reset/<uidb64>/<token>',auth_views.PasswordResetConfirmView.as_view(),name="password_reset_confirm"),
    
    path('password_reset_complete/',auth_views.PasswordResetCompleteView.as_view(),name="password_reset_complete"),
    
    
    
    ]