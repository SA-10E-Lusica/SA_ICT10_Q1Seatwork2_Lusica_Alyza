# ICT 10 Seatwork #2
# Declaring Variables & Identifying Data Types
# Author: Alyza Lusica

# Restaurant name (string)
restaurant_name = "Sea Breeze"

# Owner name (string)
owner_name = "Alyza Lusica"

# Year established (integer)
year_established = 2025

# Popular item price (float)
popular_item_price = 375.00   # Venetian Shrimp with Polenta

# Delivery option (boolean)
has_delivery = True

# Product names (list of strings)
product_names = ["Scallop Sliders", "Seafood Paella", "Crispy Crab Cakes"]

# Business hours (dictionary)
business_hours = {
    "Opening": "9:00 AM", 
    "Closing": "10:00 PM"
}

# Menu prices (dictionary with item-price pairs)
menu_prices = {
    "Venetian Shrimp with Polenta": 375.00,
    "Seafood Paella": 450.00,
    "Scallop Sliders": 200.00,
    "Crispy Crab Cakes": 250.00,
    "Lobster Rolls": 300.00
}

# Common allergens (list of strings)
common_allergens = ["Seafood", "Shellfish", "Dairy"]

# Tax rate (float)
tax_rate = 0.08


# --- Display at least 5 data ---
print("Restaurant Name:", restaurant_name)
print("Owner:", owner_name)
print("Established:", year_established)
print("Popular Item Price: ₱", popular_item_price)
print("Delivery Available:", "Yes" if has_delivery else "No")

print("\nBusiness Hours:", business_hours["Opening"], "to", business_hours["Closing"])
print("Popular Products:", ", ".join(product_names))
print("Allergens:", ", ".join(common_allergens))
print("Tax Rate:", str(tax_rate * 100) + "%")