""" Custom python file to keep all forms in one place """

# core Django imports
from django import forms

# package imports
from .models import Comment


class EmailPostForm(forms.Form):
    """
    Form that handles logic for allowing user to send email
    and also provides them to attach an optional comment to it
    """
    name = forms.CharField(max_length=50)
    to = forms.EmailField()
    # default widget is rendered as <input> element
    comments = forms.CharField(required=False,\
               widget=forms.Textarea) # display as <textarea> html element

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')
