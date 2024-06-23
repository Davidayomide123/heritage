from django.urls import path

from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('loginpage/', views.loginpage, name='loginpage'),
    path('register/', views.register, name='register'),
    path('dash/', views.dash, name='dash'),
    path('bank/', views.bank, name='bank'),
    path('crypto/', views.crypto, name='crypto'),
    path('gp/', views.gp, name='gp'),
    path('otp/', views.otp, name='otp'),
    path('payment/', views.payment, name='payment'),
    path('payoneer/', views.payoneer, name='payoneer'),
    path('paypal/', views.paypal, name='paypal'),
    path('pending/', views.pending, name='pending'),
    path('reset/', views.reset, name='reset'),
    path('setting/', views.setting, name='setting'),
    path('skrill/', views.skrill, name='skrill'),
    path('statistics/', views.statistics, name='statistics'),
    path('terms/', views.terms, name='terms'),
    path('tf/', views.tf, name='tf'),
    path('transaction/', views.transaction, name='transaction'),
    path('trust_wise/', views.trust_wise, name='trust_wise'),
    path('western_union/', views.western_union, name='western_union'),
    path('logout/', views.LogoutPage, name='logout'),
]
