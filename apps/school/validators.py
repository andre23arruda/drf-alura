import re
from validate_docbr import CPF

def validate_cpf(value: str):
    cpf = CPF()
    return cpf.validate(value)


def validate_name(value: str):
    return value.isalpha()


def validate_phone(value: str):
    PHONE_REGEX = r'^\(?(\d{2})\)?\s?(\d{4,5})[- ](\d{4})$'
    result = re.findall(PHONE_REGEX, value)
    return result
