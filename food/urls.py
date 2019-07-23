from django.urls import path
from food import views

urlpatterns = [
    path('carb/', views.calculatecarb, name='calccarb'),
    path('addfood/', views.addfood, name='addfooditem'),
]
