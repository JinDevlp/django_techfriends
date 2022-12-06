from django.urls import path 

from .views import HomeView, PostView, AddPostView, UpdatePostView, DeletePostView, CategoryView,AddCommentView,LikeView
from . import views

urlpatterns = [
    path('',HomeView.as_view(), name='home'),
    path('post/<int:pk>', PostView.as_view(), name='post-detail'),
    path('create-post/', AddPostView.as_view(), name='create-post'),
    path('post/update/<int:pk>', UpdatePostView.as_view(), name='update-post'),
    path('post/<int:pk>/delete', DeletePostView.as_view(), name='delete-post'),
    path('category/<str:cats>', CategoryView, name = 'category'),
    path('post/<int:pk>/comment', AddCommentView.as_view(),name='add-comment'),
    path('like/<int:pk>', LikeView, name='like_post')

]
