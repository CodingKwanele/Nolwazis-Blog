from django import forms
from .models import Recipe

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'submitted_by', 'description', 'difficulty', 'ingredients', 'instructions', 'image']
        widgets = {
            'difficulty': forms.Select(attrs={
                'class': 'form-select',
            }),
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'e.g. Grandma\'s Bobotie',
            }),
            'submitted_by': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Your name (optional)',
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Brief description of the recipe',
            }),
            'ingredients': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 5,
                'placeholder': 'e.g. 2 cups flour, 1 tsp salt, 3 eggs...',
            }),
            'instructions': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 8,
                'placeholder': 'Enter each step on a new line',
            }),
            'image': forms.ClearableFileInput(attrs={
                'class': 'form-control',
            }),
        }
