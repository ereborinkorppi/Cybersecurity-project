from django.urls import path

from . import views

app_name = 'diary'
urlpatterns = [
    path('', views.index, name='index'),
    path('add', views.addEntryView, name='add'),
    path('search', views.searchEntryView, name='search'),
    path('<int:entry_id>/', views.detail, name='detail'),
]