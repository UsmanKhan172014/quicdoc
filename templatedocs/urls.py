from django.urls import path
from . import views

urlpatterns = [
    path('upload_file/', views.upload_file, name='upload_file'),
    path('home/', views.index, name='index'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('update_doc_form/<int:id>', views.update_doc_form, name='updateDoc'),
    path('update/<int:id>', views.update, name='update'),
]
