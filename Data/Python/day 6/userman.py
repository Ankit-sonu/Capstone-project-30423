class User:
    def __init__(self, name): self.name = name
    def info(self): return "User"

class AdminUser(User):
    def info(self): return "Admin"
    def ban(self, user): print(f"{self.name} banned {user.name}")

class GuestUser(User):
    def info(self): return "Guest"

class RegisteredUser(User):
    def info(self): return "Registered"

a = AdminUser("Alice")
g = GuestUser("Bob")
r = RegisteredUser("Cara")
print(a.info(), g.info(), r.info())
a.ban(r)
