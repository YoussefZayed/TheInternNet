from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='Dashboard'),
    path('viewTemp/<int:email_id>/', views.viewEmailTemp, name='viewEmailTemp'),
    path('createEmail/<int:email_id>/', views.usetemp, name='usetemp'),
    path('createdEmail/<int:email_id>/', views.usedtemp, name='usedtemp'),
    path('<int:contact_id>/', views.detail, name='detail'),

]