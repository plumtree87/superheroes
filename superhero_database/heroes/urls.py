from . import views
from django.urls import path

app_name = 'heroes'
urlpatterns = [
  path('', views.index, name='index'),
  path('<int:hero_id>/', views.detail, name='detail'),
  path('create', views.create, name='create_new_hero'),
  path('edit/<int:hero_id>', views.edit, name='edit'),
  path('delete/<int:hero_id>', views.delete, name='delete')
]
