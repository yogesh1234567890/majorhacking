from django.urls import path, include

from django.contrib import admin

from hello import views
urlpatterns = [
    path("admin/", admin.site.urls),
    path("register/",views.registerPage,name="register"),
    path("login/",views.loginPage,name="login"),
    path("logout/",views.logoutUser,name="logout"),
    path('',include('hello.urls')),
]
