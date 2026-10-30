# PROGRAM: Item
# PURPOSE: To manage inventory items.
# INPUT: Item details (ID, name, price, quantity).
# PROCESS: Initializes, edits, updates, and retrieves item information.
# OUTPUT: Displays item details.
# HONOR CODE: On my honor, as an Aggie, I have neither given nor received unauthorized aid on this academic work.

class Item:
    """A class to represent an inventory item."""

    def __init__(self, item_id, name, price, quantity_on_hand):
        self.item_id = item_id
        self.name = name
        self.price = price
        self.quantity_on_hand = quantity_on_hand

    def edit_item(self, name=None, price=None, quantity_on_hand=None):
        """Edits item details."""
        if name:
            self.name = name
        if price is not None:
            self.validate_price(price)
            self.price = price
        if quantity_on_hand is not None:
            self.validate_quantity(quantity_on_hand)
            self.quantity_on_hand = quantity_on_hand
        print("Item details updated.")

    def update_quantity(self, quantity):
        """Updates the quantity on hand."""
        self.validate_quantity(quantity)
        self.quantity_on_hand += quantity
        print(f"Updated quantity on hand: {self.quantity_on_hand}")

    def get_item_details(self):
        """Retrieves item details."""
        return {
            "Item ID": self.item_id,
            "Name": self.name,
            "Price": self.price,
            "Quantity on Hand": self.quantity_on_hand
        }

    @staticmethod
    def validate_price(price):
        """Validates the price."""
        if price < 0:
            raise ValueError("Price cannot be negative.")

    @staticmethod
    def validate_quantity(quantity):
        """Validates the quantity."""
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")
