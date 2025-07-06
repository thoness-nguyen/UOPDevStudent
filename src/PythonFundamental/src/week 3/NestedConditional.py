def cust_selection(code):
    # Base item prices
    Item1 = 30
    Item2 = 40
    Item3 = 50

    # First level: decide package “size”
    if 1 <= code <= 3:
        # Nested: single‐item packages
        if code == 1:
            return f"You selected Package 1 (Item A). Total: {Item1}"
        elif code == 2:
            return f"You selected Package 2 (Item B). Total: {Item2}"
        else:  # code == 3
            return f"You selected Package 3 (Item C). Total: {Item3}"

    elif 4 <= code <= 6:
        # Nested: two‐item bundles (10% discount)
        if code == 4:
            subtotal = Item1 + Item2
        elif code == 5:
            subtotal = Item1 + Item3
        else:  # code == 6
            subtotal = Item2 + Item3
        total = subtotal * 0.9  # apply 10% off
        # Map code to labels
        labels = {4: "A+B", 5: "A+C", 6: "B+C"}[code]
        return f"You selected Package {code} ({labels}) with 10% off. Total: {total}"

    elif code == 7:
        # Nested: three‐item bundle (20% discount)
        subtotal = Item1 + Item2 + Item3
        total = subtotal * 0.8  # apply 20% off
        return f"You selected Package 7 (A+B+C) with 20% off. Total: {total}"

    else:
        # Invalid code branch
        return "Invalid package code. Please choose 1–7."

# Example usage
print(cust_selection(1))   # single A
print(cust_selection(4))   # A+B bundle
print(cust_selection(6))   # B+C bundle
print(cust_selection(7))   # triple bundle
print(cust_selection(9))   # invalid
