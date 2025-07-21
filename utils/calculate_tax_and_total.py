def calculate_tax_and_total(price: float, tax_rate: float = 0.08) -> tuple[str, str]:
    tax = round(price * tax_rate, 2)
    total = round(price + tax, 2)
    return f"Tax: ${tax:.2f}", f"Total: ${total:.2f}"
