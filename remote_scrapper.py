from bs4 import BeautifulSoup
import requests


def Display_Categories(categories_text):
    print("JOB CATEGORIES TO CHOOSE FROM: ")
    for el in categories_text:
        print(f"*{el}")

###############################################

def Choose_Category(categories):
    choice = input("Enter your choice: ")
    try:
        index = [el.lower() for el in categories].index(choice.lower())
        return index
    except ValueError:
        return Choose_Category(categories)
    
################################################

def first_stage():
    URL = "https://remote.co/remote-jobs"
    main_page = requests.get(URL)
    main_soup = BeautifulSoup(main_page.content,"html.parser")

    categories_results = main_soup.find("div",class_="col-12")
    categories = categories_results.find_all("a",class_="rounded-sm mx-1 mb-1 btn-category d-inline-block")
    categories_text = [el.text for el in categories]
    categories_link = [el["href"] for el in categories]

    Display_Categories(categories_text)
    choice = Choose_Category(categories_text) 

    NEW_URL = URL[:17]+categories_link[choice]
    return NEW_URL

def second_stage(URL):
    base_url = "https://remote.co"
    page = requests.get(URL)
    soup = BeautifulSoup(page.content,"html.parser")

    results = soup.find_all("div",class_="card-body p-0")
    correct_results = results[1]

    jobs = correct_results.find_all("a",class_="card m-0 border-left-0 border-right-0 border-top-0 border-bottom")
    for job in jobs:

        job_title = job.find("span",class_="font-weight-bold larger")    
        job_publishing = job.find("date")

        job_bussiness = job.find("p",class_="m-0 text-secondary")
        job_b_noS = job_bussiness.find(text=True)
        job_link = job["href"]

        print(job_title.text.strip())
        try:
            bussiness_index = job_b_noS.index("|")
            print(job_b_noS[:bussiness_index].strip())
        except:
            print(job_b_noS.strip())
        print(job_publishing.text.strip())
        print(f"Apply at: {base_url+job_link}")
        print("--------------------------------")




URL = first_stage()
second_stage(URL)  

