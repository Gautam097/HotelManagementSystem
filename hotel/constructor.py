from ast import arguments


class Employee:
    no_of_leaves =8
    
    # Employee class ko argument dene ko constructor kehte hai
    # where name = instance variable and aname is arguments
    def ___init___(self,aname,asalary,arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

# self ka mtlb  khud aur self kya hota hai na wo object jiski baat ki ja rahi hai. and agar koi function self argument lekr define hai usko aur main agar class ka object banau   example niche hai . obj.printdetails() krdu to wo fuction call ho jayega us object ke liye . it means obj become self in this fucntion.
    def printdetails(self):
        return f"The Name is {self.name}. salary is {self.salary} and role is {self.role}"

gautam = Employee(" gautam",255,"programmer")

# rohan = Employee()
# harry = Employee()
# harry.name = " Harry"
# harry.salary = 455
# harry.role = "instructor"

# rohan.name = "rohan"
# rohan.salary = 2234
# rohan.role = "student"

# print(rohan.printdetails())
print(gautam.salary)