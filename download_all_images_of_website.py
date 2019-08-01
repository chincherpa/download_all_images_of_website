import re
import requests
from bs4 import BeautifulSoup

site = 'https://dev.to/emmawedekind/using-git-tags-to-version-coding-tutorials-39cc'

response = requests.get(site)

soup = BeautifulSoup(response.text, 'html.parser')
img_tags = soup.find_all('img')

urls = [img['src'] for img in img_tags]


for url in urls:
    print(url)
    # if not url.endswith('jpg'): continue
    filename = re.search(r'/([\w_-]+[.](jpg|gif|png))$', url)
    print(filename)
    try:
        with open(filename.group(1), 'wb') as f:
            if 'http' not in url:
                # sometimes an image source can be relative 
                # if it is provide the base url which also happens 
                # to be the site variable atm. 
                url = '{}{}'.format(site, url)
            response = requests.get(url)
            f.write(response.content)
    except:
        print('geht net')
