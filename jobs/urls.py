from django.urls import path
from . import views


urlpatterns = [
    path('find_jobs/', views.find_jobs, name="find_jobs"),
    path('accept_job/<int:id>/', views.accept_job, name="accept_job"),
    path('profile/', views.profile, name="profile")
]
