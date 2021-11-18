from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'categories', 'tags']

class UpdateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']
    def save(self, commit=True):
        post = self.instance
        post.title = self.cleaned_data['title']
        post.content = self.cleaned_data['content']
        post.tags.clear()
        tags = self.cleaned_data['tags']
        for tag in tags:
            post.tags.add(tag)
        if commit:
            post.save()
        return post