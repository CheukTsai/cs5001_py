# Homework credited by Zhuocai Li
# https://github.ccs.neu.edu/CS-5001-SEA-Spring2021/student-ZhuocaiLi

def DMV():
    import random
    driver_license = ""
    num = 1
    for num in range(1,8):
        driver_license = driver_license + str(random.randint(1,9))
        num += 1    
    name = str(input("Please enter your first, middle and last name: "))
    name_LN = ""
    name_FN = ""
    space_num = 0
    for character in name:
        if(character.isspace()):
            space_num = space_num + 1
        if(space_num <2):
            name_FN = name_FN + character 
        if(space_num == 2 and character.isspace() == False):
            name_LN = name_LN + character        
    date_of_birth = str(input("Enter date of birth(MM/DD/YY): ")) 
    
    slash_num = 0
    expire_day = ""
    for character in date_of_birth:
        expire_day = expire_day + character
        if(character == "/"):
            slash_num = slash_num+1
        if(slash_num == 2):
            expire_day = expire_day + "21"
            break
    
    print("-------------------------------------")
    print("Washington Driver License")
    print("DL ", driver_license)
    print("LN ", name_LN)
    print("FN ", name_FN)
    print("DOB", date_of_birth)
    print("EXP", expire_day)
    print("-------------------------------------")
DMV()