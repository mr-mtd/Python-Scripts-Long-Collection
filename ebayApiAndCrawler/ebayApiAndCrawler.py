import requests
import xml.etree.ElementTree as ET
import DesktopUI

class EbayAPI:
    def __init__(self, app_id):
        self.app_id = app_id
        self.headers = {
            "X-EBAY-SOA-OPERATION-NAME": "findItemsByKeywords",
            "X-EBAY-SOA-SECURITY-APPNAME": app_id,
            "X-EBAY-SOA-GLOBAL-ID": "EBAY-US",
            "X-EBAY-SOA-RESPONSE-DATA-FORMAT": "XML"
        }
        self.api_url = "https://svcs.ebay.com/services/search/FindingService/v1"

    def search(self, keywords):
        pagination_input = {"entriesPerPage": "10", "pageNumber": "1"}
        item_filter = {"name": "VehicleType", "value": "Motorcycle"}

        response = requests.get(self.api_url, headers=self.headers, params={"keywords": keywords,
                                                                            "paginationInput": pagination_input,
                                                                            "itemFilter": item_filter})
        root = ET.fromstring(response.content)

        results = []
        for item in root.findall(".//{http://www.ebay.com/marketplace/search/v1/services}item"):
            title = item.find("{http://www.ebay.com/marketplace/search/v1/services}title").text
            item_id = item.find("{http://www.ebay.com/marketplace/search/v1/services}itemId").text
            view_item_url = item.find("{http://www.ebay.com/marketplace/search/v1/services}viewItemURL").text
            results.append({"title": title, "item_id": item_id, "view_item_url": view_item_url})

        return results


def main():

   # app_id = "<YOUR_APP_ID_HERE>"
   # ebay_api = EbayAPI(app_id)
   # results = ebay_api.search("motorcycle")
   # for result in results:
   #     print("{result['title']} (Item ID: {result['item_id']}) - View on eBay: {result['view_item_url']}")
    DesktopUI.

if __name__ == "__main__":
    main()
