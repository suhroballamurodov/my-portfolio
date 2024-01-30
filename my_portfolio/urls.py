from django.urls import path, include
from .views import *
from . import views
from rest_framework import routers



router = routers.DefaultRouter()
router.register(r'posts', PostViewSet)


urlpatterns = [
    # path("register", views.register_request, name="register"),
    path('', main, name='main'),
    path('portfolio_details/', portfolio_details, name='portfolio_details'),
    # path('forms/contact/', views.contact, name='contact'),
    path('contact/', views.contact, name='contact'),
    path('contact/success/', views.contact_success, name='contact_success'),
    path('telegram_bot/', views.telegram, name='telegram_bot'),
    path('web/', views.web, name='web'),
    path('motions', views.motions, name='motions'),
    # path('posts', views.get), #API uchun 
    path('api/', include(router.urls)),  #API uchun link
    # path('forms', contact, name = 'forms'),
] 