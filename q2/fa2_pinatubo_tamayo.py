class Patient:
    name: str
    bill_amount: float

    def __init__(self, name, bill_amount):
        self.name = name
        self.bill_amount = bill_amount

    def get_name(self):
        return f"Patient Name: {self.name}"

    def set_name(self, name):
        self.name = name

    def get_bill_amount(self):
        return f"Original Bill: ₱{self.bill_amount:.2f}"

    def set_bill_amount(self, bill_amount):
        self.bill_amount = bill_amount

    def calculate_bill(self):
        return f"Final Bill: ₱{self.bill_amount:.2f}\n"


class SeniorPatient(Patient):
    def calculate_bill(self):
        self.bill_amount = self.bill_amount - (self.bill_amount * 0.2)
        return f"Final Bill: ₱{self.bill_amount:.2f}\n"


class PhilHealthPatient(Patient):
    def calculate_bill(self):
        self.bill_amount = self.bill_amount - (self.bill_amount * 0.15)
        return f"Final Bill: ₱{self.bill_amount:.2f}\n"


print("Hospital Billing System\n-----------------------")
regular_patient = Patient("Juan Dela Cruz", 15000)
print(regular_patient.get_name())
print(regular_patient.get_bill_amount())
print(regular_patient.calculate_bill())

senior_patient = SeniorPatient("Maria Santos", 15000)
print(senior_patient.get_name())
print(senior_patient.get_bill_amount())
print(senior_patient.calculate_bill())

philhealth_patient = PhilHealthPatient("Pedro Reyes", 15000)
print(philhealth_patient.get_name())
print(philhealth_patient.get_bill_amount())
print(philhealth_patient.calculate_bill())
