from django.urls import path

from . import views

urlpatterns = [
    path('pens/add', views.edit_object, name="add_pen"),
    path('pens/edit/<int:obj_id>', views.edit_object, name="edit_object"),
    path('pens/delete/<int:obj_id>', views.delete_pen, name="delete_pen"),
    path('inks/add', views.edit_ink, name ="add_ink"),
    path('inks/edit/<int:ink_id>', views.edit_ink, name="edit_ink"),
    path('inks/delete/<int:ink_id>', views.delete_ink, name="delete_ink"),
    path('', views.index, name='index'),
]
