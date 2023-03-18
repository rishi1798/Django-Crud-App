from django.urls import path
from . import views


urlpatterns = [
    path('',views.home,name="home"),
    path('delete/<int:id>',views.delete_user,name="delete-user"),
    path('update/<int:id>',views.update_user,name="update-user"),
]
