#文件读取：把数据读取到全局变量PETS中：

PETS=[]
FILE_NAME="PetsInfo.txt"

try:
    with open(FILE_NAME,"r",encoding="utf-8") as fp:
        while True:            
            pet_string=fp.readline()
            if not pet_string:
                break
            pet_decode=pet_string.split("|")
            pet_info={"ID":pet_decode[0],"name":pet_decode[1],"category":pet_decode[2],"price":pet_decode[3]}
            PETS.append(pet_info)
        fp.close()
        
except FileNotFoundError:
    fp=open(FILE_NAME,"w",encoding="utf-8")
    fp.close()


#实现函数：

def add_pet():
    print("add pet infomation:")
    ID=input("请输入宠物编号：")
    name=input("请输入宠物名称：")
    category=input("请输入宠物种类：")
    price=input("请输入宠物价格：")
    temp_pet={"ID":ID,"name":name,"category":category,"price":price}
    PETS.append(temp_pet)
    print("pet infomation insert succeed!")

def search_pet():
    print("search pet infomation ****:")
    name=input("请输入宠物名称：")
    flag=1
    for pet in PETS:
        if name==pet["name"]:
            temp="编号:{}\n名称:{}\n种类: {}\n价格: {}".format(
                pet["ID"],
                pet["name"],
                pet["category"],
                pet["price"]
                )
            print(temp)
            flag=2
    if flag==1:
        print("not find pet infomation!")

def delete_pet():
    ID=input("请输入宠物的编号")
    for pet in PETS:
        if pet["ID"]==ID:
            PETS.remove(pet)
            print("OK,pet infomation delete succeed!")
            break


def list_pet():
    print("list all infomation about pets:")
    for pet in PETS:
        print("-"*30)
        temp="编号: {}\n名称: {}\n种类: {}\n价格: {}".format(
                pet["ID"],
                pet["name"],
                pet["category"],
                pet["price"]
        )
        print(temp)
        print("-"*30)

        


def exit_sys():
    with open(FILE_NAME,"w",encoding="utf-8") as fp:
        lines=[]
        for pet in PETS:
            pet_encode="{}|{}|{}|{}|".format(
                pet["ID"],
                pet["name"],
                pet["category"],
                pet["price"]
            )
            lines.append(pet_encode+"\n")
        fp.writelines(lines)
        fp.close()





#主
def main():
    print("*"*30)
    print("1.添加宠物")
    print("2.查找宠物")
    print("3.删除宠物")
    print("4.列出宠物")
    print("5.退出系统")
    print("*"*30)
    while True:
        option=input("请输入你的选项：")
        if option=="1":
            add_pet()
        elif option=="2":
            search_pet()
        elif option=="3":
            delete_pet()
        elif option=="4":
            list_pet()
        elif option=="5":
            exit_sys()
            break
        else:
            print(u"请输入正确选项：")

main()
        
