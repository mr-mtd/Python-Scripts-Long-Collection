import requests
from bs4 import BeautifulSoup

class ItemScraper:
    def __init__(self, url, item_class, price_class):
        self.url = url
        self.item_class = item_class
        self.price_class = price_class

    def scrape(self):
        # Send a GET request to the webpage and store the HTML response
        response = requests.get(self.url)

        # Parse the HTML response with BeautifulSoup
        soup = BeautifulSoup(response.text, "html.parser")

        # Find all elements on the page with the specified class
        items = soup.find_all(class_=self.item_class)

        # Loop through the items and extract the price and description
        for item in items:
            price = item.find(class_=self.price_class).text
            print("Price: {price}\n")

if __name__ == "__main__":
    # Define the URL and classes for the webpage to scrape
    url = "https://www.ebay.com/sch/i.html?_from=R40&_trksid=m570.l1313&_nkw=zelda&_sacat=0"
    item_class = "s-item__details clearfix".split() # Split the string into a list of classes
    price_class = "s-item__price"

    # Create a new instance of the ItemScraper class and run the scrape method
    scraper = ItemScraper(url, item_class, price_class)
    scraper.scrape()
    