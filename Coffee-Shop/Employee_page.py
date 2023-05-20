

class employee:
    
    def __init__(self,name_employee:str, number_employee:int):
        
        self.name_employee = name_employee
        self.number_employee = number_employee

    def casher_info(self):


        return (f"cahser name: {self.name_employee} \ncahser No. {self.number_employee}")


casher1 = employee("Nasser",1)
casher2 = employee("Amaal",2)
casher3 = employee("Ahmad",3)


casher_list = set()
casher_list.add(casher1.casher_info())
casher_list.add(casher2.casher_info())
casher_list.add(casher3.casher_info())


def casher_print():
    accountant = ""

    for i in casher_list:
        accountant = i
        print(accountant)
        break

    return ""

