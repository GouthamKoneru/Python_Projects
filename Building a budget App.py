class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({
            "amount": amount,
            "description": description
        })

    def withdraw(self, amount, description=""):
        if not self.check_funds(amount):
            return False

        self.ledger.append({
            "amount": -amount,
            "description": description
        })
        return True

    def get_balance(self):
        return sum(item["amount"] for item in self.ledger)

    def transfer(self, amount, category):
        if not self.check_funds(amount):
            return False

        self.withdraw(amount, f"Transfer to {category.name}")
        category.deposit(amount, f"Transfer from {self.name}")
        return True

    def check_funds(self, amount):
        return amount <= self.get_balance()

    def __str__(self):
        title = self.name.center(30, "*")
        output = title + "\n"

        for item in self.ledger:
            description = item["description"][:23]
            amount = f'{item["amount"]:.2f}'[:7]
            output += f"{description:<23}{amount:>7}\n"

        output += f"Total: {self.get_balance():.2f}"
        return output


def create_spend_chart(categories):
    output = "Percentage spent by category\n"

    # Calculate withdrawals for each category.
    spent = []
    for category in categories:
        total = sum(
            -item["amount"]
            for item in category.ledger
            if item["amount"] < 0
        )
        spent.append(total)

    total_spent = sum(spent)

    # Calculate percentages, rounded down to the nearest 10.
    percentages = []
    for amount in spent:
        if total_spent == 0:
            percentage = 0
        else:
            percentage = int((amount / total_spent) * 100) // 10 * 10
        percentages.append(percentage)

    # Draw the vertical bar chart.
    for level in range(100, -1, -10):
        output += f"{level:>3}|"
        for percentage in percentages:
            if percentage >= level:
                output += " o "
            else:
                output += "   "
        output += " \n"

    # Draw the horizontal line.
    output += "    " + "-" * (len(categories) * 3 + 1) + "\n"

    # Print category names vertically.
    max_length = max(len(category.name) for category in categories)

    for i in range(max_length):
        output += "     "
        for category in categories:
            if i < len(category.name):
                output += category.name[i] + "  "
            else:
                output += "   "
        if i < max_length - 1:
            output += "\n"

    return output