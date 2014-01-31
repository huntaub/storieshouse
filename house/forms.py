from django import forms
from house.models import Story, StoryAuthor
from django.forms.widgets import *

class StoryForm(forms.ModelForm):
    class Meta:
        model = Story
        exclude = ('user', 'date_added', 'slug', 'viewcount')
        widgets = {
            'title': TextInput(attrs={'class': 'form-control'}),
            'body': Textarea(attrs={'class': 'form-control'}),
            'icon': Select(attrs = {'class': 'form-control'}),
            'image': TextInput(attrs = {'class': 'form-control', 'placeholder': 'Use icon for story.'}),
            'category': Select(attrs = {'class': 'form-control'}),
            # 'published': CheckboxInput(attrs = {'class': 'form-control'}),
        }

class StoryAuthorForm(forms.ModelForm):
    about = forms.CharField(widget = Textarea(attrs = {'class': 'form-control'}))
    avatar = forms.CharField(widget = TextInput(attrs = {'class': 'form-control'}))
    class Meta:
        model = StoryAuthor
        exclude = ('user')