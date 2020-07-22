class Loan:

  def __init__(self,P,r,n):
    self.principal = P
    assert self.principal > 0,"Principal can't be negative"
    self.rate = r 
    assert self.rate > 0,"Rate of Interest can't be negative"
    self.numberOfPeriods = n 
    assert self.numberOfPeriods > 0,"Tenure can't be negative"
    self.payment = self.principal*(self.rate*((1 + self.rate)**self.numberOfPeriods) / (((1 + self.rate)**self.numberOfPeriods) - 1))
    self.schedule = self.amortization_schedule()
    
  def amortization_schedule(self):
    amount = self.principal
    period = 0
    balance =   amount
    schedule = []
    total_interest = 0
    while period < self.numberOfPeriods:
      monthly_interest = balance * self.rate
      amount =  self.payment - monthly_interest
      if balance < amount:
        print("error")
      balance = balance - amount
      period+=1
      total_interest += monthly_interest
      schedule_dict = dict(Period=period,Interest=monthly_interest,Principal=amount,Balance=balance)
      schedule.append(schedule_dict) 
    self.total_interest = total_interest
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



