from django.core.exceptions import ValidationError
from django.forms import Form, PasswordInput
from django.forms.fields import CharField
import re

__author__ = 'a141890'


class UserLoginForm(Form):
    id = CharField(label="ID")
    password = CharField(widget=PasswordInput(), label="PASSWORD")

    def clean_id(self):
        id = self.cleaned_data['id']
        id = re.sub(r'\s+', '', id, flags=re.IGNORECASE|re.UNICODE)
        if not id:
            raise ValidationError('ID is required')
        return id