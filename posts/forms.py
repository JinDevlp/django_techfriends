from django import forms
from .models import Post,Comment
from django.urls import reverse


# choices = Category.objects.all().values_list('name','name')


class PostForm(forms.ModelForm):

    class Meta:
        model = Post 
        fields = ('title', 'category','body','image1')
        
        widgets = {
            'category': forms.CheckboxSelectMultiple(),
        }
     
class EditPostForm(forms.ModelForm):
    class Meta:
        model = Post 
        fields = ('title', 'category','body','image1')
        
        widgets = {
            'category': forms.CheckboxSelectMultiple(attrs={'class' : 'forms-control' }),
        }

class CommentForm(forms.ModelForm):
    
    class Meta:
        model = Comment 
        fields = ('body',)