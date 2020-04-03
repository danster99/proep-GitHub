from django import forms

from HappyM8.users.models import User


class UserForm(forms.ModelForm):

    class Meta:
        model = User
        exclude = ['status', 'code', 'is_admin']

    first_name = forms.CharField(max_length=200, label='FIRST_NAME')
    last_name = forms.CharField(max_length=200, label='LAST_NAME')

    email = forms.EmailField(max_length=255, required=True, label='EMAIL')

    password = forms.CharField(
        widget=forms.PasswordInput, required=True, label='PASSWORD')
    repeat_password = forms.CharField(
        widget=forms.PasswordInput, required=True,
        label='REPEAT_PASSWORD')
    phone_number = forms.CharField(
        max_length=15, required=False, label='PHONE_NUMBER')

    def clean(self):
        password = self.cleaned_data['password']
        email = self.cleaned_data.get('email', None)
        if password != self.cleaned_data['repeat_password']:
            raise forms.ValidationError('PASSWORDS_DO_NOT_MATCH')

        if User.email_used(email):
            raise forms.ValidationError('EMAIL_ALREADY_CONNECTED')
