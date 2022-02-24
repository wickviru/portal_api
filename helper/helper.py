from django.core.exceptions import ValidationError
from django.core.validators import validate_email

def validateEmail(value):
    try:
        validate_email(value)
    except ValidationError as e:
        return 0
    else:
        return 1