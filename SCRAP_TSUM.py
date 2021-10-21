import requests
import json

headers = {
            "accept": "application/json, text/plain, */*",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36"
}


def get_page(url):
    s = requests.Session()
    response = s.get(url=url, headers=headers)

    with open("index_tsum", 'w', encoding='utf8') as file:
        file.write(response.text)


def get_json(url):
    s = requests.Session()
    response = s.get(url=url, headers=headers)

    data = response.json()
    for d in data:
        print(d["skuList"][0]['price_original'])

    with open("result_tsum", 'w', encoding='utf8') as file:
        json.dump(response.json(), file, indent=4, ensure_ascii=False)


def main():
    get_page(url="https://www.tsum.ru/brand/muzhskoe-2408/stone_island.html")
    get_json(url="https://api.tsum.ru/v2/catalog/search?section=18327&brand=181113&enable_brand_filter_gender=1&strategy=advanced,zero_queries_predictor")


if __name__ == "__main__":
    main()
