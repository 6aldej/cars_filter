from django.contrib import admin
from django.urls import path
from car import views
from car.views import CarsView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.car_list),
    path('index/', CarsView.as_view(), name='main'),
]
