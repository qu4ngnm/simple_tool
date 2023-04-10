#Tool check active subdomain from amass result

from concurrent.futures import ThreadPoolExecutor
import requests
from requests.exceptions import ConnectionError
import argparse

parser = argparse.ArgumentParser(description='Example argument parser')
parser.add_argument('--input_file','-i', help='path to input file')
parser.add_argument('--output-file', '-o', default='output.txt', help='path to output file')

args = parser.parse_args()

domain_list = []
active_domain = []
def read_file(file):
    with open(file, 'r') as f:
        for url in f:
            url = url.replace('\n','')
            domain_list.append(url)

def validate_existence(domain):
        try:
            response = requests.get(domain, timeout=10)
        except ConnectionError:
            print(f'Domain {domain} [is dead]')
        else:
            print(f'Domain {domain} [is active]')
            active_domain.append(domain)

def write_file():
    with open(args.output_file, 'w') as f:
        for url in active_domain:
            f.write(url + '\n')


read_file(args.input_file)
with ThreadPoolExecutor() as executor:
    executor.map(validate_existence, domain_list)
write_file()