def check(x):
    try:
        num2=int(x) #an to num den einai int den einai oyte to num2 ara epistrefei false
        calc(num2)
        return True
    except:
        return False

def calc(y):
    a=2 #dinei mia timh diaforh toy 1 sth metavlhth a gia na ksekinhsei h diadikasia
    while a!=1: #oso o telikos arithmos einai monopshfios epanalave
        num3 = y*3 + 1
        array = [int(i) for i in str(num3)] #vazei se lista kathe pshfio ths num3
        print('Τα ψηφία του τελικού αριθμού είναι: ' + str(array))
        s=sum(array)
        print('Το άθροισμα των ψηφίων είναι: ' + str(s))
        a=len(str(s))
        if a==1:
            print('Ο τελικός αριθμός έχει 1 ψηφίo, οπότε ολοκληρώνετε η διαδικασία')
            break #an a=1 h diadikasia teleiwnei kai h synarthsh check epistrefei true
        print('Ο τελικός αριθμός έχει '+str(a)+' ψηφία, οπότε επαναλαμβάνετε η διαδικασία με το '+str(s)+'\n')
        num3 = s #kane pali thn diadikasia me arxikh metavlhth thn s
        y = s 

num='b' #dinei esfalmenh timh sth metavlhth num gia na zhththei arithmos
while not check(num): #oso h synarthsh check epistrefei False (otan dhladh o xrhsths dinei string) zhta ksana arithmo
    num = input("Δώσε έναν φυσικό αριθμό:")
