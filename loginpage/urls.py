from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path('search/', views.search, name='search'),
    path('', views.login_view, name='index'),  # Redirect root URL to login page
]
