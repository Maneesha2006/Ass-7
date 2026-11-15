
class ShoppingCart:
    def __init__(self):
        self.items = []
        self.discount = 0

    def add_item(self, item):
        self.items.append(item)
        print(item, "added to cart")

    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)
            print(item, "removed from cart")

    def apply_coupon(self, discount):
        self.discount = discount
        print(discount, "% coupon applied")

    def show_cart(self):
        print("Cart Items:", self.items)
        print("Discount:", self.discount, "%")


class Command:
    def execute(self):
        pass

    def undo(self):
        pass


class AddCommand(Command):
    def __init__(self, cart, item):
        self.cart = cart
        self.item = item

    def execute(self):
        self.cart.add_item(self.item)

    def undo(self):
        self.cart.remove_item(self.item)


class RemoveCommand(Command):
    def __init__(self, cart, item):
        self.cart = cart
        self.item = item

    def execute(self):
        self.cart.remove_item(self.item)

    def undo(self):
        self.cart.add_item(self.item)


class CouponCommand(Command):
    def __init__(self, cart, discount):
        self.cart = cart
        self.discount = discount
        self.old_discount = cart.discount

    def execute(self):
        self.cart.apply_coupon(self.discount)

    def undo(self):
        self.cart.apply_coupon(self.old_discount)


class Remote:
    def __init__(self):
        self.history = []
        self.redo_history = []

    def execute(self, command):
        command.execute()
        self.history.append(command)
        self.redo_history.clear()

    def undo(self):
        if self.history:
            command = self.history.pop()
            command.undo()
            self.redo_history.append(command)
        else:
            print("Nothing to undo")

    def redo(self):
        if self.redo_history:
            command = self.redo_history.pop()
            command.execute()
            self.history.append(command)
        else:
            print("Nothing to redo")


cart = ShoppingCart()
remote = Remote()

remote.execute(AddCommand(cart, "Laptop"))
remote.execute(AddCommand(cart, "Mouse"))
remote.execute(RemoveCommand(cart, "Mouse"))

cart.show_cart()

print("\nUndo Operation:")
remote.undo()
cart.show_cart()

print("\nRedo Operation:")
remote.redo()
cart.show_cart()

print("\nApplying Coupon:")
remote.execute(CouponCommand(cart, 10))
cart.show_cart()
