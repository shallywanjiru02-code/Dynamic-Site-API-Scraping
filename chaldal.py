import requests
import json
import pandas as pd

def get_json():
    url = "https://catalog.chaldal.com/searchPersonalized"
    payload = json.dumps({
  "apiKey": "e964fc2d51064efa97e94db7c64bf3d044279d4ed0ad4bdd9dce89fecc9156f0",
  "storeId": 1,
  "warehouseId": 8,
  "pageSize": 8000,
  "currentPageIndex": 0,
  "metropolitanAreaId": 1,
  "query": "",
  "productVariantId": -1,
  "bundleId": {
    "case": "None"
  },
  "canSeeOutOfStock": "true",
  "filters": [],
  "maxOutOfStockCount": {
    "case": "Some",
    "fields": [
      5
    ]
  },
  "shouldShowAlternateProductsForAllOutOfStock": {
    "case": "Some",
    "fields": [
      "true"
    ]
  },
  "customerGuid": {
    "case": "None"
  },
  "deliveryAreaId": {
    "case": "None"
  },
  "shouldShowCategoryBasedRecommendations": {
    "case": "None"
  }
})
    headers = {
  'accept': 'application/json',
  'accept-language': 'en-US,en;q=0.9',
  'cache-control': 'no-cache',
  'content-type': 'application/json',
  'origin': 'https://chaldal.com',
  'pragma': 'no-cache',
  'priority': 'u=1, i',
  'referer': 'https://chaldal.com/',
  'sec-ch-ua': '"Google Chrome";v="155", "Chromium";v="155", "Not(A:Brand";v="24"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"Windows"',
  'sec-fetch-dest': 'empty',
  'sec-fetch-mode': 'cors',
  'sec-fetch-site': 'same-site',
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/155.0.0.0 Safari/537.36',
}

    response = requests.request("POST", url, headers=headers, data=payload)
    return response.json()




# we create another function that will convert this json into a csv file or excel we check the data
# we are going to be using json undercore normalize function of pandas in this that wil take the data and return to data frame 
def save_to_csv(data):
    if data:
        df = pd.json_normalize(data)
        df.to_csv("chaldal.csv")


# lets create another function that by this function we are going to get data by calling this function
def main():
    data = get_json()
    save_to_csv(data.get('hits'))
    print('Done')
    
    
# we are going to call the main function
if __name__ == '__main__':
    main()