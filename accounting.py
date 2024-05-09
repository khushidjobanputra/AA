class StackSimulator:
    def __init__(self):
        self.items = []
        self.amortised_cost = 0
        self.credit_bank = 0

    def is_empty(self):
        return len(self.items) == 0

    def push(self, value):
        self.items.append(value)
        self.amortised_cost += 2
        self.credit_bank += 1
        print(f"Pushed ({value}): charge is 2 units (1 for push, 1 as credit for future pop)")
        self.print_stack()

    def pop(self):
        if self.is_empty():
            print('stack underflow')
        else:
            pop_value = self.items.pop()
            self.amortised_cost += 0
            self.credit_bank -= 1
            print(f"Popped ({pop_value}): No charge, uses credit")
            self.print_stack()

    def multipop(self, count):
        if count > len(self.items):
            print(f"Error: Trying to pop {count} items, but stack has only {len(self.items)} items")
        else:
            popped_values = []
            for _ in range(count):
                popped_values.append(self.items.pop())
                self.amortised_cost += 0
                self.credit_bank -= 1
            print(f"Multipopped {count} items: {popped_values}")
            self.print_stack()

    def print_stack(self):
        print(f'Stack: {self.items}\nCredit Bank: {self.credit_bank}\nAmortised cost: {self.amortised_cost}\n')

# Test the multipop method
stack = StackSimulator()
stack.push(1)
stack.push(2)
stack.push(3)
stack.multipop(2)