import json
from app import app

def load_categories():
    with open('%s/data/categories.json' % app.root_path, encoding = 'utf-8') as f:
        return json.load(f)

def load_products(categories_id = None):
    with open('%s/data/products.json' % app.root_path, encoding = 'utf-8') as f:
        products = json.load(f)
    if categories_id:
        products = [p for p in products if p['categories_id'] == int(categories_id)]


    return products

if __name__ == '__main__':
    import os
    os.ro