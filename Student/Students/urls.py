from django.urls import path
from . import views
urlpatterns = [
    path('',views.home),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
    path('profile/<int:pk>/',views.profile,name='profile'),
    path('Acedemic/<int:pk>/',views.Acedemic,name='Acedemic'),
    path('createstudent/<int:pk>/',views.createstudent,name='createstudent'),
    path('addcourses/<int:pk>/',views.addcourses,name='addcourses'),
    path('go_back/<int:pk>', views.go_back, name='go_back'),
     path('students/', views.students, name='students') 
    #'' will point out to the home page.
]