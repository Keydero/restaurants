from datetime import datetime


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
