"""Experiment:Configure VS Code with AI Coding Assistant
Objective: Implement and understand Configure VS Code with AI Coding Assistant."""

class Calculator:
    
    
    def __init__(self, a, b):
        
        self.a = a
        self.b = b

    
    def add(self):
        
        return self.a + self.b

    def subtract(self):
        return self.a - self.b

    def multiply(self):
        return self.a * self.b

calc = Calculator(10, 5)

print(f"Addition: {calc.add()}")        
print(f"Subtraction: {calc.subtract()}")  
print(f"Multiplication: {calc.multiply()}")
