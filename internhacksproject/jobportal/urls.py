from django.urls import path

from jobportal import views


urlpatterns = [
    path('', views.jobs4you, name='jobs')
]
