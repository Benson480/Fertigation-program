##class Duck:
##    def __init__(self, height, weight, sex):
##        self.height = height
##        self.weight = weight
##        self.sex = sex
##
##    def walk(self):
##        pass
##    
##    def quack(self):
##        return print("Quack")
##
##
##duckling = Duck(height=10, weight=3.4, sex="male") #instance1
##drake = Duck(height=25, weight=3.7, sex="male") #instance2
##hen = Duck(height=20, weight=3.4, sex="female") #instance3
##
####drake.quack()
####print(duckling.height)
##
##print(Duck.__class__)   #type
##print(duckling.__class__)
####print(duckling.sex.__class__)
##print(duckling.quack.__class__)


##class Demo():
##    def __init__(self, value):
##        self.instance_var = value
##
##d1 = Demo(100)
##d2 = Demo(200)
##print("d1's instance variable is equal to:", d1.instance_var)
##print("d2's instance variable is equal to:", d2.instance_var)

##class Demo():
##    def __init__(self, value):
##        self.instance_var = value
##
##
##d1 = Demo(100)
##d2 = Demo(200)
##
##d1.another_var = "another variable in the object"
##
##print("contents of d1:", d1.__dict__)
##print("contents of d2:", d2.__dict__)
##print(d1.instance_var)

##
##class Demo:
##    class_var = 'shared variable'
##
##print(Demo.class_var)
##print(Demo.__dict__)


##class Demo:
##    class_var = 'shared variable'
##
##d1 = Demo()
##d2 = Demo()
##
##print(Demo.class_var) #use class
##print(d1.class_var)  #use class instance
##print(d2.class_var)
##print("Contents of d1:", d1.__dict__)
##
##class Duck:
##    counter = 0
##    species = "duck"
##
##    def __init__(self, height, weight, sex):
##        self.height = height
##        self.weight = weight
##        self.sex = sex
##        Duck.counter +=1
##
##    def walk(self):
##        pass
##    def quack(self):
##        print('quacks')
##
##class Chicken:
##    species = 'chicken'
##
##    def walk(self):
##        pass
##    def cluck(self):
##        print('clucks')
##
##duckling = Duck(height=10, weight=3.4, sex="male")
##drake = Duck(height=25, weight=3.7, sex="male")
##hen = Duck(height=20, weight=3.4, sex="female")
##
##chicken = Chicken()
##
##print("So many ducks were born:", Duck.counter)
##
##for poultry in duckling, drake, hen, chicken:
##    print(poultry.species, end=' ')
##    if poultry.species == 'duck':
##        poultry.quack()
##    elif poultry.species == 'chicken':
##        poultry.cluck()
##    


class Phone:
    counter = 0
    def __init__(self, number):
        self.number = number
        Phone.counter += 1

    def call(self, number):
        message = 'Calling {} using own number {}'.format(number, self.number)
        return message

class FixedPhone(Phone):
    last_SN = 0

    def __init__(self, number):
        super().__init__(number)
        FixedPhone.last_SN += 1
        self.SN = 'FP-{}'.format(FixedPhone.last_SN)

class MobilePhone(Phone):
    last_SN = 0

    def __init__(self, number):
        super().__init__(number)
        MobilePhone.last_SN += 1
        self.SN = 'MP-{}'.format(MobilePhone.last_SN)


print('Total number of phone devices created:', Phone.counter)
print("Creating 2 devices")
fphone = FixedPhone('555-2368')
mphone = MobilePhone('01632-960004')

print("Total number of phone devices created:", Phone.counter)
print("Total number of mobile phone devices created:", MobilePhone.last_SN)

print(fphone.call('01632-960004'))
print('Fixed phone received "{}" serial number'.format(fphone.SN))
print('Mobile phone receivedd "{}" serial number'.format(mphone.SN))
