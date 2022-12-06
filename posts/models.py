from django.db import models
from django.contrib.auth.models import User
from users.models import Profile
from django.urls import reverse
# Create your models here.

# Post Model
class Post(models.Model):
    title = models.CharField(max_length=300)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True) # delete posts
    body = models.TextField(blank=True, null=True)
    image1 = models.ImageField(null=True, blank=True,upload_to='post_images/', default='post_images/post_default.png')
    created = models.DateTimeField(auto_now_add=True)
    # category = models.CharField(max_length=10, choices= CHOICES)
    category = models.ManyToManyField('Category', verbose_name="Category", blank=True)
    likes = models.ManyToManyField(User, related_name='tech_post')
    
    def total_likes(self):
        return self.likes.count()
    
    def __str__(self):
        return self.title + ' | ' + str(self.author)
    
    def get_absolute_url(self):
        return reverse('home')
        # return reverse('post-detail', args=(str(self.id)))
    # return to the post detail page

CHOICES = [
    ('Interview','Interview'),('Resume','Resume'), ('Project', 'Project'), ('Question', 'Question')
]
class Category(models.Model):
    name = models.CharField(max_length=100, choices=CHOICES)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('home')
    
class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments' ,on_delete=models.CASCADE, null=True, blank=True)
    user = models.ForeignKey(User, related_name='user', on_delete=models.CASCADE, null=True, blank=True)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.user)
    