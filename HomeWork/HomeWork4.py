class InterestBearingItem:
    pass

class Asset:
    pass

class BankAccount(Asset, InterestBearingItem):
    pass

class Security(Asset):
    pass

class InsurableItem:
    pass

class RealEstate(Asset, InsurableItem):
    pass

class Stock(Security):
    pass

class Bond(Security):
    pass

class SavingsAccount(BankAccount):
    pass

class CheckingAccount(BankAccount):
    pass
