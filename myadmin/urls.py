

from django.urls import path

from myadmin import views



urlpatterns = [
    path('dashboard/',views.dashboard,name='dashboard'),
    path('logins/',views.logins,name='logins'),
    path('masterpage/',views.masterpage,name='masterpage'),
    path('logout/',views.logout,name='logout'),
    path('user/',views.user,name='user'),
    path('category/',views.category,name='category'),
    path('setting/',views.setting,name='setting'),
    path('add_new/',views.add_new,name='add_new'),
    path('delte_category/<id>/',views.delte_category, name="delete_category"),
    path('update/<id>/',views.update, name="update")


    
   
]