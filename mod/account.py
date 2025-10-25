accounts=[]
import time
from func.convert_from_json import convert_from_json
import re
class Account:
    
    def __init__(self,id,type,name,password):
        self.id=id
        self.type=type
        self.name=name
        self.password=password
    def add_account():
        accounts=convert_from_json("data/accounts.json")
        id = "ACC"
        account_type=input("Enter account type: \n").strip()
        # if re.match("gmail",'hotmail',"facebook",'instgram') == False:
        #     print("Valid account type")
        #     return
        name=input("Enter account Name: \n").strip()
        password=input("Enter account Password").strip()
        if account_type =='' or name=='' or password =="":
            print("Valid account data")
            return
        print("Check if account exit...")
        time.sleep(2)
        for acc in accounts:
            if acc['name'].lower() == name.lower():
                print("Exit Account ^^")
                return
        new_account=Account(id,account_type,name,password)
        accounts.append(new_account.__dict__)
        from func.write_txt import write_txt
        write_txt("data/accounts.json",accounts)
    def get_password():
        accounts=convert_from_json("data/accounts.json")
        # Authantcate user
        account_name=input("Enter account Name: \n").strip()
        for acc in accounts:
            if acc['name'].lower() == account_name.lower():
                print(f"account name: {acc['name']}")
                print(f'account password: {acc['password']}')
    def list_accounts():
        print("list")
