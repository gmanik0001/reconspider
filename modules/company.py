from config import clearbit_api
import requests
import json
import clearbit
import os
clearbit.key=clearbit_api
def comDetail(domain):
    try:
        company=clearbit.Company.find(domain=domain,stream=True)
        if company != None:
            print "\n-------------------------------------------------\n"
            print "[+] Gathering Company Information from [clearbit]...\n"
            print "Location-------------> "+str(company['name'])
            print "Domain Name----------> "+str(company['domain'])
            print "Location-------------> "+str(company['location'])
            print "Email Address--------> "+str(company['site']['emailAddresses'])
            print "Number of Employees--> "+str(company['metrics']['employees'])
            print "Contact Number-------> "+str(company['phone'])
            print "Description----------> "+str(company['description'])

        else:
            print "No information"
    except:
        print "Try Again"
