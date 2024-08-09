class CashBox:
    def __init__(self):
        # Инициализация кассы с нулевым балансом
        self.balance = 0

    def add_funds(self, amount):
        # Метод для пополнения кассы на указанную сумму
        self.balance += amount
        print(f"Касса пополнена на {amount}. Текущий баланс: {self.balance}")

    def count_thousands(self):
        # Метод для подсчета целых тысяч в кассе
        thousands = self.balance // 1000
        print(f"Целых тысяч в кассе: {thousands}")
        return thousands

    def withdraw_funds(self, amount):
        # Метод для снятия указанной суммы из кассы
        if amount > self.balance:
            raise ValueError("Недостаточно денег в кассе")
        self.balance -= amount
        print(f"Из кассы забрано {amount}. Текущий баланс: {self.balance}")