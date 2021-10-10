
# from django.contrib.auth.forms import UserCreationForm

# class CustomUserCreationForm(UserCreationForm):
#     class Meta(UserCreationForm.Meta):
#         fields = UserCreationForm.Meta.fields + ("email",)

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
User = get_user_model()
# Create your forms here.

class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)
    address = forms.CharField(max_length=100)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2", "address")
    
    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.address = self.cleaned_data['address']
        if commit:
            user.save()
        return user