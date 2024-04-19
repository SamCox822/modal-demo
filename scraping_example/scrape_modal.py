import modal
import requests
from bs4 import BeautifulSoup
import time
from scrape import get_wikipedia_links, write_headers_to_file

# Create a Modal image with the dependencies we need
# this tells modal what dependencies we need to run the function
wiki_image = (modal.Image.
              debian_slim(python_version="3.12")
            .pip_install("requests", "beautifulsoup4"))
stub = modal.Stub(name="wikipedia-header-scraper")


@stub.local_entrypoint() #replaces the if __name__ == "__main__": we are used to
def main():
    start_time = time.time()
    with open(f"all_headers.csv", 'w') as f:
        f.write("page,headers\n")
    wikipedia_links = get_wikipedia_links()
    for headers, wikilink in get_wikipedia_headers.map(wikipedia_links):
        write_headers_to_file(headers, wikilink)
    end_time = time.time()
    print(f"Finished! It took {round(end_time - start_time,2)}! :)")


#stubs have lots of paramters,Image, gpu, container_idle_timeout, allow_concurrent_inputs, secret
@stub.function(image=wiki_image) # this changes the function to a Modal function object
#this lets us use their parallelization features:)
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
        print (f"Got headers for {url}")
        return headers, url
    except Exception as e:
        print(f"An error occurred: {e}")



