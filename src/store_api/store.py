from datetime import datetime


def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))


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
