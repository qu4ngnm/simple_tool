# TOol add prefix https:// before the url to add to scope in Burp Suite
import argparse

parser = argparse.ArgumentParser(description='Example argument parser')
parser.add_argument('--input_file','-i', help='path to input file')
parser.add_argument('--output-file', '-o', default='output.txt', help='path to output file')

args = parser.parse_args()

url_list = []

def add_prefix(url):
    url = url.replace('\n', '')
    url = 'https://' + url + '/'
    return url

def read_file(file):
    with open(file, 'r') as f:
        for url in f:
            url = add_prefix(url)
            url_list.append(url)


def write_file(ofile):
    with open(ofile, 'w') as f:
        for url in url_list:
            f.write(url + '\n')


read_file(args.input_file)
write_file(args.output_file)