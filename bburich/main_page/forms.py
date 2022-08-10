from datetime import datetime
from django import forms
from django.core.exceptions import ValidationError

from .models import Experience


class ExperienceAdminForm(forms.ModelForm):

    class Meta:
        model = Experience
        fields = '__all__'

    def clean(self):
        start_at = self.cleaned_data.get('start_at')
        if start_at > datetime.now().date():
            raise ValidationError('start_at field must be earlier than today')

        end_at = self.cleaned_data.get('end_at')
        if end_at and end_at > datetime.now().date():
            raise ValidationError('end_at field must be earlier than today')

        if end_at and end_at < start_at:
            raise ValidationError(
                'end_at filed must be earlier than start_at field'
            )
