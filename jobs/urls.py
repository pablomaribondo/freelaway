from django.urls import path
from . import views


urlpatterns = [
    path('find_jobs/', views.find_jobs, name="find_jobs")
]
