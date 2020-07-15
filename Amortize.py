#this file contains all the commands required for Command #line options

import argparse
from Amortization import *


parser = argparse.ArgumentParser(description = 'Calculate amortization value and print the schedule')
parser.add_argument('-P','--P',type = float,help = 'Principal amount') 
parser.add_argument('-r','--r',type = float,help = 'Annual rate of interest') 
parser.add_argument('-n','--n',type = int,help = 'Tenure in years') 
args = parser.parse_args()

if __name__ == "__main__":
  print_header(args.P,args.r,args.n)
  