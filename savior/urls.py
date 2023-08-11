from django.urls import path, include
from . import views

app_name='savior'

urlpatterns = [
    path('', views.main , name='main'),
    path('pricelist/', views.pricelist , name='pricelist'),

    #일본
    path('japan/', views.japan , name='japan'),
    path('japan_exchange/', views.japan_exchange , name='japan_exchange'),
    path('japan_pricelist/', views.japan_pricelist , name='japan_pricelist'),
    path('japan_clothes/', views.japan_clothes , name='japan_clothes'),
    path('japan_foods/', views.japan_foods , name='japan_foods'),
    path('japan_others/', views.japan_others , name='japan_others'),
    #미국
    path('USA/', views.USA , name='USA'),
    path('USA_exchange/', views.USA_exchange , name='USA_exchange'),
    path('USA_pricelist/', views.USA_pricelist , name='USA_pricelist'),
    path('USA_clothes/', views.usa_clothes , name='USA_clothes'),
    path('USA_foods/', views.usa_foods , name='USA_foods'),
    path('USA_others/', views.usa_others , name='USA_others'),
    #베트남
    path('vietnam/', views.vietnam , name='vietnam'),
    path('vietnam_exchange/', views.vietnam_exchange , name='vietnam_exchange'),
    path('vietnam_pricelist/', views.vietnam_pricelist , name='vietnam_pricelist'),
    path('vietnam_clothes/', views.vietnam_clothes , name='vietnam_clothes'),
    path('vietnam_foods/', views.vietnam_foods , name='vietnam_foods'),
    path('vietnam_others/', views.vietnam_others , name='vietnam_others'),
    
    #* 로그인 및 회원가입
    path('accounts/', include('accounts.urls', namespace='accounts' )),

    #* 마이페이지 
    path('mypage/', views.mypage, name='mypage'),
]