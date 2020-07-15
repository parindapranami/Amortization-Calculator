#this file contains just the functions

def total_interest(schedule):
  interest = 0.0
  for dictionary in schedule:
    interest += float(dictionary['Interest'])
  return interest

def amortization_schedule(P,r,n):
  payment = amortization_payment(P,r,n)
  #need to change these values
  r = r/1200
  n = n*12
  month = 0
  balance = P
  schedule = []
  while month < n:
    monthly_interest = balance * r
    P =  payment - monthly_interest
    balance = balance - P
    month+=1
    schedule_dict = dict(Month=month,Interest=monthly_interest,Principal=P,Balance=balance)
    schedule.append(schedule_dict) 
  return schedule

def amortization_payment(P,r,n):
  r=r/1200
  n=n*12
  A = P*(r*((1 + r)**n) / (((1 + r)**n) - 1))
  return A
  
def print_header(P,r,n):
  payment = amortization_payment(P,r,n)
  print(" ")
  print("Your monthly Amortization payment is: $ {:.2f}".format(payment))
  print(" ")
  print("Following is the Amortization Schedule\n")
  print("Month no.\t  Interest\t Principal\tBalance Amount")
  print("--------------------------------------------------------------------------")
  final_schedule = amortization_schedule(P,r,n)
  for entry in final_schedule:
    interest = entry["Interest"]
    principal = entry["Principal"]
    month = entry["Month"]
    balance = entry["Balance"]
    each_row = "{:.0f}\t\t $  {:.2f}\t $  {:.2f}\t $  {:.2f}"
    print(each_row.format(month,interest,principal,balance))
  
  final_interest = total_interest(final_schedule)
  print("\nYou have paid a total interest of $ {:.2f}".format(final_interest))
  print("\nYou have successfully returned a principal of : $ {:.2f}".format(P))

#for non-CLI code
#calling the first function 
#print_header(P)

  
