# source /home/nontapat/.cache/pypoetry/virtualenvs/datagener-bx0uWqDJ-py3.8/bin/activate
import random
import string

def get_names(n_rec):
    lineList = [line.rstrip('\n') for line in open('/home/nontapat/Documents/my packages/datagener/name_dict/names.txt')]
    name_list = random.choices(lineList, k=n_rec)
    return name_list

def get_emails(name_list):
    company_name_list = random.choices([line.rstrip('\n') for line in open('/home/nontapat/Documents/my packages/datagener/name_dict/company-names.txt')], k=len(name_list))
    surname_list = random.choices(string.ascii_letters, k=len(name_list))
    email_list= list(map(lambda x, y, z: x+ '.' +y + '@mail.' + z + '.co', name_list, surname_list, company_name_list))
    return email_list

if __name__=='__main__':
    print(get_names(10))