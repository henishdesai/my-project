"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from atexit import register
from django.contrib import admin # type: ignore
from django.urls import include, path  # type: ignore
#from myapp import views
#from foodapp import views
#from henishapp import views
from django.conf import settings
from django.conf.urls.static import static 
#from django.conf.urls import url 
from django.contrib.staticfiles.urls import staticfiles_urlpatterns 




urlpatterns = [
    path('admin/', admin.site.urls),
    # path('food/', views.food,name="food"),
    # path('demo1/',views.demo1,name="demo1"),
    # path('demo/',views.demo,name="demo"),
    # path('contect_page/',views.contect_page,name="contect_page"),
    # path('food/delete/<int:recipe_id>',views.delete_recipe,name="delete_recipe"),
    # path('food/update_recipe/<int:id>/', views.update_recipe, name='update_recipe'),
    # path('login/',views.login,name="login"),
   # path('register/',views.register,name="register"),
    #path('home/',views.home,name="home"),
   # path('about/',views.about,name="about"),
   # path('contact/',views.contact,name="contact"),
   # path('login1/', views.login, name='login'),
   # path('register1/',views.register,name="register"),


    # path('W_home/', views.W_home, name="W_home"),
    # path('W_about/', views.W_about, name="W_about"),
    # path('W_shop/', views.W_shop, name="W_shop"),
    # path('W_contact/', views.W_contact, name="W_contact"),
    # path('login/', views.login, name='login'),
    # path('sign_up/',views.sign_up,name="sign_up"),

    path('myadmin/',include("myadmin.urls")),
 

    


   
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)









