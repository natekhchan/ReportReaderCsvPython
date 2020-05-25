#!/usr/bin/env python3
#
# Nathan Chan (@natekhchan)
# https://www.ptrace-security.com
#
# report_parser_with_csv_support.py: This script displays the vulnerabilities stored
# in an external CSV report file (e.g. files/vulnerabilities.csv).
#
 
import sys

 
def display_stats(stats):
    output = str(stats['high'])   + ' high ; '
    output+= str(stats['medium']) + ' medium ; '
    output+= str(stats['low'])    + ' low '
    print('\nVulnerability Stats: ' + output)
     
    return
 
 
def is_not_a_client(host):    
    hostid = int(host.split('.')[3])    # Get last byte of the IP
 
    if hostid >= 1 and hostid <= 99:
       return True
    else:
       return False
 
 
def read_report(filename):
    report = []
    
    csv = open(filename, 'r')

    for line in csv.readlines():
       report.append(line.rstrip('\n'))	# Remove newline and add to report
 
    csv.close()
    return report
 
 
def main():
    num = {'high': 0, 'medium': 0, 'low': 0}

    report = read_report('files/vulnerabilities.csv')

    for i in range(0, len(report)):
       (host, cve, severity, description) = report[i].split(',')
 
       if is_not_a_client(host):
          print(host + ' is vulnerable to ' + cve)
     
          if severity == 'High':
               num['high'] += 1
          elif severity == 'Medium':
               num['medium'] += 1
          elif severity == 'Low':
               num['low'] += 1
          else:
               print('Invalid vulnerability ranking!')
 
    display_stats(num)
    sys.exit(0)
 
 
if __name__ == "__main__":
    main()
 
