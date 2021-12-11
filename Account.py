# holds account information for a user
from Day import Day
from datetime import date


class Account:

    #fields
    name: str
    email: str
    date_joined: str

    # list of Day objects
    days: list[Day]

    def __init__(self, inName: str, inEmail: str):
        self.name = inName
        self.email = inEmail
        today = date.today()
        self.date_joined = today.strftime("%m/%d/%Y")
        self.days = []