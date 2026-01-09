import requests 
import sys 
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
subdomains_path = os.path.join(script_dir, "subdomains.txt")

sub_list = open(subdomains_path).read() 
subdoms = sub_list.splitlines()

# target = input("Enter the target domain (e.g. example.com, example.org, etc.): ")

for sub in subdoms:
    sub_domains = f"http://{sub}.{sys.argv[1]}" 

    try:
        requests.get(sub_domains)
        print("Valid domain: ",sub_domains)
    
    except requests.ConnectionError: 
        pass
    
    else:
        print("Valid domain: ",sub_domains)   