class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    def __str__(self):
        return str(self.day) + "/" + str(self.month) + "/" + str(self.year)

    def is_leap_year(self, year):
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            return True
        else:
            return False

    def days_in_month(self, month, year):
        if month == 2:
            if self.is_leap_year(year):
                return 29
            else:
                return 28
        # special logic of mine(odd months and even months)
        elif (month <= 7 and month % 2 == 1) or (month >= 8 and month % 2 == 0):
            return 31
        else:
            return 30

    def __add__(self, other):
        day = self.day + 1
        month = self.month
        year = self.year

        if day > self.days_in_month(month, year):
            day = 1
            month = month + 1
            if month > 12:
                month = 1
                year = year + 1

        return Date(day, month, year)


# test
today = Date(31, 12, 2024)
tomorrow = today + 1
print("Today:", today)
print("Tomorrow:", tomorrow)
