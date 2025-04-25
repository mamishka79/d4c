from django import forms

from .models import Comment, Post


class CommentForm(forms.ModelForm):
    """Form for adding comments."""
    class Meta:
        model = Comment
        fields = ['text']
        widgets = {
            'text': forms.Textarea(attrs={
                'rows': 3,
                'placeholder': 'Your comment…',
            }),
        }


class PostForm(forms.ModelForm):
    """Form for creating and editing posts."""
    class Meta:
        model = Post
        fields = ['title', 'content']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={
                'rows': 6,
                'class': 'form-control',
            }),
        }
