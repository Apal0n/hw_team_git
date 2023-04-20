from django.urls import path
from . import views


urlpatterns = [
    path('', views.main_page, name='main'),
    path('courier/', views.show_couriers, name='courier')
]
