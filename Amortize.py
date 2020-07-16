#this file contains all the commands required for Command #line options

import argparse
from Amortization import *


parser = argparse.ArgumentParser(description = 'Calculate amortization value and print the schedule')
parser.add_argument('-P','--P',type = float,help = 'Principal amount') 
parser.add_argument('-r','--r',type = float,help = 'rate of interest per period') 
parser.add_argument('-n','--n',type = int,help = 'Tenure') 
args = parser.parse_args()

if __name__ == "__main__":
  args.r = args.r / 1200
  args.n = args.n * 12
  print_schedule(args.P,args.r,args.n)
  