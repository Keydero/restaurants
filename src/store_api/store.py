from connexion import request

stores = [
    {
        "name": "WoodyPlanet",
        "items": [
            {
                "name": "Table",
                "price": 79.99
            }
        ],
    },
    {
        "name": "Talem",
        "items": [
            {
                "name": "Notebook",
                "price": 650.99
            }
        ]
    }
]


def list():
    return {"stores": stores}


def create():
    store = request.get_json()
    new_store = {"name": store["name"], "items": []}
    stores.append(new_store)
    return new_store, 201


def create_item(name):
    item = request.get_json()
    for store in stores:
        if store["name"] == name:
            new_item = {"name": item["name"], "price": item["price"]}
            store["items"].append(new_item)
            return new_item
    return {"error": "Store not Found"}, 404
