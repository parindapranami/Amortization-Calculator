P = float(input("Enter your principal(loan amount1): "))
r = float(input("Enter the rate of interest per period: "))
n = int(input("Enter the period: "))
compounding = int(input("Enter the compounding (i.e. annual=12,semi annual = 6) :  "))

compounding_span = int (12 / compounding)

def total_interest(schedule):
  interest = 0.0
  for dictionary in schedule:
    interest += float(dictionary['Interest'])
  return interest

def amortization_schedule(P,r,n):
  payment = amortization_payment(P,r,n)
  #need to change these values
  r = r/100 * compounding_span
  
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
  r = r/100 * compounding_span
  
  A = P*(r*((1 + r)**n) / (((1 + r)**n) - 1))
  return A
  
def print_header(P):
  payment = amortization_payment(P,r,n)
  print(" ")
  print("Your monthly Amortization payment is:{:.2f}".format(payment))
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


#calling the first function
print_header(P)