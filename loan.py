from datetime import date
from dateutil.relativedelta import relativedelta

class Loan:
  
  def __init__(self,P,r,n):
    assert P > 0,"Principal can't be negative"
    assert r > 0,"Rate of Interest can't be negative"
    assert n > 0,"Tenure can't be negative"
    self.principal = P
    self.rate = r 
    self.numberOfPeriods = n 
    self.payment = self.principal*(self.rate*((1 + self.rate)**self.numberOfPeriods) / (((1 + self.rate)**self.numberOfPeriods) - 1))
    self.schedule = self.amortization_schedule()
    


  def amortization_schedule(self):
    amount = self.principal
    period = 0
    balance =   amount
    schedule = []
    total_interest = 0
    monthly_date = date.today() + relativedelta(months=1)
    while period < self.numberOfPeriods:
      monthly_interest = balance * self.rate
      amount =  self.payment - monthly_interest
      balance = balance - amount
      period+=1
      total_interest += monthly_interest 
      schedule_dict = dict(Period=period,Date=monthly_date,Interest=monthly_interest,Principal=amount,Balance=balance)
      schedule.append(schedule_dict) 
      monthly_date +=relativedelta(months=1)
    self.total_interest = total_interest
    return schedule

  def print_schedule(self):
    print(" ")
    print("Your monthly Amortization payment is: $ {:.2f}".format(self.payment))
    print(" ")
    print("Following is the Amortization Schedule\n")
    print("Period no.  Start date\t\t    Interest\t   Principal\tBalance Amount")
    print("--------------------------------------------------------------------------")
    for entry in self.schedule: 
      interest = entry["Interest"]
      principal = entry["Principal"]
      Period = entry["Period"]
      balance = entry["Balance"]
      startDate = entry["Date"]
      each_row = "{:.0f} \t    {}\t\t $  {:.2f}\t $  {:.2f}\t $  {:.2f}"
      print(each_row.format(Period,startDate,interest,principal,balance))
    print("\nYou have paid a total interest of $ {:.2f}".format(self.total_interest))
    print("\nYou have successfully returned a principal of : $ {:.2f}".format(self.principal))



# after you learn about dates, your next goal is as follows.
# - in Loan create a new property startDate as the beginning of the coming month. e.g. if you were creating Loan today, the "startDate" properrty should hold value for August 1st 2020.  The date should be object, not string.
# - In amortization calculation, add a start date for each period in the dictionary. Again, add objects in the dictionary. For now, assume that each period is a month.
# - In print amortization schedule, print the date in the second column after period number. Use date format as yyyy/mm/dd

#DOUBTs
#if month is december then startDate should be january,but will this code give me month as 12 + 1=01 or 12 + 1=13