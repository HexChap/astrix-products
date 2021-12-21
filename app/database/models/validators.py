import re

from tortoise.validators import Validator, ValidationError


PHONE_NUMBER_PATTERN = r"^(\+|00)?[1-9][0-9 \-\(\)\.]{7,32}$"


class PhoneNumberValidator(Validator):
    """
    Validator to check if a given value is phone number.
    """

    def __init__(self):
        self.phone_pattern = re.compile(PHONE_NUMBER_PATTERN)

    def __call__(self, value):
        if not self.phone_pattern.match(value):
            raise ValidationError(f"Value '{value}' is not email.")
