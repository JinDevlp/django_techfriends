from django.urls import path 

from .views import UserRegisterView,UserProfileView,PasswordChangeView,CreateProfilePage,UserEditView,EditProfilePageView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    
    path('edit-user/', UserEditView.as_view(), name='edit-user'), # edit user 
    
    path('<int:pk>/edit-profile/', EditProfilePageView.as_view(), name='edit-profile'), # edit user 
    
    path('create-profile/', CreateProfilePage.as_view(), name='create-profile'), # create profile after registration
    
    path('<int:pk>/profile/', UserProfileView.as_view(), name='profile'),
    
    # path('password/',auth_views.PasswordChangeView.as_view(template_name='registration/password.html')),
    path('password/', PasswordChangeView.as_view(),name='passwordchange')
]

  