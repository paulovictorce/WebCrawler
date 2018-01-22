import requests
from lxml import html
import os

print 'URL : '
url = raw_input()
print 'Lang : '
lang = raw_input()

if(lang == 'pt'):
    url = url + '?ned=pt-BR_br&hl=pt-BR&gl=BR'
else:
    url = url + '?ned=us&gl=US&hl=en'

print url

response = requests.get(url)
f = open('titles.txt', 'w')

if (response.status_code == 200):
    print('Request Ok!')
    page = html.fromstring(response.text)
    # text = page.cssselect('a.nuEeue.hzdq5d.ME7ew')[0].text
    for a in page.cssselect('a.nuEeue.hzdq5d.ME7ew'):
        f.writelines(a.text_content().encode('utf-8') + os.linesep)
    f.close
else:
    print('Request Wrong!') 