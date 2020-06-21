from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='Dashboard'),
    path('<int:contact_id>/', views.detail, name='detail'),

]