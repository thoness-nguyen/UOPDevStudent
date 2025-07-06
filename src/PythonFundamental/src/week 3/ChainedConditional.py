"""
A chained conditional evaluates one test after another in a single, top-level sequence of if → elif → else branches. 
Each condition is mutually exclusive, and execution stops as soon as one branch is true. 
In contrast, a nested conditional places an if (or elif) inside another branch, creating multiple levels of indentation.

"""
### Chained Conditional Example ###

def cust_selection(code):
    # Define base prices for each individual item
    Item1 = 30
    Item2 = 40
    Item3 = 50

    # Single‐item packages (no discount)
    # Each branch checks the incoming `code` parameter
    # and returns the corresponding package label and cost.
    if code == 1:
        return f"You selected Package 1 (Item A). Total: {Item1:.2f}"
    elif code == 2:
        return f"You selected Package 2 (Item B). Total: {Item2:.2f}"
    elif code == 3:
        return f"You selected Package 3 (Item C). Total: {Item3:.2f}"
    elif code == 4:
        # Two‐item bundle (10% discount)
        subtotal = Item1 + Item2
        total = subtotal * 0.9  # apply 10% off
        return f"You selected Package 4 (A+B) with 10% off. Total: {total:.2f}"
    else:
        return "Invalid package code. Please choose 1–3."
    

# Example usage

print(cust_selection(1))  # single A
print(cust_selection(4))  # A+B bundle
print(cust_selection(9))  # invalid