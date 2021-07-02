from django.core import validators
from django import forms
from .models import User

class Userregistration(forms.ModelForm):
    class Meta:
        model=User
        fields=['image','company','username','password','email','firstname','lastname','address','city','country','postal_code','about_me']
        widgets={
            'image':forms.FileInput(attrs={'class': 'form-control','enctype': 'multipart/form-data boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW'},),
            'company':forms.TextInput(attrs={'class':'form-control'}),
            'username':forms.TextInput(attrs={'class':'form-control'}),
            'password':forms.PasswordInput(render_value=True,attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'firstname':forms.TextInput(attrs={'class':'form-control'}),
            'lastname':forms.TextInput(attrs={'class':'form-control'}),
            'address':forms.TextInput(attrs={'class':'form-control'}),
            'city':forms.TextInput(attrs={'class':'form-control'}),
            'country':forms.TextInput(attrs={'class':'form-control'}),
            'postal_code':forms.NumberInput(attrs={'class':'form-control'}),
            'about_me':forms.TextInput(attrs={'class':'form-control'})

            #'password':forms.PasswordInput(render_value=True,attrs={'class':'form-control'}),
           # 'confirmpassword':forms.PasswordInput(render_value=True,attrs={'class':'form-control'}),
        }

class Userlogin(forms.ModelForm):
    class Meta:
        fields = ['username', 'password']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(render_value=True, attrs={'class': 'form-control'}),

        }



        def clean(self, *args, **kwargs):
            data = self.cleaned_data
            content = data.get('content', None)
            if content == "":
                content = None
            image = data.get("image", None)
            if content is None and image is None:
                raise forms.ValidationError('content or image is required.')
            return super().clean(*args, **kwargs)
class Userlogin(forms.ModelForm):
    class Meta:
        fields=['username','password']
        widgets={
            'username':forms.TextInput(attrs={'class':'form-control'}),
            'password': forms.PasswordInput(render_value=True, attrs={'class': 'form-control'}),

        }
