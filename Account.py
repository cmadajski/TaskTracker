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

    def __init__(self, inName: str, inEmail: str, inPass: str, inJoin: str):
        self.name = inName
        self.email = inEmail
        self.password = inPass
        self.date_joined = inJoin
        self.days = []