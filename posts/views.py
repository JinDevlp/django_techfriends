from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
# listview = query set from database and brings back all record
# detailview = query set from database and brings back one record
from .models import Post, Category,Comment
from .forms import PostForm, EditPostForm, CommentForm
from users.models import Profile
from django.urls import reverse_lazy,reverse
# Create your views here.

class HomeView(ListView):
    model = Post
    template_name = 'techfriends/home.html'
    cats = Category.objects.all()
    post = Post.objects.all()
    ordering = ['-created']
    
    def get_context_data(self, *args, **kwargs):
        category_menu = Category.objects.all()
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context['category_menu'] = category_menu
        return context
    

class PostView(DetailView):
    model = Post 
    template_name = 'posts/post_detail.html'
    
    def get_context_data(self, *args, **kwargs):
        category_menu = Category.objects.all()
        context = super(PostView, self).get_context_data(*args, **kwargs)
        
        stuff = get_object_or_404(Post, id=self.kwargs['pk']) #look up a post with the pk 
        total_likes = stuff.total_likes()
        context['category_menu'] = category_menu
        context['total_likes'] = total_likes
        return context

def LikeView(request,pk):
    post = get_object_or_404(Post, id =request.POST.get('post_id')) # post_id comes from the button on post_detail.html
    post.likes.add(request.user)
    return HttpResponseRedirect(reverse('post-detail', args=[str(pk)])) # redirect user to the detail page


def CategoryView(request, cats):
    topic_posts = Category.objects.get(name__iexact=cats).post_set.all()
    ordered_topic_posts = topic_posts.order_by('-created')

    return render(request, 'posts/topics.html', {'category': cats, 'topic_posts': ordered_topic_posts})
    

class AddPostView(LoginRequiredMixin,CreateView):
    model = Post
    form_class = PostForm
    template_name = 'posts/post_form.html'
    success_url = reverse_lazy('home')
    
    def form_valid(self,form):
        obj = form.save(commit=False)   
        obj.author = self.request.user
        obj.save() 
        return super(AddPostView,self).form_valid(form)
    
class AddCommentView(CreateView):
    model = Comment 
    form_class = CommentForm
    template_name = 'posts/add_comment.html'
    success_url = reverse_lazy('home')
        
    def form_valid(self,form):
        obj = form.save(commit=False)
        obj.user = self.request.user 
        obj.post_id = self.kwargs['pk']
        obj.save()
        return super(AddCommentView,self).form_valid(form)
    
        
    
    # def get_context_data(self, *args, **kwargs):
    #     category_menu = Category.objects.all()
    #     context = super(AddPostView, self).get_context_data(*args, **kwargs)
    #     context['category_menu'] = category_menu
    #     return context
    
class UpdatePostView(UpdateView):
    model = Post 
    form_class = EditPostForm
    template_name = 'posts/post_update_form.html'
    
   
    # def get_absolute_url(self):
    #     return reverse('post-detail')
    # fields = '__all__'
    # fields = ('title', 'body')
    # def createProject(self, request):
    #     profile = request.user.profile
    #     form = PostForm
    #     if form.is_valid():
    #         project = form.save(commit=False)
    #         project.owner = profile
    #         project.save()
            
    #     context = {'form': form}
    #     return render(request, "projects/project_form.html", context)
    
class DeletePostView(DeleteView):
    model = Post 
    template_name = 'posts/post_delete.html'
    success_url = reverse_lazy('home')