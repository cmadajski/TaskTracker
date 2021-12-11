# holds account information for a user
from Day import Day
from datetime import date


class Account:

    #fields
    name: str
    email: str
    password: str
    date_joined: str

    # list of Day objects
    days: list[Day]

    def __init__(self, inName: str, inEmail: str, inPass: str):
        self.name = inName
        self.email = inEmail
        self.password = inPass
        today = date.today()
        self.date_joined = today.strftime("%m/%d/%Y")
        self.days = []