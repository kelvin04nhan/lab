from product import Product

def main():
    n = int(input("Enter the number of products: "))
    products = []

    for i in range(1, n + 1):
        name = input(f"Enter the name of product {i}: ")
        price = float(input(f"Enter the price of product {i}: "))
        quantity = int(input(f"Enter the quantity of product {i}: "))

        product = Product(name, price, quantity)
        products.append(product)

    print("\nProduct Information:")
    for product in products:
        product.output()
        print("-" * 30)

    total_amount = Product.getTotalAmount()
    print(f"\nTotal Amount for all products: {total_amount}")

if __name__ == "__main__":
    main()

