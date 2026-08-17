import argparse
import os

def scaffold_singleton(args):
    content = """class SingletonMeta(type):
    _instances = {}
    
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

class DatabaseConnection(metaclass=SingletonMeta):
    def connect(self):
        print("Connected to DB")

if __name__ == "__main__":
    db1 = DatabaseConnection()
    db2 = DatabaseConnection()
    print(db1 is db2)  # True
"""
    filename = "singleton_pattern.py"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"[SUCCESS] Scaffoled Singleton Pattern at {filename}")

def scaffold_strategy(args):
    content = """from abc import ABC, abstractmethod

class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount: float):
        pass

class CreditCardPayment(PaymentStrategy):
    def pay(self, amount: float):
        print(f"Paid ${amount} using Credit Card")

class PayPalPayment(PaymentStrategy):
    def pay(self, amount: float):
        print(f"Paid ${amount} using PayPal")

class ShoppingCart:
    def __init__(self, strategy: PaymentStrategy):
        self._strategy = strategy
        
    def checkout(self, amount: float):
        self._strategy.pay(amount)

if __name__ == "__main__":
    cart = ShoppingCart(CreditCardPayment())
    cart.checkout(100.0)
"""
    filename = "strategy_pattern.py"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"[SUCCESS] Scaffoled Strategy Pattern at {filename}")

def main():
    parser = argparse.ArgumentParser(description="Design Pattern Scaffolding Tools")
    subparsers = parser.add_subparsers(dest="command", required=True)

    single_parser = subparsers.add_parser("init-singleton", help="Scaffold a thread-safe Singleton pattern in Python")
    single_parser.set_defaults(func=scaffold_singleton)

    strat_parser = subparsers.add_parser("init-strategy", help="Scaffold a Strategy pattern in Python")
    strat_parser.set_defaults(func=scaffold_strategy)

    args = parser.parse_args()
    args.func(args)

if __name__ == "__main__":
    main()
