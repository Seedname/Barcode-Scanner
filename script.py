import requests


def search_item(item_id: str) -> dict:
    # API link
    url = f"https://api.upcdatabase.org/product/{item_id}"

    # sending get request and saving the response as response object
    r = requests.get(url=url, headers={"Authorization": "Bearer E13B280796487261E5D32B9DEAF51B30"})

    # extracting data in json format
    data = r.json()

    return data


if __name__ == "__main__":
    # Add the code for the barcode scanner here.
    item_barcode = "720825548692"
    search_item(item_barcode)
