from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.views import generic
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,UserChangeForm,PasswordChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView,CreateView,UpdateView
from django.contrib.auth.views import PasswordChangeView
from .models import Profile
from .forms import SignupForm,EditProfileForm,ProfileForm
from posts.views import PostView
from posts.models import Category,Post
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404

# Create your views here.

class UserRegisterView(CreateView): 
    form_class = SignupForm
    template_name = 'registration/register_form.html'
    success_url = reverse_lazy('login')
    

# class UserRegisterView(CreateView): 
#     form_class = SignupForm
#     template_name = 'registration/register_form.html'
#     success_url = reverse_lazy('create-profile')
    
#     def form_valid(self,form):
#         user = form.save()
#         login(self.request, user)
#         return redirect(self.success_url)


class CreateProfilePage(CreateView):
    model = Profile
    form_class = ProfileForm
    template_name = 'users/create_profile.html'
    success_url = reverse_lazy('home')
    
    def form_valid(self,form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class EditProfilePageView(UpdateView):
    form_class = ProfileForm 
    model = Profile 
    template_name = 'users/edit_profile.html'
    
    def form_valid(self,form):
        form.instance.user = self.request.user
        return super().form_valid(form)
 
 
# This is for editing User
class UserEditView(UpdateView):
    form_class = EditProfileForm
    template_name = 'users/edit_user.html'
    success_url = reverse_lazy('home')
    
    def get_object(self):
        return self.request.user 

class PasswordChangeView(PasswordChangeView):
    form_class = PasswordChangeForm 
    
    success_url = reverse_lazy('home')

class UserProfileView(LoginRequiredMixin,DetailView):
    model = Profile 
    template_name = 'users/profile.html'
  
    def get_context_data(self,*args,**kwargs):
        context = super().get_context_data(* args, **kwargs)
        page_user = get_object_or_404(Profile,id=self.kwargs['pk'])
        all_posts = Post.objects.all()
        user_posts = all_posts.filter(author_id=self.request.user.id)
        context['user_posts'] = user_posts
        context['page_user'] = page_user 
        
        return context 
        
    
    