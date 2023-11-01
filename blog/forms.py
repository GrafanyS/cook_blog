from django import forms
from .models import Comment, Recipe


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ['create_at', 'post']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'name'}),
            'email': forms.EmailInput(attrs={'placeholder': 'email'}),
            'website': forms.TextInput(attrs={'placeholder': 'website'}),
            'message': forms.Textarea(attrs={'placeholder': 'message'})
        }


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        exclude = ['create_at', 'recipes']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'name'}),
            # 'serves': forms.TextInput(attrs={'placeholder': 'serves'}),
            'prep_time': forms.TextInput(attrs={'placeholder': 'prep_time'}),
            'cook_time': forms.TextInput(attrs={'placeholder': 'cook_time'}),
            'ingredients': forms.Textarea(attrs={'placeholder': 'ingredients'}),
            'directions': forms.Textarea(attrs={'placeholder': 'directions'})
        }
