from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('login', views.login, name = 'login'),
    path('register', views.register, name = 'register'),
    path('logout', views.logout, name = 'logout'),
    path('details', views.details, name='details'),
    path('edit_user/<int:user_id>', views.edit_user, name = 'edit_user'),
    path('api/delete_user/<int:user_id>', views.delete_user, name = 'delete_user'),
]
