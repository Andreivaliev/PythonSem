def revers_range(num):
    if num > 0:
        revers_range(num-1)
    print(num, end="")


def degree(a,b):
    if b==0:
        return 1
    if b>0:
        return a*degree(a,b-1)
    if b<0: 
        return 1/a*degree(a,b+1) 


def sum(a,b):

    if a==0:
        return b
    return sum(a-1,b+1)


def sum_of_dividers(num):
    sum=1
    for i in range(2, num // 2 + 1):
        if num %i == 0:
            sum+=i
    return sum

def find_farthest_orbit(orbits):
    list1=list(filter(lambda x: x[0]!=x[1],orbits))
    max=0
    count=0
    list2=[]
    for i in list1:
        if i[0]*i[1]>max:
            max=i[0]*i[1]
            count+=1
            list2.append((i[0],i[1]))
            if count>1:
                list2.pop(0)
    return list2

def slog(st):
    sum=0
    for word in st:
        count=0
        for i in word:
            if i in 'аеёиоуыэюя':
                count+=1
        if sum>0 and sum!=count:
            return False
        sum=count
    return True 





def show_contacts(file_name):
    with open(file_name, 'r') as file:
        date=file.readlines()

        for contact in date:
            print(contact)
    input("press any key")
    
def add_contact(file_name):
    with open(file_name, 'a') as file:
        res = ''
        res += input("Input a surname of contact: ")
        res += input("Input a name of contact: ")
        res += input("Input a phone number of contact: ")

        file.write(res)
    input("Contact was successfully contact! Press any key")   

def search_contact(file_name):
    target=input("Input a name of contact for searching: ")

    with open(file_name, 'r') as file:
        data = file.readlines()

        if target in data:
            for contact in data:
                if target in contact:
                    print(contact)
                    break
        else:
            print("there is no contacts with this name.")
    input("press any key")

def drawing():
    print('1 - show contacts')
    print('2 - add contact')
    print('3 - search contact')
    print('4 - exist')

def main():
    while True:
        os.system('CLS')
        drawing()





