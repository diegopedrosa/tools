import requests
import json
import sys


def get_zones():
    r = requests.get('https://dns.coffee/api/zones' )
    return (json.loads(r.text)['data']['zones'])

def get_ns(zone):
    r = requests.get('https://dns.coffee/api/zones/%s' % zone)
    return (json.loads(r.text)['data']['nameservers'])


def check_dns(ns):
    r = requests.get('https://dns.coffee/api/nameservers/%s' % ns)
    result = json.loads(r.text)['data']
    domains = ('news - %s - %s' % (d['name'], d['firstseen']) for d in result['domains'])
    archive_domains = ('archive - %s - %s - %s' % (d['name'], d['firstseen'], d['lastseen']) for d in result['archive_domains'])
    return domains,archive_domains


def show_dns(*args):
    ns = args[0]
    domains, archive_domains = check_dns(ns)
    if len(args) > 2:
        value = args[2]
        print("\n".join([s for s in domains if value in str(s).lower()]))
        print("\n".join([s for s in archive_domains if value in str(s).lower()]))
    else:
        print("\n".join([s for s in domains]))
        print("\n".join([s for s in archive_domains]))


if __name__ == '__main__':

    for z in get_zones():
        print(z['zone'])
        try:
            for ns in get_ns(z['zone']):
                print(ns['name'])
        except:
            pass

    '''


    try:
        show_dns('NS1.ANONS.IO',*sys.argv)
    except Exception as e:
        show_dns('NS2.ANONS.IO',*sys.argv)
    try:
        show_dns('NS75.DOMAINCONTROL.COM',*sys.argv)
    except Exception as e:
        show_dns('NS76.DOMAINCONTROL.COM',*sys.argv)
    try:
        show_dns('CARTER.NS.CLOUDFLARE.COM',*sys.argv)
    except Exception as e:
        show_dns('TINA.NS.CLOUDFLARE.COM',*sys.argv)
'''
