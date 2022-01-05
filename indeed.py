import requests
page = requests.get('https://ng.indeed.com/?r=us')
page.status_code
page.content
