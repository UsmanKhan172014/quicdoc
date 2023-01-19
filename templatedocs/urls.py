from django.urls import path
from . import views

urlpatterns = [
    path('upload_file/', views.home, name='upload_file'),
    path('get_all/', views.get_all, name='get_all'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('updateDoc/<int:id>', views.updateDoc, name='updateDoc'),
    path('update/<int:id>', views.update, name='update'),
    path('load_admin/', views.load_admin, name='load_admin'),
]
