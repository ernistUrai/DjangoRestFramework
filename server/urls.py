from django.contrib import admin
from django.urls import path, include
from . import views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('user.urls')),  # myapp URL'дерин кошуу

    path('login', views.login, name="login"),
    path('signup', views.signup, name="signup"),
    path('test-token', views.test_token, name="test_token"),

    
]
