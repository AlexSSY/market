from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _
import re


def phone_regex_validator(value: str) -> None:
    if re.fullmatch('\+\d{10,24}', value) == None:
        raise ValidationError(message=_('Phone number is invalid'))
    elif value.startswith('+38'):
        raise ValidationError(message=_('Your region is not allowed'))
