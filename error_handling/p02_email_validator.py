from re import findall


class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


class SpecialSymbolAndNumberError(Exception):
    pass


MIN_NAME_LENGTH = 4
VALID_DOMAINS = ("com", "bg", "org", "net")
SPECIAL_SYMBOLS = ("*", "_", "-", ".")
pattern = r"([a-z0-9]+[a-z0-9\-\.\_\*]*)\b"
email = input()

while email != "End":
    if "@" not in email:
        raise MustContainAtSymbolError("Email must contain @")

    elif len(email.split("@")[0]) <= MIN_NAME_LENGTH:
        raise NameTooShortError("Name must be more than 4 characters")

    elif email.split(".")[-1] not in VALID_DOMAINS:
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")

    elif email.split("@")[0] != findall(pattern, email.split("@")[0])[0]:
        raise SpecialSymbolAndNumberError(f"Email address must contain at least one digit and one special symbol from"
                                          f" the following: {', '.join(s for s in SPECIAL_SYMBOLS)}")

    else:
        print("Email is valid")

    email = input()

