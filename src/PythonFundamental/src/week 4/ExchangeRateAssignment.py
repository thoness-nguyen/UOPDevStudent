"""
Business Logic: Exchange Rate Calculation
This module provides a function to calculate the total amount in exchange based on a given amount and quantity from different currency codes.
It includes error handling for invalid exchange rates.
"""

def billing_amount(amount: float, quantity: int, currencyCode: int) -> float:
    if quantity <= 0:
        raise ValueError("Quantity must be greater than zero.")

    total_amount = amount * quantity

    if total_amount < 0:
        raise ValueError("Total amount cannot be negative.")

    return exchange_rate(total_amount, currencyCode)

def exchange_rate(amount: float, currencyCode: int) -> float:
    # Create a dictionary to hold exchange rates for different currencies
    exchange_rates = {
        1: {"rate": 1.0, "curName": "USD"},        # USD to USD
        2: {"rate": 0.85, "curName": "EUR"},       # USD to EUR
        3: {"rate": 0.75, "curName": "GBP"},       # USD to GBP
        4: {"rate": 24200.12, "curName": "VND"}    # USD to Vietnamese Dong
    }

    # Check if the currencyCode exists in the exchange_rates dictionary
    if currencyCode not in exchange_rates:
        raise ValueError("Invalid currency code.")

    converted_amount = exchange_rates[currencyCode]["rate"] * amount
    return converted_amount

# Example usage
total = billing_amount(100, 2, 1)  # USD
print(f"Total amount in USD: {total}")

total = billing_amount(100, 2, 2)  # EUR
print(f"Total amount in EUR: {total}")

total = billing_amount(100, 2, 3)  # GBP
print(f"Total amount in GBP: {total}")

total = billing_amount(100, 2, 4)  # Vietnamese Dong
print(f"Total amount in Vietnamese Dong: {total}")
