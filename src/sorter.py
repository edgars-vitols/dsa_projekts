from typing import List
from product import Product 

def quick_sort(products: List[Product], key: str, reverse: bool = False) -> None:
  
    _quick_sort_recursive(products, 0, len(products) - 1, key, reverse)

def _quick_sort_recursive(products: List[Product], low: int, high: int, key: str, reverse: bool):
   
    if low < high:
        pi = _partition(products, low, high, key, reverse)
        _quick_sort_recursive(products, low, pi - 1, key, reverse)
        _quick_sort_recursive(products, pi + 1, high, key, reverse)

def _partition(products: List[Product], low: int, high: int, key: str, reverse: bool) -> int:
   
    pivot = getattr(products[high], key) 
    i = low - 1

    for j in range(low, high):
        current_value = getattr(products[j], key)

        if (not reverse and current_value <= pivot) or \
           (reverse and current_value >= pivot):
            i += 1
            products[i], products[j] = products[j], products[i] 

    products[i + 1], products[high] = products[high], products[i + 1]
    return i + 1

if __name__ == "__main__":
    
    from product import Product
    test_products = [
        Product("LISABO Galds", 149.00, "link1"),
        Product("ADDE Krēsls", 12.99, "link2"),
        Product("KALLAX Plaukts", 29.99, "link3"),
        Product("MALM Gulta", 299.00, "link4"),
        Product("NORDMÄRKE Uzlāde", 9.99, "link5"),
        Product("ÄPPLARÖ sols", 79.50, "link6"),
        Product("BERGMUND Krēsls", 45.00, "link7")
    ]

    print("Oriģinālais saraksts:")
    for p in test_products:
        print(p)

    print("\n--- Kārtošana pēc cenas (aug.): ---")
    products_by_price = list(test_products)
    quick_sort(products_by_price, key='cena')
    for p in products_by_price:
        print(p)

    print("\n--- Kārtošana pēc cenas (dil.): ---")
    products_by_price_rev = list(test_products)
    quick_sort(products_by_price_rev, key='cena', reverse=True)
    for p in products_by_price_rev:
        print(p)

    print("\n--- Kārtošana pēc nosaukuma (A-Z): ---")
    products_by_name = list(test_products)
    quick_sort(products_by_name, key='nosaukums')
    for p in products_by_name:
        print(p)

    print("\n--- Kārtošana pēc nosaukuma (Z-A): ---")
    products_by_name_rev = list(test_products)
    quick_sort(products_by_name_rev, key='nosaukums', reverse=True)
    for p in products_by_name_rev:
        print(p)
