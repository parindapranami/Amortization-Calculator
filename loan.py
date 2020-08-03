#this file contains just the methods 

from datetime import date
from datetime import datetime
from dateutil.relativedelta import relativedelta

class AmortizationPeriod :

  def __init__(self):#self,monthly_interest,amount,balance,period,monthly_date):
    # self.period = period
    # self.date = monthly_date
    # self.interest = monthly_interest
    # self.principal = amount
    # self.balance = balance
    pass
    

class Loan:
  
  def __init__(self,P,r,n,d):
    assert P > 0,"Principal can't be negative"
    assert r > 0,"Rate of Interest can't be negative"
    assert n > 0,"Tenure can't be negative"
    self.principal = P
    self.rate = r 
    self.numberOfPeriods = n 
    self.payment = self.principal*(self.rate*((1 + self.rate)**self.numberOfPeriods) / (((1 + self.rate)**self.numberOfPeriods) - 1))
    self.startDate = d
    self.schedule = self.amortization_schedule()
    

  def amortization_schedule(self):
    amount = self.principal
    period = 0 
    balance =   amount
    schedule = []
    total_interest = 0
    monthly_date = self.startDate
    while period < self.numberOfPeriods:
      monthly_interest = balance * self.rate
      amount =  self.payment - monthly_interest
      balance = balance - amount
      period+=1
      total_interest += monthly_interest 
      ap = AmortizationPeriod()
      #schedule_dict = dict(Period=period,Date=monthly_date,Interest=monthly_interest,Principal=amount,Balance=balance) #class amortization period
      ap.period = period
      ap.date = monthly_date
      ap.interest = monthly_interest
      ap.principal = amount
      ap.balance = balance
      schedule.append(ap) 
      monthly_date += relativedelta(months=1)
    self.total_interest = total_interest
    return schedule

  def print_schedule(self):
    print(" ")
    print("Your monthly Amortization payment is: $ {:.2f}".format(self.payment))
    print(" ")
    print("Following is the Amortization Schedule\n")
    print("Period no.  Start date\t    Interest\t   Principal\tBalance Amount")
    print("-----------------------------------------------------------------------------")
    for entry in self.schedule: 
      each_row = "{:.0f} \t    {}-{}-{}\t  $  {:.2f}\t $  {:.2f}\t $  {:.2f}"
      # print(each_row.format(Period,startDate.year,startDate.month,startDate.day,interest,principal,balance))
      print(each_row.format(entry.period,entry.date.year,entry.date.month,entry.date.day,entry.interest,entry.principal,entry.balance))
    print("\nYou have paid a total interest of $ {:.2f}".format(self.total_interest))
    print("\nYou have successfully returned a principal of : $ {:.2f}".format(self.principal))

