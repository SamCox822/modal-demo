import requests
from bs4 import BeautifulSoup
import time
import os

def get_wikipedia_headers(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
        
        #get headers
        headers = []
        for i in range(1, 7): 
            for header in soup.find_all(f'h{i}'):
                headers.append(header.text.strip())
        return headers
    except Exception as e:
        print(f"An error occurred: {e}")

def get_wikipedia_links():
    #get list of wikipedia pages
    file_path = os.path.join(os.path.dirname(__file__), "list_of_wikipeda_pages.txt")
    with open(file_path, 'r') as f:
        pages = f.readlines()
        pages = [page.strip().replace('"', '') for page in pages]
    return pages

def write_headers_to_file(headers, page):
    with open(os.path.join(os.path.dirname(__file__),"all_headers.csv"), 'a') as f:
        headers = str(headers).replace(",", "")
        f.write(f"{page},{headers}\n")
        
def remove_if_failed(page, file_path):
    with open(file_path, 'r') as f:
        pages = f.readlines()
        pages = [page.strip() for page in pages]
        if page in pages:
            pages.remove(page)
    with open(file_path, 'w') as f:
        for page in pages:
            f.write(f"{page}\n")

def main():
    start_time = time.time()
    with open(f"all_headers.csv", 'w') as f:
        f.write("page,headers\n")
    # get a list of wikipedia urls
    pages = get_wikipedia_links()
    for page in pages:
        # get headers from each page
        headers = get_wikipedia_headers(page)
        # write headers to file
        write_headers_to_file(headers, page)
    end_time = time.time()
    print(f"I'm getting old just waiting on this to run! It took {round(end_time - start_time,2)}! :(")

if __name__ == "__main__":
    main()
    

