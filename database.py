class Database():

    __instance = None

    jmeno = None

    def __new__(self):
        if Database.__instance:
            print("Instance již existuje")
        else:
            print("Vytvářím instanci")
            self.jmeno = "SQLite"
            Database.__instance = self
        return Database.__instance
