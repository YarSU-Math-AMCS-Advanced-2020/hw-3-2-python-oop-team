import datetime


class Client:
    def __init__(self, first_name: str = 'Unknown', last_name: str = 'Shadow',
                 birthdate: datetime = datetime.date(1970, 1, 1),
                 mail: str = 'noonecares@hmail.com', password: str = 'qwerty123'):
        self.first_name = first_name
        self.last_name = last_name
        self.birthdate = birthdate
        self.mail = mail
        self.password = password

    # TODO: getters, setters, phone number



