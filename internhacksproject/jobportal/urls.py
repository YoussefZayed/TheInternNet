from django.urls import path

from jobportal import views


urlpatterns = [
    path('jobs/', views.jobs4you, name='jobs'),
    path('saved/', views.savedJobs, name='saved'),
    path('save/', views.savePosts, name='save')
]
