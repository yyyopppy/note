from django import forms
from django.forms import ModelForm
from .models import NotePost, Comment


class NotePostForm(ModelForm):
    class Meta:
        model = NotePost
        fields = ['category', 'title', 'comment', 'image1', 'image2']
    


class SearchForm(forms.Form):
    query = forms.CharField(label='検索')


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']  





# class ReactionForm(ModelForm):
#     class Meta:
#         model = Reaction
#         fields = ['reaction_type']
#         # widgets = {
#         #     'reaction_type': forms.RadioSelect,
#         # }
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.fields['reaction_type'].empty_label = ""