from django import forms

class CommentForm(forms.Form):
    user_attrs={
        'type': 'text',
        'placeholder': 'Your Name',
        'name': 'username',
    }
    email_attrs = {
        'type': 'email',
        'placeholder': 'Your Email',
        'name': 'email',
    }
    comm_attrs = {
        'rows': '5',
        'placeholder': 'Your Comment',
        'name': 'comment',
    }
    username = forms.CharField(max_length=255, widget=forms.TextInput(attrs=user_attrs))
    email = forms.EmailField(widget=forms.EmailInput(attrs=email_attrs))
    comment = forms.CharField(widget=forms.Textarea(attrs=comm_attrs))
    image = forms.ImageField(max_length=255, required=False,
                            widget=forms.ClearableFileInput(attrs={'name':'image', 'type':'file'}))
    
class MessageForm(forms.Form):
    
    name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={
        'type':"text",
        'placeholder':"Your Name",
        'name':'name',
          }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'type':"email",
        'placeholder':"Your Email",
        'name':'email',
    }))
    subject = forms.CharField(widget=forms.TextInput(attrs={
        'type':"text",
        'placeholder':"Subject",
        'name':'subject',
    }))
    message = forms.CharField(widget=forms.Textarea(attrs={
        'type':"text",
        'placeholder':"Message",
        'name':'message',
        'cols':"30",
         'rows':"9",
    }))
    






    

    

