class Bill:
    """
    bill object
    """

    def __init__(self, amount, period):
        self.amount = amount
        self.period = period


class Flatmate:
    """
    flatmate object
    """

    def __init__(self, name, days_in_house):
        self.name = name
        self.days_in_house = days_in_house

    def pays(self, bill, flatmate):
        weight = (self.days_in_house /
                  (self.days_in_house + flatmate.days_in_house))
        to_pay = weight * bill.amount
        return to_pay