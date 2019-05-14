class Login:
    def __init__(self, toppings):
        self.toppings = toppings
        self._password_allowed = False


    @property
    def password_allowed(self):
        return self._password_allowed

    @password_allowed.setter
    def password_allowed(self, value):
        if value:
            password = input("Enter the Password: ")
            if password == "nomelase":
                self._password_allowed = value
            else:
                raise ValueError("Alert! Intruder!")

login = Login(["Ingeniero", "Software"])
print(login.password_allowed)
login.password_allowed = True
print(login.password_allowed)
