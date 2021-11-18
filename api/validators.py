from datetime import datetime

from django.core.exceptions import ValidationError


def correct_year_validator(value):
    if value < 850 or value > datetime.now().year:
        raise ValidationError(
            ('%(value)Год введен неверно!'),
            params={'value': value},
        )
