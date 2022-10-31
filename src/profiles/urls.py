from django.urls import path

from . import views

urlpatterns = [
    path("staff", views.staff_list, name="staff-list"),
    path("staff/<slug>", views.staff_full, name="staff-single"),
    path("phd", views.phd_list, name="phd-list"),
    path("phd/<slug>", views.phd_full, name="phd-single"),
]
