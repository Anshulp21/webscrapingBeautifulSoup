import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Set up Chrome driver options
def get_chrome_web_driver(options):
    return webdriver.Chrome("./chromedriver", chrome_options=options)

def get_web_driver_options():
    return webdriver.ChromeOptions()

def set_ignore_certificate_error(options):
    options.add_argument('--ignore-certificate-errors')

def set_browser_as_incognito(options):
    options.add_argument('--incognito')

# Set up pipeline to extract data from webpage
def extract_data(url):
    source = requests.get(url)
    soup = BeautifulSoup(source.text, 'html.parser')
    
    # Extract title
    title = soup.find('title').text
    
    # Extract all links
    links = soup.find_all('a', href=True)
    
    # Extract all images
    images = soup.find_all('img')
    
    # Extract all tables with class 'infobox vevent'
    tables = soup.find_all('table', class_='infobox vevent')
    
    return {
        'title': title,
        'links': links,
        'images': images,
        'tables': tables
    }

# Set up pipeline to extract data from Wikipedia
def extract_wikipedia_data(url):
    source = requests.get(url)
    soup = BeautifulSoup(source.text, 'html.parser')
    
    # Extract title
    title = soup.find('title').text
    
    # Extract all tables with class 'infobox vevent'
    tables = soup.find_all('table', class_='infobox vevent')
    
    # Extract all divs with class 'toc'
    toc = soup.find_all('div', class_='toc')
    
    return {
        'title': title,
        'tables': tables,
        'toc': toc
    }

# Main function
def main():
    url = "https://getpython.wordpress.com/"
    wikipedia_url = "https://en.wikipedia.org/wiki/World_War_II"
    
    # Extract data from webpage
    data = extract_data(url)
    
    # Extract data from Wikipedia
    wikipedia_data = extract_wikipedia_data(wikipedia_url)
    
    # Print extracted data
    print("Title:", data['title'])
    print("Links:")
    for link in data['links']:
        print(link['href'])
    print("Images:")
    for image in data['images']:
        print(image)
    print("Tables:")
    for table in data['tables']:
        print(table.text)
    
    print("\nWikipedia Data:")
    print("Title:", wikipedia_data['title'])
    print("Tables:")
    for table in wikipedia_data['tables']:
        print(table.text)
    print("TOC:")
    for toc in wikipedia_data['toc']:
        print(toc.text)

if __name__ == "__main__":
    main()
