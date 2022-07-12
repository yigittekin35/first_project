from django import forms
from django.core import validators
from first_app.models import User

#Custom validation, aldığı parametrenin ismi value olmalı
def check_for_z(value):
    if value[0].lower() != 'z':
        raise forms.ValidationError('Name needs to start with Z')

class FormName(forms.Form):
    name = forms.CharField(validators = [check_for_z])
    email = forms.EmailField()
    verify_email = forms.EmailField(label = 'Enter your email again')
    text = forms.CharField(widget = forms.Textarea, label = 'Description')
    botcatcher = forms.CharField(required = False,
                                 widget = forms.HiddenInput,
                                 validators = [validators.MaxLengthValidator(0)])

    #Submit click sonrası
    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data['email']
        verify_email = all_clean_data['verify_email']
        if email != verify_email:
            raise forms.ValidationError('Emails are not equal')

    # def clean_botcatcher(self):
    #     botcatcher = self.cleaned_data['botcatcher']
    #     if len(botcatcher) > 0:
    #         raise forms.ValidationError('Gotcha Bot!')
    #     return botcatcher

class NewUser(forms.ModelForm):
    #Örnek validators
    # first_name = forms.CharField(validators: [check_for_z])
    class Meta:
        model = User
        #Tüm alanları kullanmak için __all__ kullanılıyor
        #Harici alanlar için exclude = ['field1', 'field2']
        #1-2 alan eklemek için fields = ('field1', 'field2')
        fields = '__all__'
