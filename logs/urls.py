from django.urls import path
from logs import views

urlpatterns = [
    path('', views.insulinform, name='logs'),
    path('display/', views.display, name='display'),
    path('detail/', views.detail, name='detail'),
]
