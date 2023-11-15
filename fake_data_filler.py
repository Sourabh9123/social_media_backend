from storeapp.models import Category, Customer, Product, OrderItem,Payment
from faker import Faker


fake = Faker()
category = Category.objects.get(id=1)
print(category)
# Generate values for product_price and product_quantity
product_price = fake.pydecimal(min_value=1, max_value=1000, right_digits=2)  # Generates a random decimal with 2 decimal places between 1 and 1000
product_quantity = fake.random_int(min=1, max=100)  # Generates a random integer between 1 and 100

# Create a Product instance
product = Product.objects.create(
    product_name=fake.name(),
    category=category,
    product_img=fake.image_url(),
    product_description=fake.text(),
    product_price=product_price,
    product_quantity=product_quantity
)