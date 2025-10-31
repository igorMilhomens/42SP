import string


def is_valid_password(value: str) -> bool:
    """
    Recebe uma string e retorna se a string é uma senha valida
    """
    return (
        validate_len(value)
        & validate_char_upper(value)
        & validate_char_lower(value)
        & validate_char_num(value)
        & validate_char_spec(value)
        & validate_space(value)
    )


def validate_len(value: str) -> bool:
    """
    Valida se a senha possui:
        Mínimo de 8 caracteres
        Máximo de 16 caracteres
    """
    return 7 < len(value) < 17


def validate_char_upper(value: str) -> bool:
    """
    Valida se a senha possui menos uma letra maiúscula
    """
    return any(char.isupper() for char in value)


def validate_char_lower(value: str) -> bool:
    """
    Valida se a senha possui ao menos uma letra minúscula
    """
    return any(char.islower() for char in value)


def validate_char_num(value: str) -> bool:
    """
    Valida se a senha possui ao menos um dígito
    """
    return any(char.isdigit() for char in value)


def validate_char_spec(value: str) -> bool:
    """
    Valida se a senha possui ao menos um dígito
    """
    return any(char in string.punctuation for char in value)


def validate_space(value: str) -> bool:
    """
    Valida se não contem espaços em branco
    """
    return " " not in value
