import requests
from lxml import html

print 'URL : '
url = raw_input()
response = requests.get(url)

if (response.status_code == 200):
    print('Request Ok!')
    page = html.fromstring(response.text)
    text = page.cssselect('a.nuEeue.hzdq5d.ME7ew')[0].text
    print text

else:
    print('Request Wrong!')