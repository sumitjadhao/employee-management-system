from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser


class EmployeeCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    phone = forms.CharField(required=False)
    department = forms.CharField(required=False)
    designation = forms.CharField(required=False)
    date_joined_company = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'phone', 'department', 'designation', 'date_joined_company', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.role = 'employee'
        user.email = self.cleaned_data['email']
        user.phone = self.cleaned_data['phone']
        user.department = self.cleaned_data['department']
        user.designation = self.cleaned_data['designation']
        user.date_joined_company = self.cleaned_data['date_joined_company']
        if commit:
            user.save()
        return user