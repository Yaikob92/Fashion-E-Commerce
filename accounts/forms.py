from django import forms
from . models import Account

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Account
        fields  = ['first_name','last_name','email','password']

    def clean(self):
        cleaned_data = super(RegistrationForm,self).clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        print(f"Password: {password}, Confirm Password: {confirm_password}")

        if password != confirm_password:
            raise forms.ValidationError("Passwords do not match.")
        