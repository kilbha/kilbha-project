from django.contrib import admin
from django.urls import path
from accounts import views
from feedarea import views as fviews
urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/',views.LoginPage,name='login'),
    path('reg/',views.SignUpPage,name='signup'),
    path('',fviews.HomePage,name='home'),
    path('logout/',views.LogOutPage,name='logout'),
    path('yes/<int:prk>',fviews.YesCounter,name='yc'),
    path('no/<int:prk>',fviews.NoCounter,name='nc'),
]
