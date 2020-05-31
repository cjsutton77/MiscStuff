def luhn(num):
    num = num[::-1]
    sumc = 0
    b = enumerate(num)
    for i,j in b:
        if i%2 != 0:
            c=((int(j)*2))
            if (c>9):
                c=c%10+1
            #print(j,2*int(j),c)
        else:
            c=int(j)
            #print(j,c)
        sumc = sumc + c
    #print(sumc)
    return sumc

def swap_pos(arr,pos1,pos2):
    lst = list(arr)
    lst[pos1],lst[pos2] = lst[pos2],lst[pos1]
    #print(lst)
    return lst    

def swap(n):
    for i in range(14):
        ana=[]
        ana = swap_pos(n,i,i+1)
        val = luhn(''.join(ana)) 
        #print(val)
        if val % 10 == 0:
            break
        else:
            continue
    return ''.join(ana)

def cycle(n):
    pos = n.index('?')
    nn = list(n)
    for i in range(10):
        nn[pos] = str(i)
        val = luhn(''.join(nn)) 
        #1print(i,val)
        if val % 10 == 0:
            break
        else:
            continue
    return ''.join(nn)

cases = int(input())

inp=[]
for i in range(cases):
    inp.append(input())

for i in inp:
    v = i
    if '?' in v:
        nv = cycle(v)
    else:
        nv = swap(v)
    print (nv)
    
