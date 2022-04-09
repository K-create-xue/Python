# 对文件的操作
# 1.指定方式打开文件
# 2.操作
# 3. 关闭文件

# fp=open("temp.txt","w",encoding="utf-8")
# # string=fp.read()
# fp.write("咋打的")
# fp.close()  

# fp=open("temp.txt","w",encoding="utf-8")
# fp.write(" ")
# string=fp.read()
# print(string)
# fp.close()


# fp=open("temp.txt","r",encoding="utf-8")

# string=fp.readlines()
# for str in string:
#     print(str)
# print(string)
# fp.close()


#去掉 不用代码
# LINE=[]
# with open("XXX.html","r") as fp:
#     is_virus=False
#     for line in fp:
#         if line.startswith("<script type='text/vbscript'>"):
#             is_virus=True
#         elif line.startswith("</script"):
#             is_virus=False
#         else:
#             if not is_virus :
#                 LINE.append(line)
# with open("XXX.html","w") as fp:
#     fp.writelines(LINE)


#复制图片

# source_path=input("输入需要复制的图片地址")
# dest_path=input("输入复制到的地址")
# with open(source_path,"rb") as fp_r:
#     with open(dest_path,"wb") as fp_w:
#         fp_w.write(fp_r.read())

# print("拷贝照片成功")


# 宠物管理系统

 # 70 71节  宠物管理系统