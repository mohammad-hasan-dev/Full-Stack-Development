class bc_account:
    def withdraw(self):
        print("Money Withdrawn")

class sv_ac(bc_account):
    pass


ba= bc_account()
ba.withdraw()