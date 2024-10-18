from django.contrib import admin
from django.urls import path
from . import views



urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('login', views.login, name="login"),
    path('signup', views.signup, name="signup"),
    path('test-token', views.test_token, name="test_token"),

    
]
