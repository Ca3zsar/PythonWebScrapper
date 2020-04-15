from bs4 import BeautifulSoup
import requests

URL = "http://pythonjobs.github.io"
page = requests.get(URL)

soup = BeautifulSoup(page.content,"html.parser")
results = soup.find(class_="job_list")
job_elements = soup.find_all("div",class_="job")

for element in job_elements:
    element_title = element.find("h1")
    info_elements = element.find_all("span",class_="info")

    print(f"Title: {element_title.text}")
    print(f"Location: {info_elements[0].text}")
    print(f"Date of publishing: {info_elements[1].text}")
    print(f"Duration: {info_elements[2].text}")
    print(f"Company: {info_elements[3].text}")
    print(f"Apply at: {URL}{element_title.find('a')['href']}",end='\n'*2)