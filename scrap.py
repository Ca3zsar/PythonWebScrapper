import requests
import pprint
from bs4 import BeautifulSoup

URL = 'https://www.monster.com/jobs/search/?q=Software-Developer&where=Australia'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')
results = soup.find(id="ResultsContainer")
job_elements = results.find_all("section",class_="card-content")
python_jobs = results.find_all("h2",string=lambda text:"python" in text.lower())

for element in job_elements:

    title_element = element.find("h2",class_="title")
    company_element = element.find("div",class_="company")
    location_element = element.find("div",class_="location")

    if None in (title_element,company_element,location_element):
        continue

    link_element = element.find('a')['href']

    print(title_element.text.strip())
    print(company_element.text.strip())
    print(location_element.text.strip())
    print(f"Apply here: {link_element}",end='\n'*2)

