from mod.account import Account
def welcome():
    print("""
1- Press 1 to create password Account
2- Press 2 to get Account
          """)
    enter = int(input("Enter Num: \n"))
    print(enter)
    if enter == 1:Account.add_account()
    if enter == 2:Account.get_password()