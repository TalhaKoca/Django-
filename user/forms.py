from django import forms
from django.contrib.auth.models import User

class LoginForm(forms.Form):

    username = forms.CharField(label="Kullanıcı Adı")
    password = forms.CharField(label="Parola",widget=forms.PasswordInput)

class RegisterForm(forms.Form):
    
    username = forms.CharField(max_length=44,label="Kullanıcı Adı")
    password = forms.CharField(max_length=20,label="Parola",widget=forms.PasswordInput)
    # widget=forms.PasswordInput parola alanı şeklinde gözükecek...
    confirm = forms.CharField(max_length=20,label="Parolayı Doğrula",widget=forms.PasswordInput)
    
    def clean(self): # Form sınfının içindeki bir method
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        confirm = self.cleaned_data.get("confirm")
        user = User.objects.filter(username__contains = username)

        if password and confirm and password != confirm:
            raise forms.ValidationError("Paralolar Eşleşmiyor...")
        elif user:
            raise forms.ValidationError("Kullanıcı adı sistemde kayıtlıdır.")
        
    
        values = {
            "username" : username,
            "password" : password

        }
        # sözlükleri değerleri döndürebilmek için kullandık...
        return values
""" if User.objects.filter(username_iexact=username).exist():
            raise forms.ValidationError("Bu kullanıcı adı zaten kullanılıyor...")"""

      