import os
from urllib.parse import urlparse

from django.core.exceptions import ValidationError


def validate_logo(logo):

    ext = os.path.splitext(logo.name)[1]
    valid_extensions = ['.jpg', '.jpeg', '.png', '.svg']
    if not ext.lower() in valid_extensions:
        raise ValidationError('Unsupported file extension.')

    if logo.file.size > 128 * 1024:
        raise ValidationError('Logo must be less than 128 kitobytes.')


def validate_github(link):
    if not link:
        raise ValidationError('Link is empty')
    url_obj = urlparse(link)
    if not url_obj.hostname == 'github.com':
        raise ValidationError(f'{url_obj.hostname} links not allowed')
