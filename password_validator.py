import string

class PasswordValidator:
    def __init__(self, min_length=8, require_upper=True, require_lower=True,
                 require_digit=True, require_special=True, blacklist=None):
        self.min_length = min_length
        self.require_upper = require_upper
        self.require_lower = require_lower
        self.require_digit = require_digit
        self.require_special = require_special
        self.blacklist = blacklist or []

    def validate(self, password):
        if len(password) < self.min_length:
            return False, "Password too short"

        if self.require_upper and not any(c.isupper() for c in password):
            return False, "Missing uppercase letter"

        if self.require_lower and not any(c.islower() for c in password):
            return False, "Missing lowercase letter"

        if self.require_digit and not any(c.isdigit() for c in password):
            return False, "Missing digit"

        if self.require_special and not any(c in string.punctuation for c in password):
            return False, "Missing special character"

        if password.lower() in (p.lower() for p in self.blacklist):
            return False, "Password is too common"

        return True, "Password is valid"
