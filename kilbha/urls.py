from django.contrib import admin
from django.urls import path
from accounts import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/',views.LoginPage,name='login'),
    path('reg/',views.SignUpPage,name='signup'),
]
