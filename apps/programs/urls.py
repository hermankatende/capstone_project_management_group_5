from django.urls import path
from . import views

urlpatterns = [
    path("", views.program_list, name="program_list"),
    path("add/", views.add_program, name="add_program"),
]
