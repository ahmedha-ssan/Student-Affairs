from django import views
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home', views.home, name='home'),
    path('add', views.add, name='add'),
    path('login', views.login, name='login'),
    path('edit', views.edit, name='edit'),
    path('search', views.search, name='search'),
    path('search_edit', views.search_edit, name='search_edit'),
    path('view', views.view, name='view'),
    path('department', views.department, name='department'),
    path('create', views.create, name='create'),
    path('search_data', views.search_data, name='search_data'),
    path('update/<str:id>', views.update, name='update'),
    path('delete/<str:id>', views.delete, name='delete')
    # path('update', views.update, name='update'),
]
