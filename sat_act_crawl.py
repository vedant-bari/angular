import requests
from lxml import html
#url = 'https://nces.ed.gov/collegenavigator/?id=178369#general'
#url = 'https://nces.ed.gov/collegenavigator/?id=144892#general'
url= 'https://nces.ed.gov/collegenavigator/?id=178369#general'
#url = 'https://nces.ed.gov/collegenavigator/?id=102058#general'
pageContent = requests.get(url)
tree = html.fromstring(pageContent.content)
