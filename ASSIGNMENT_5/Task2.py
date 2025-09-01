list1=[]
for i in range(1,11):
    list1.append(i)
print("Original List: ",list1)
list2=list1[0:5]
print("Extrcted First Five Element From List: ",list2)
list3=list2[::-1]
print("Reversed Extracted Element: ",list3)
