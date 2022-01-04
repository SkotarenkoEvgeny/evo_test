from django.urls import path

from . import views

urlpatterns = [
    path('', views.home_page_view, name='home'),
    path('names_list/', views.NamesListView.as_view(), name='name_list'),
    ]
