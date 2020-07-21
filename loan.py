class Loan:

  def __init__(self,P,r,n):
    self.principal = P
    self.rate = r 
    self.numberOfPeriods = n 
    self.payment = self.principal*(self.rate*((1 + self.rate)**self.numberOfPeriods) / (((1 + self.rate)**self.numberOfPeriods) - 1))
    assert self.payment > 0,"Monthly Amortization payment cannot be negative"
    self.schedule = self.amortization_schedule()
    
  def amortization_schedule(self):
    amount = self.principal
    period = 0
    balance =   amount
    schedule = []
    total_interest = 0
    while period < self.numberOfPeriods:
      monthly_interest = balance * self.rate
      assert monthly_interest > 0,"Interest should be a positive number"
      amount =  self.payment - monthly_interest
      assert amount > 0,"Amount should be a positive number"
      balance = balance - amount
      #assert balance > 0,"Balance should be a positive number"
      period+=1
      total_interest += monthly_interest
      schedule_dict = dict(Period=period,Interest=monthly_interest,Principal=amount,Balance=balance)
      schedule.append(schedule_dict) 
    self.total_interest = total_interest
    assert self.total_interest > 0,"""Total interest can't be negative"""
    return schedule

  def print_schedule(self):
    print(" ")
    print("Your monthly Amortization payment is: $ {:.2f}".format(self.payment))
    print(" ")
    print("Following is the Amortization Schedule\n")
    print("Period no.\t  Interest\t Principal\tBalance Amount")
    print("--------------------------------------------------------------------------")
    for entry in self.schedule: 
      interest = entry["Interest"]
      principal = entry["Principal"]
      Period = entry["Period"]
      balance = entry["Balance"]
      each_row = "{:.0f}\t\t $  {:.2f}\t $  {:.2f}\t $  {:.2f}"
      print(each_row.format(Period,interest,principal,balance))
    print("\nYou have paid a total interest of $ {:.2f}".format(self.total_interest))
    print("\nYou have successfully returned a principal of : $ {:.2f}".format(self.principal))



