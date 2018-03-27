import requests
import json
import os
import sys


def findgithub(querystring):
    headers = {'Accept': 'application/vnd.github.preview',
               'Authorization':'token %s' % os.environ['token']}

    params = {'q':querystring,
              'sorted':'indexed'}
    r = requests.get('https://api.github.com/search/code',params=params,headers=headers)
    items = json.loads(r.text)['items']

    for item in items:
        print('%s - %s - %s' % (item['name'],item['html_url'],item['repository']['full_name']))


if __name__ == '__main__':
    total = len(sys.argv)
    if total <= 1:
        print('Digite um ip ou passe o nome e o caminho do arquivo com uma lista de ips.\n '
              'Exemplo: \n  - findgithub poker')
    else:
        if os.path.isfile(sys.argv[1]):
            print('Analisando...')
            findgithub(sys.argv[1])
        else:
            findgithub(sys.argv[1])
