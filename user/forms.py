from django import forms 


class RegisterForm(forms.Form):
    username = forms.CharField(max_length = 30, label = 'Username')
    password = forms.CharField(max_length =30, label ="Password", widget = forms.PasswordInput)
    confirm = forms.CharField(max_length =30, label ="Confirm Password", widget = forms.PasswordInput)

    def clean(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        confirm = self.cleaned_data.get("confirm")

        if password and confirm and confirm != password:
            raise forms.ValdationError("Passwords did not match!")
        values = { 
            'username': username,
            'password': password
        }
        return values

class LoginForm(forms.Form):
    username = forms.CharField(label='Username')
    password = forms.CharField(label='Password',widget=forms.PasswordInput)
