from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

class SubForm(forms.Form):
    sub_email = forms.CharField(max_length=20)

    def clean_renewal_date(self):
        data = self.cleaned_data['sub_email']

        # Check if a date is not in the past.
        if '@' not in data :
            raise ValidationError(_('Invalid Email - Incorrect email format'))

        # # Check if a date is in the allowed range (+4 weeks from today).
        # if data > datetime.date.today() + datetime.timedelta(weeks=4):
        #     raise ValidationError(_('Invalid date - renewal more than 4 weeks ahead'))

        # Remember to always return the cleaned data.
        return data