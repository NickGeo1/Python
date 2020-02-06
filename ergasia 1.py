import re

f = open("TEXT FOR 1.txt")
text = f.read() #apothikevei to periexomeno toy arxeioy sthn text
word_list = re.split('[.!?;:,\n ]',text) #xwrizei tis lekseis toy keimenoy apo toys xarakthres stis [] kai tis vazei sth lista word_list
while '' in word_list:
    word_list.remove('') #afairei kathe pithano keno string apo th lista 
    

print('Οι λέξεις του αρχείου είναι: '+ str(word_list))

final_list = [] #h lista poy tha periexei tis 5 lekseis
for i in range(0, 5): #pente fores epanalhpsh gia na vrei tis 5 megalhteres
    max1 = 0
    for j in range(len(word_list)):      
        if len(word_list[j]) > max1: 
             max1 = len(word_list[j]);
             maxword = word_list[j]  #edw elegxei kathe leksh ths listas 5 fores kai meta apo kathe perasma afairei th megalhterh apo thn word_list kai thn prosthetei sthn final_list
    word_list.remove(maxword); 
    final_list.append(maxword)
    
print('\nΟι 5 μεγαλύτερες λέξεις είναι: '+str(final_list))

vowels = ["a", "A", "y", "Y", "i", "I", "o", 'O', 'e', 'E', 'u', 'U']
for i in range (len(vowels)):
    final_list = [j.replace(vowels[i], '') for j in final_list] # se kathe leksh ths final_list antikathista ta grammata pou periexontai sth vowels me '' (afairountai ta fwnhenta)
    
for i in range (len(final_list)):
    final_list[i] = final_list[i][::-1] # gurnaei anapoda oles tis lekseis ths final_list
    
print ('\n Οι ίδιες λέξεις ανάποδα χωρίς φωνήεντα: '+str(final_list)) 

f.close()
