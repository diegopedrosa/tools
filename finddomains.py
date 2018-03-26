import requests
import json
import sys
from time import sleep


def get_zones():
    r = requests.get('https://dns.coffee/api/zones' )
    return json.loads(r.text)['data']['zones']


def get_ns(zone):
    r = requests.get('https://dns.coffee/api/zones/%s' % zone)
    return json.loads(r.text)['data']['nameservers']


def check_dns(ns):
    try:
        r = requests.get('https://dns.coffee/api/nameservers/%s' % str(ns).lower())
        result = json.loads(r.text)['data']
        domains = ('news - %s - %s' % (d['name'], d['firstseen']) for d in result['domains'])
        archive_domains = ('archive - %s - %s - %s' % (d['name'], d['firstseen'], d['lastseen']) for d in result['archive_domains'])

    except Exception as e:
        if r.status_code == 429:
            print('    - http status %s '% r.status_code)
            sleep(2)
            domains, archive_domains = check_dns(ns)

    return domains,archive_domains


def show_dns(*args):

    ns = args[0]
    domains, archive_domains = check_dns(ns.replace('\n', ' ').replace('\r', '').replace(' ', ''))

    if len(args) > 2:
        value = args[2]
        print("\n    - ".join([s for s in domains if value in str(s).lower()]))
        print("\n    - ".join([s for s in archive_domains if value in str(s).lower()]))
    else:
        print("\n    - ".join([s for s in domains]))
        print("\n    - ".join([s for s in archive_domains]))


if __name__ == '__main__':
    with open('nameservers.txt','r') as nameservers:
        for ns in nameservers:
            try:
                print('  * %s' % ns)
                show_dns(ns, *sys.argv)
            except Exception as e:
                print('    Error: %s' % e)
                pass

    for z in get_zones():
        print(z['zone'])
        try:
            for ns in get_ns(z['zone']):
                print('  * %s'%ns['name'])
                show_dns(ns['name'],*sys.argv)
        except Exception as e:
            print('    Error: %s' % e)
            pass



