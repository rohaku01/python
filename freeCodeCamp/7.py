class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []
    
    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})
    
    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False
    
    def get_balance(self):
        return sum(item["amount"] for item in self.ledger)
    
    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category.name}")
            category.deposit(amount, f"Transfer from {self.name}")
            return True
        return False
    
    def check_funds(self, amount):
        return amount <= self.get_balance()
    
    def __str__(self):
        # Заголовок
        title = f"{self.name:*^30}\n"
        
        # Транзакции
        lines = []
        for item in self.ledger:
            description = item["description"][:23]
            amount = f"{item['amount']:.2f}"
            lines.append(f"{description:<23}{amount:>7}")
        
        transactions = "\n".join(lines)
        
        # Итог
        total = f"Total: {self.get_balance():.2f}"
        
        if lines:
            return title + transactions + "\n" + total
        return title + total


def create_spend_chart(categories):
    # Собираем суммы снятий
    withdrawals = []
    for category in categories:
        total = 0
        for item in category.ledger:
            if item["amount"] < 0:
                total += abs(item["amount"])
        withdrawals.append(total)
    
    # Общая сумма снятий
    total_spent = sum(withdrawals)
    
    # Рассчитываем проценты (округление вниз до 10)
    percentages = []
    if total_spent > 0:
        for spent in withdrawals:
            percent = (spent / total_spent) * 100
            percent = (percent // 10) * 10
            percentages.append(int(percent))
    else:
        percentages = [0] * len(categories)
    
    # Строим диаграмму
    chart = "Percentage spent by category\n"
    
    # Вертикальная ось от 100 до 0
    for i in range(100, -1, -10):
        chart += f"{i:>3}|"
        for percent in percentages:
            if percent >= i:
                chart += " o "
            else:
                chart += "   "
        chart += " \n"
    
    # Горизонтальная линия
    chart += "    " + "-" * (len(categories) * 3 + 1) + "\n"
    
    # Названия категорий вертикально
    max_len = max(len(cat.name) for cat in categories)
    for i in range(max_len):
        chart += "     "
        for cat in categories:
            if i < len(cat.name):
                chart += f"{cat.name[i]}  "
            else:
                chart += "   "
        if i < max_len - 1:
            chart += "\n"
    
    return chart