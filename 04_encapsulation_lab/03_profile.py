# import re
# pattern_for_rusername = r"\S{5,15}"
# pattern_for_password = r"^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$"
# no regex no pain :D


class Profile:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value):
        if len(value) < 5 or len(value) > 15:
            raise ValueError("The username must be between 5 and 15 characters.")
        self.__username = value


    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, value):
        is_length_valid = len(value) >= 8
        is_uppercase_presented = len([char for char in value if char.isupper()]) > 0
        is_digit_presented = len([char for char in value if char.isdigit()]) > 0
        if not is_length_valid or not is_uppercase_presented or not is_digit_presented:
            raise ValueError("The password must be 8 or more characters with at least 1 digit and 1 uppercase letter.")
        self.__password = value

    def __str__(self):
        return (f'You have a profile with username:'
                f' "{self.username}" and password: {"*" * len(self.password)}')
