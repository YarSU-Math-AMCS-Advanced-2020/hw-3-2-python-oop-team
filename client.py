class Client:
    def __init__(self, client_id: str):
        self.client_id = client_id
        self.first_name = 'Unknown'
        self.last_name = 'Shadow'
        self.birthdate = '1.1.1970'
        self.mail = 'noonecares@hmail.com'
        self.phone_number = '+79000000000'
        self.password = 'qwerty123'

    def registration(self, first_name: str, last_name: str, birthdate: str, mail: str, phone_number: str,
                     password: str):
        self.first_name = first_name
        self.last_name = last_name
        self.birthdate = birthdate
        self.mail = mail
        self.phone_number = phone_number
        self.password = password
