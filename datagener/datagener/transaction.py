# source /home/nontapat/.cache/pypoetry/virtualenvs/datagener-bx0uWqDJ-py3.8/bin/activate
import random
import string
from pathlib import  Path
import argparse
from tqdm import tqdm, trange
from time import sleep


def parse_cli():
    p = argparse.ArgumentParser(description='Transaction data generator')
    p.add_argument('--type', choices=('transaction', 'master'), default='transaction', help='transaction = event data, master = look up table')
    p.add_argument('--n_rec', nargs='?',default=1000, type=int, help='number of records to generate')
    return p.parse_args()

def get_names(n_rec):  
    lineList = [line.rstrip('\n') for line in open("./name_dict/names.txt")]
    name_list = random.choices(lineList, k=n_rec)
    return name_list

def get_emails(name_list):  
    company_name_list = random.choices([line.rstrip('\n') for line in open('./name_dict/company-names.txt')], k=len(name_list))
    surname_list = random.choices(string.ascii_letters, k=len(name_list))
    email_list= list(map(lambda x, y, z: x+ '.' +y + '@mail.' + z + '.co', name_list, surname_list, company_name_list))
    return email_list

def main():
    args = parse_cli()

    if args.type == 'transaction':
        print(f'\ngenerating {args.n_rec} transactional data points ...')
        # for i in trange(100):
        #     sleep(0.03)
        pbar = tqdm(total=100)
        for i in range(10):
            sleep(0.1)
            pbar.update(10)
            
        pbar.close()
    elif args.type == 'master':
        print('establishing a master table ...')

if __name__=='__main__':
    main()
    