from . import views
from django.urls import path
from candidate.views import candidate_token

urlpatterns = [
    path('', views.home),
    path('token', views.candidate_token),

]