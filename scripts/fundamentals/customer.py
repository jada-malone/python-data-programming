# PROGRAM: Customer
# PURPOSE: To manage customer data.
# INPUT: Customer details (ID, name, email).
# PROCESS: Initializes, updates, and retrieves customer information.
# OUTPUT: Displays customer details.
# HONOR CODE: On my honor, as an Aggie, I have neither given nor received unauthorized aid on this academic work.

class Customer:
    """A class to represent a customer."""

    def __init__(self, customer_id, name, email):
        self.customer_id = customer_id
        self.name = name
        self.email = email

    def update_details(self, name=None, email=None):
        """Updates customer details."""
        if name:
            self.name = name
        if email:
            self.validate_email(email)
            self.email = email
        print("Customer details updated.")

    def get_customer_info(self):
        """Retrieves customer information."""
        return {
            "Customer ID": self.customer_id,
            "Name": self.name,
            "Email": self.email
        }

    @staticmethod
    def validate_email(email):
        """Validates the email format."""
        if "@" not in email or "." not in email:
            raise ValueError("Invalid email address.")
