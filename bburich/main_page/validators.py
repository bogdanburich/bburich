from django.core.exceptions import ValidationError


def validate_logo(logo):
    if logo.file.size > 128*1024:
        raise ValidationError('Logo must be less than 128 kitobytes.')
