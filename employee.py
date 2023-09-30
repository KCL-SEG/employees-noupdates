"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name, monthly_salary, contract_hours, hour_rate, bonus, commision_rate, number_of_commissions):
        self.name = name
        self.monthly_salary = monthly_salary
        self.contract_hours = contract_hours
        self.hour_rate = hour_rate
        self.bonus = bonus
        self.commision_rate = commision_rate
        self.number_of_commissions = number_of_commissions
        self.pay = ""

    def get_pay(self):
        self.pay = self.monthly_salary + (self.contract_hours * self.hour_rate) + self.bonus + (self.commision_rate * self.number_of_commissions)
        return self.pay
    
    def contract_type(self):
        if self.monthly_salary > 0:
            return "monthly salary of " + str(self.monthly_salary)
        else: 
            return "contract of " + str(self.contract_hours) + " hours at " + str(self.hour_rate) + "/hour"
        
    def get_bonus(self):
        if self.bonus == 0:
            return ""
        elif self.bonus > 0:
            return " and receives a bonus commission of " + str(self.bonus)
        
    def get_commision(self):
        if self.number_of_commissions == 0:
            return ""
        elif self.number_of_commissions > 0:
            return " and receives a commission for " + str(self.number_of_commissions) + " contract(s) at " + str(self.commision_rate) + "/contract"

    def __str__(self):
        return self.name + " works on a " + self.contract_type() + self.get_bonus() + self.get_commision() +  ". Their total pay is " + str(self.get_pay()) + "."
    

# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie', 4000, 0, 0, 0, 0, 0,)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie', 0, 100, 25, 0, 0, 0)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee', 3000, 0, 0, 0, 200, 4)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan', 0, 150, 25, 0, 220, 3)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie', 2000, 0, 0, 1500, 0, 0)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel', 0, 120, 30, 600, 0, 0)

print(str(billie)) 
print(str(charlie)) 
print(str(renee)) 
print(str(jan)) 
print(str(robbie)) 
print(str(ariel)) 