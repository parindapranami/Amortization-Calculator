# Parinda, regarding converting things to object oriented. Here are some hints.
# If I write a program that uses this Loan class, I want to be able to do the following. 
# 1) Create a Loan object like this.
 
#     loan = Loan(150000, 4.5, 360)

# 2) I should be able to use properties on the loan like this.

# print(loan.principal)
# print(loan.interest)
# print(loan.numberOfPeriods)

# 3) I should also be able to print payment like this.

# print(loan.paymentPerPeriod)

# 4) I should be able to get payment schedule (array of dictionaries) like this 

# schedule = loan.generateAmortizationSchedule()

# 5) I should be able to print the schedule like this.

# loan.printAmortizationSchedule()

# 6) All the code should be in a "Loan.py" file
#  The properties above are named the way I would name in java or swift (lowerCamelCase). If python has different convention for naming properties, then you should find out and use that. If you can't figure out, use lowerCamelCase style.
#  After you implement Loan.py, it should be very easy to change command line program to use Loan.py instead.


class Loan:

  def __init__(self,P,r,n):
    self.principal = P
    self.rate = r
    self.numberOfPeriods = n
    self.payment = self.principal*(self.rate*((1 + self.rate)**self.numberOfPeriods) / (((1 + self.rate)**self.numberOfPeriods) - 1))
    #self.paymentPerPeriod = amortization_payment(self)
    # self.generateAmortizationSchedule =amortization_schedule(P,r,n)
    # schedule = self.generateAmortizationSchedule 

  # def total_interest(schedule):
  #   interest = 0.0
  #   for dictionary in schedule:
  #     interest += float(dictionary['Interest'])
  #   return interest

  def amortization_schedule(self):
    #payment = self.payment
    #need to change these values
    period = 0
    balance = self.principal
    schedule = []
    while period < self.numberOfPeriods:
      monthly_interest = balance * self.rate
      self.principal =  self.payment - monthly_interest
      balance = balance - self.principal
      period+=1
      schedule_dict = dict(Period=period,Interest=monthly_interest,Principal=self.principal,Balance=balance)
      schedule.append(schedule_dict) 
    return schedule

  # def amortization_payment(self):
  #   A = self.principal*(self.rate*((1 + self.rate)**self.numberOfPeriods) / (((1 + self.rate)**self.numberOfPeriods) - 1))
  #   return A
  
  def print_schedule(self):
    #payment = self.payment
    print(" ")
    print("Your monthly Amortization payment is: $ {:.2f}".format(self.payment))
    print(" ")
    print("Following is the Amortization Schedule\n")
    print("Period no.\t  Interest\t Principal\tBalance Amount")
    print("--------------------------------------------------------------------------")
    final_schedule = self.amortization_schedule()
    for entry in final_schedule:
      interest = entry["Interest"]
      principal = entry["Principal"]
      Period = entry["Period"]
      balance = entry["Balance"]
      each_row = "{:.0f}\t\t $  {:.2f}\t $  {:.2f}\t $  {:.2f}"
      print(each_row.format(Period,interest,principal,balance))
  
    # final_interest = total_interest(final_schedule)
    # print("\nYou have paid a total interest of $ {:.2f}".format(final_interest))
    # print("\nYou have successfully returned a principal of : $ {:.2f}".format(self.principal))


loan = Loan(165000,4.5,30) 

print(loan.print_schedule())