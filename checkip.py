__author__ = "Diego Pedrosa"
__copyright__ = "MIT"
import requests
import json
import sys
import os
from ipaddress import ip_address


def check_ip(ip):
    url = "http://freegeoip.net/json/"
    try:
        ip_address(ip)
    except Exception as e:
        print("O valor %s não é um ip. Erro %s" % (ip, e))
        sys.exit(2)

    r = requests.get('%s%s' % (url, ip))
    result = json.loads(r.text.replace('\n', ' ').replace('\r', '').replace(' ', ''))
    return '%s - %s - %s - %s' % (result['ip'], result['country_name'], result['region_code'], result['city'])


def check_file(file):
    result = []
    with open(file, 'r') as ips:
        for i in ips:
            r = check_ip(i)
            result.append(r)
    return result


def show(result):
    if isinstance(result, list):
        print(*result, sep='\n')
    else:
        print(result)


if __name__ == '__main__':
    total = len(sys.argv)
    if total <= 1:
        print('Digite um ip ou passe o nome e o caminho do arquivo com uma lista de ips.\n '
              'Exemplos: \n  - checkip x.x.x.x \n  - checkip c:\\temp\ips.txt')
    else:
        if os.path.isfile(sys.argv[1]):
            print('Analisando...')
            show(check_file(sys.argv[1]))
        else:
            show(check_ip(sys.argv[1]))

