class EmployeeSalary:
    hourly_payment = 400
    
    def __init__(self, name, rest_days=None, hours = None, email = None):
        self.name = name
        self.rest_days = rest_days
        self.hours = hours        
        self.email = email
    @classmethod
    def get_hours(cls, name, rest_days=None, hours=None, email=None):
        if hours is None:
            hours = (7 - rest_days) * 8
        return cls(name, rest_days, hours, email)


    @classmethod
    def get_email(cls, name, rest_days=None, hours=None, email=None):
        if email is None:
            email = f"{name}@email.com"
        return cls(name, rest_days, hours, email)
    
    @classmethod
    def set_hourly_payment(cls, payment):
        cls.hourly_payment = payment


    def salary(self):
        return self.hours * EmployeeSalary.hourly_payment