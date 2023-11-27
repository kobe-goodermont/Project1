from django.urls import path
from . import views


urlpatterns = [
    # path function defines a url pattern
    # '' is empty to represent based path to app
    # views.index is the function defined in views.py
    # name='index' parameter is to dynamically create url
    # example in html <a href="{% url 'index' %}">Home</a>.
    path('', views.index, name='index'),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('register/', views.registerPage, name="register"),
    path('create/', views.CreatePage.as_view(), name="create"),
    path('create_workout', views.createWorkout, name="createWorkout"),
    path('update_workout/<str:pk>/', views.updateWorkout, name="updateWorkout"),
    path('delete_workout/<str:pk>/', views.deleteWorkout, name="deleteWorkout"),
]

