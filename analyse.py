
def print_dict_by_freq(dc,re=True,n=0):
    #按照频率顺序显示信息
    k=list(dc.keys())
    v=list(dc.values())
    kv=[]
    for i in range(len(k)):
        kv.append((v[i],k[i]))
    kv=sorted(kv,key=lambda x:x[0],reverse=re)
    if n!=0:
        for i in kv[:n]:
            print("<{}>={:>2} ".format(i[1],i[0]),end="")
    else:
        for i in kv:
            print("<{}>={:>2} ".format(i[1],i[0]),end="")
            
        print()


a=open ("lala.txt")
arr=a.read()
dc={}
k=3
print(arr.split())
haha=['lacrosses', 'protectional', 'blistered', 'leaseback', 'assurers', 'frizzlers', 'submerse', 'rankness', 'moonset', 'farcer', 'brickyard', 'stolonic', 'trimmings', 'glottic', 'rotates', 'twirlier', 'stuffer', 'publishable', 'invalided', 'harshens', 'tortoni', 'unlikely', 'alefs', 'gladding', 'favouring', 'particulate', 'baldpates', 'changeover', 'lingua', 'proctological', 'freaking', 'outflanked', 'amulets', 'imagist', 'hyped', 'pilfers', 'overachiever', 'clarence', 'outdates', 'smeltery']
print(haha)
for i in arr.split():

    for j in range(len(i)):
        if i[j:j+k] in dc:
            dc[i[j:j+k]]=dc[i[j:j+k]]+1
        else:
            dc[i[j:j+k]]=1
#print_dict_by_freq(dc)