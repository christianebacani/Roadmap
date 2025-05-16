# Question: Not very secure
# Categories: 5 Kyu

def alphanumeric(password: str) -> bool:
    def is_password_atleast_one_character(password_char: str) -> bool:
        if len(password_char) > 0:
            return True
        
        return False
    
    def is_passowrd_contains_only_alnum(password_char: str) -> bool:
        for i in range(len(password_char)):
            if not password_char[i].isalnum():
                return False
        
        return True
    
    def is_password_does_not_contain_whitespaces_underscore(password_char: str) -> bool:
        for i in range(len(password_char)):
            if password_char[i] == ' ' or password_char[i] == '_':
                return False

        return True

    if is_password_atleast_one_character(password) and is_passowrd_contains_only_alnum(password) and is_password_does_not_contain_whitespaces_underscore(password):
        return True

    return False 