import re

f=open("TEXT FOR 5.txt")
text=f.read()
list1 = re.split('[.!?;:,\n ]',text) #xwrizei tis lekseis toy keimenoy apo toys xarakthres stis [] kai tis vazei sth lista list1
while '' in list1:
    list1.remove('') #afairei kathe pithano keno string apo th lista

print('Η αυθεντική λίστα είναι: ' + str(list1))

for i in range (len(list1)):
    if len(list1[i])>3:
        list1[i] = list1[i][1:] + list1[i][0] + "ay" #metaferei to prwto gramma sto telos kai prosthetei to "ay" se oses lekseis ths listas exoun parapanw apo 3 grammata

print('\nΗ τελική λίστα είναι: ' + str(list1))

f.close()
