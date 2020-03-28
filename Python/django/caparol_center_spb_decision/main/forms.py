from django import forms

class EmailForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'type':"email", 'name':"email", 'placeholder':"Email"}))

        
