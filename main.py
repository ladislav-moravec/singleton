from database import Database

a = Database()
b = Database()
c = Database()

print("Jméno databáze a {} b {} c {}".format(a.jmeno, b.jmeno, c.jmeno))
print("Je a instance Databaze?", a is Database)
print("Je b instance Databaze?", b is Database)
print("Je c instance Databaze?", c is Database)
