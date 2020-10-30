from django.urls import path, re_path

from . import views

urlpatterns = [
    path('submission/', views.create),
    path('submissions/', views.all),
    re_path(r'^', views.FrontendAppView.as_view()), 
]
