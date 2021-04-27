# core Django imports
from django import forms


class EmailPostForm(forms.Form):
    """
    Form that handles logic for allowing user to send email
    and also provides them to attach an optional comment to it
    """
    name = forms.CharField(max_length=50)
    email = forms.EmailField()
    to = forms.EmailField()
    # default widget is rendered as <input> element
    comments = forms.CharField(required=False,\
               widget=forms.Textarea) # display as <textarea> html element
