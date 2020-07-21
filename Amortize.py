#this file contains all the commands required for Command #line options

import argparse
from loan import *


parser = argparse.ArgumentParser(description = 'Calculate amortization value and print the schedule')
parser.add_argument('-P','--P',type = float,help = 'Principal amount') 
parser.add_argument('-r','--r',type = float,help = 'rate of interest per period') 
parser.add_argument('-n','--n',type = int,help = 'Tenure') 
args = parser.parse_args()
assert args.P > 0,"Principal should be a positive non zero number"
assert args.r > 0,"Rate should be a positive non zero number"
assert args.n > 0,"Tenure should be a positive non zero number"

if __name__ == "__main__":
  loan = Loan(args.P,args.r/1200,args.n*12) 
  print(loan.print_schedule())
  