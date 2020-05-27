#!/usr/bin/env python3
#
# Nathan Chan (@natekhchan)
# https://www.ptrace-security.com
#
# email_collector_with_subprocess.py: This script parses an HTML file using the well-known
# egrep utility and extracts all the emails in the document.
#

import os
import io
import sys
import subprocess


def is_html_file(filename):
    if not os.path.isfile(filename):
        return False        # filename is not a file
        
    ext = filename.split('.')[-1]
    if ext == 'htm' or ext == 'html':
        return True         # filename is an HTML file
    else:
        return False        # filename is not an HTML file


def extract_emails_from(filename):
    emails = []

    proc = subprocess.Popen(['egrep', "-o", r'[a-zA-Z0-9.-]+@[a-zA-Z0-9.-]+.[a-zA-Z0-9.-]+.', 'files/faculty.html'], stdout=subprocess.PIPE)
    proc2 = subprocess.Popen(['uniq'], stdin=proc.stdout, stdout=subprocess.PIPE)
    for match in io.TextIOWrapper(proc2.stdout, encoding="utf-8"):
        # Remove %3C and %3E\n from each match
        email = match.rstrip("\n")[0:-1]
        replacement1 = email.replace("3C", "")
        replacement2 = replacement1.replace("%3E", "")
        emails.append(replacement2)
    emails = list(dict.fromkeys(emails))  # de-duplicate e-mail lines in list
    
    return emails


def display(emails):
    for email in emails:		
        print(email)
    print('\n' + str(len(emails)) + ' e-mail addresses found.')


def usage(scriptname):
    print("Usage  : %s <html_file>" % (scriptname))
    print("Example: %s files/faculty.html"  % (scriptname))


def main():

    if len(sys.argv) != 2:
        usage(sys.argv[0])
        sys.exit(1)

    filename = sys.argv[1]
    if is_html_file(filename):
        emails = extract_emails_from(filename)
        display(emails)
    else:
        print(filename + ' is not an HTML file.')

    sys.exit(0)


if __name__ == "__main__":
    main()
