string = input("Δώσε ενα string: ")
anum = ''.join(str(ord(i)) for i in string) #metatrepei kathe gramma toy string se ascii kai enwnei ola ta ascii pshfia
print("Το string σε ASCII είναι: " + anum)
for i in range (2, int(anum)): #diairei olous toys arithmous prin ton anum me ton anum kai an estw kai enas ton diairei (afeinei upoloipo 0) stamataei h diadikasia (o arithmos den einai prwtos)
    if int(anum)%i==0: 
        print("Ο αριθμός δεν είναι πρώτος")
        break
    if i==(int(anum)-1): #an h epanalhpsh ftasei ston arithmo pou einai o anum - 1 tote o anum einai prwtos (afou den diareitai me kanena prohgoumeno) 
        print("Ο αριθμός είναι πρώτος")
        
        
