from django.contrib import admin
from django.urls import path
from Library import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.Home , name= "Home_Page"),
    path('main_page',views.Register , name= "main_page"),
    path('SignIn',views.SignIn , name= "SignIn_Page"),
    path('Add_Books',views.add , name= "Add_Books"),
    path('Study',views.Study , name= "Home"),
    path('View_Books',views.View_books , name= "view_books"),
    path('Manage_Users',views.manage_users , name= "Manage_users"),
    path('Manage_books',views.manage_books , name= "Manage_Books"),
]