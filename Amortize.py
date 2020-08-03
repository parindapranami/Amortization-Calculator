#this file contains all the commands required for Command #line options
from datetime import date
import argparse
from loan import *
from dateutil.relativedelta import relativedelta


parser = argparse.ArgumentParser(description = 'Calculate amortization value and print the schedule')
parser.add_argument('-P','--P',type = float,help = 'Principal amount') 
parser.add_argument('-r','--r',type = float,help = 'rate of interest per period') 
parser.add_argument('-n','--n',type = int,help = 'Tenure') 
parser.add_argument('-d','--d',help = 'Start Date of monthly payment')
args = parser.parse_args()


if __name__ == "__main__":
  if args.d:
    inputDate =  datetime.strptime(args.d, "%Y-%m-%d")
    inputDate = date(inputDate.year , inputDate.month , 1)
  else :
    inputDate = date.today() + relativedelta(months=1)
    inputDate = inputDate.replace(day = 1)
  args.d = inputDate
  loan = Loan(args.P,args.r/1200,args.n*12,args.d) 
  print(loan.print_schedule())
 