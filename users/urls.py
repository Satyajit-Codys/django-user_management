from django.urls import path
from django.conf.urls import include, url
from . import views

urlpatterns = [
    # path("register", views.register_request, name="register"),
    # path("login", views.login_request, name="login"),
    # path("logout", views.logout_request, name= "logout"),
    path("", views.dashboard, name="dashboard"),
    # path("users/dashboard.html", views.dashboard, name="dashboard"),
    url(r"^dashboard/", views.dashboard, name="dashboard"),
    url(r"^login/", views.login_request, name="login"),
    url(r"^logout/", views.logout_request, name="logout"),
    url(r"^register/", views.register_request, name="register"),
]