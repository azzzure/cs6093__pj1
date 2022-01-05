from util import *



        
        

def plaintext_ciphertext(ciphertext,plaintext):
    L=len(plaintext)
    dc={}
    for i in range(L):
        d=distance(ciphertext[i],plaintext[i])
        if d in dc:
            dc[d]=dc[d]+1
        else:
            dc[d]=1
    # print_dict_by_freq(dc,n=6)
    # print(">>{}<<".format(len(dc.keys())))
    if len(dc.keys())<27:
        print("our guess:")
        print(plaintext)
        return True
    else :
        return False


    


def plaintext_ciphertext_with_random(ciphertext,plaintext):
    num_rand_char=len(ciphertext)-len(plaintext)
    if num_rand_char>24 :
        num_rand_char=24
    shifted_ciphertext=[]
    for i in range(num_rand_char):
        temp=ciphertext[i:]+ciphertext[:i]
        shifted_ciphertext.append(temp)
    Lc=len(ciphertext)
    Lp=len(plaintext)
    shiftcycle=""
    for ct in shifted_ciphertext:
        for i in range(Lc):
            d=chr(distance(ct[i],plaintext[i%Lp])+97)
            shiftcycle=shiftcycle+d
    dc={}
    n_repeat=5
    for i in range(len(shiftcycle)-n_repeat):
        if shiftcycle[i:i+n_repeat] in dc:
            dc[shiftcycle[i:i+n_repeat]]=dc[shiftcycle[i:i+n_repeat]]+1
        else:
            dc[shiftcycle[i:i+n_repeat]]=1
    # print_dict_by_freq(dc,n=10)
    max_num=extract_max_n_freq(dc,1)
    # print(">>{}<<".format(len(dc.keys())))
    return max_num
    

def plaintext_ciphertext_with_random_no_cycle(ciphertext,plaintext):
    num_rand_char=len(ciphertext)-len(plaintext)
    if num_rand_char>24 :
        num_rand_char=24
    #最多24个就循环了嘛
    shifted_ciphertext=[]
    for i in range(num_rand_char):
        temp=ciphertext[i:]+ciphertext[:i]
        shifted_ciphertext.append(temp)
    dc={}
    Lc=len(ciphertext)
    Lp=len(plaintext)
    for ct in shifted_ciphertext:
        for i in range(Lc):
            d=distance(ct[i],plaintext[i%Lp])
            if d in dc:
                dc[d]=dc[d]+1
            else:
                dc[d]=1


    v=extract_max_n_freq(dc,6)
    # print_dict_by_freq(dc,n=6)
    # print(">>{}<<".format(len(dc.keys())))
    return sum(v)

def test1_dec(ciphertext):
    if len(ciphertext)==500:
        for plaintext in candidates:
            if plaintext_ciphertext(ciphertext,plaintext):
                break
            else:
                continue
    else:
        n=[]
        for plaintext in candidates:
            n.append(plaintext_ciphertext_with_random(ciphertext,plaintext))
        # print(n)
        if (max(n)>min(n)*3)and(max(n)>min(n)+3):
            index=n.index(max(n))
            print("our guess:")
            print(candidates[index])
        else:
            print("oops")
            n=[]
            for plaintext in candidates:
                n.append(plaintext_ciphertext_with_random_no_cycle(ciphertext,plaintext))
            # print("{}".format(n))
            index=n.index(max(n))
            print("our guess:")
            print(candidates[index])
            

