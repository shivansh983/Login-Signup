from django.urls import path
from .views import SignUpView, LoginView, UserSearchView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('search/', UserSearchView.as_view(), name='user_search'),
]
