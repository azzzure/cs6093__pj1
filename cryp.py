import random
import difflib
candidates=[
 "dispossess drencher barstool interval cardiacs vixens mooncalves tinnily perineal panamanian unparalleled unsoundness goalkeeper torchier eclat bartisans jewed claudius evading monogamy automatically shuckings electromagnetic coatee swallowing padrone dispensaries mexicans opulently monumentally intent homebreds concordantly elitists monopolism crimps catastrophical vulnerable bicepses julius brainier sinker supt sluggishly doctrine revives pupate towability openendedness bagginess transcribing "
,"portaled grouter martha staving convinces glucoses engild slideways brewages recommend retorted duchesses temporalties architecturally sneered nonresidence enfilade attn buxomest delouses whammy humiliation larker inhabiter drowsiness cobbles femaleness redeemability peremptorily fluencies chemosensitivities duality semestrial adsorbates upholder obligator resituating prolix unassailable diminishments manipulating winnable bedazzling whereby libeled theologians attentiveness pillboxes idolisms i"
,"mopeds exemptions finial misfiles dandyism transistors chemoreceptivity pickerels opprobriums pessimist livingly formulary entombment pratfalls libelously yahooism zippier conventionalizing reconsolidates draftsmen playoff dissonant assert belgrade cosecs chamfer outrageously buglers blouses denigrates sequencies nonactives steers reassumed tenantry operated panty white retsina mystifiers eyedropperful management bindweed hansom verbalizing overacted interlaced scavengery spattering lurcher obla"
,"corpuscular malines kit abortiveness beseemed pyramidal scollops vinously loggerhead stockrooms kabob stilbestrol vascularly digraph rapport repressively herpetological shushes toothless huddled backtracks diabetics darklier waning coplots heartlessness reconstitution camellia seral abattoir nonmembership whisper jaywalked misinstruction joggled courteous mandarin wavelets soother marginality guttering maladroit oblong nomadism greenwood postelection cinquefoils dubiety webless marts questor sco"
,"stratocumuli diesels pegless queuers invaluably halberd gluteal administration midbody fault stub recrate transship unthawed coercions lunations slangs moults gracing incompletely circumnavigate impeded inning windiness developments peculates insensateness forevermore unsteady houston assonant dicotyledons douser biotins rebaptized tinny majorem sociosexualities informatively throve bruited grassy hermeneutical reindexed screwier doubter guiltlessly monomaniacs hygienist wearying triune chias bu"
]
words=['lacrosses', 'protectional', 'blistered', 'leaseback', 'assurers', 'frizzlers', 'submerse', 'rankness', 'moonset', 'farcer', 'brickyard', 'stolonic', 'trimmings', 'glottic', 'rotates', 'twirlier', 'stuffer', 'publishable', 'invalided', 'harshens', 'tortoni', 'unlikely', 'alefs', 'gladding', 'favouring', 'particulate', 'baldpates', 'changeover', 'lingua', 'proctological', 'freaking', 'outflanked', 'amulets', 'imagist', 'hyped', 'pilfers', 'overachiever', 'clarence', 'outdates', 'smeltery']

alphabeta="abcdefghijklmnopqrstuvwxyz "
def print_dict_by_seq(dc)  :
    #按照字母顺序显示频率
    for char in "abcdefghijklmnopqrstuvwxzy ":
        if char in dc:
            print("<{}>={:>2} ".format(char,dc[char]),end="")
        else:
            print("<{}>={:>2} ".format(char, 0),end="")
    print()
def distance(a,b):
    a=alphabeta.index(a)
    b=alphabeta.index(b)
    return (a-b)%27
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

def char_freq_anal(ciphertext):
    #接受一段密文，统计每个字符出现的频率
    freq={}
    for char in ciphertext:
        if char in freq:
            freq[char]=freq[char]+1
        else:
            freq[char]=1
    return freq

def plaintext_ciphertext(ciphertext,plaintext):
    L=len(plaintext)
    dc={}
    for i in range(L):
        d=distance(ciphertext[i],plaintext[i])
        if d in dc:
            dc[d]=dc[d]+1
        else:
            dc[d]=1
    print_dict_by_freq(dc)
    print(">>{}<<".format(len(dc.keys())))

def plaintext_ciphertext_with_random(ciphertext,plaintext):
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

    print_dict_by_freq(dc,re=True,n=15)
    print(">>{}<<".format(len(dc.keys())))

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
    shiftcycle=""
    for ct in shifted_ciphertext:
        for i in range(Lc):
            d=distance(ct[i],plaintext[i%Lp])
            if d in dc:
                dc[d]=dc[d]+1
            else:
                dc[d]=1


    print_dict_by_freq(dc,re=True)
    print(">>{}<<".format(len(dc.keys())))





def coin_generation_algorithm(ciphertext_pointer=0,t=0,L=0):
    return random.uniform(0,1)
def no_rand(ciphertext_pointer=0,t=0,L=0):
    return 1
def shifting(char,shift,forward=True):
#xyz abc
    if isinstance(shift,str):
        #abcd
        #1234
        shift_num=ord(shift)-96
        if shift==" ":
            shift_num=27
    if isinstance(shift,int):
        shift_num=shift
    char_num=alphabeta.index(char)
    if forward:
        shifted_num=(char_num+shift_num)%27
    else:
        shifted_num=(char_num-shift_num)%27
    
    return alphabeta[shifted_num]
def shifting_words(string,key,forward=True):
    Ls=len(string)
    Lk=len(key)
    w=""
    for i in range(len(string)):
        w=w+shifting(string[i],key[i%Lk],forward=forward)
    return w

def random_char():
    rdint =random.randint(0,26)
    return alphabeta[rdint]
def key_character_scheduling_algorithm2(message_pointer=0,t=26,L=0):
    #totall random
    return random.randint(0,t-1)
def key_character_scheduling_algorithm(message_pointer=0,t=26,L=0):
    #no random
    return message_pointer%t
    pass
def key_character_scheduling_algorithm1(message_pointer,t,L=0):
    #普通的多码加密
    return message_pointer%t


def cryp1(plaintext,key,coin_gen=coin_generation_algorithm):
    #五个明文的加密
    ciphertext=""
    message_pointer =0
    cipher_pointer=0
    t=len(key)
    for plainchar in plaintext:

        if coin_gen()<0.05:
            ciphertext=ciphertext+random_char()
            cipher_pointer=cipher_pointer+1

        # j=key_character_scheduling_algorithm(message_pointer,)
        j=key_character_scheduling_algorithm2(message_pointer, t=t)
        ciphertext=ciphertext+shifting(plainchar,key[j])
        message_pointer=message_pointer+1
        cipher_pointer=cipher_pointer+1

    return ciphertext

def cryp2(key,coin_gen=coin_generation_algorithm,rdseed=0):
    #随机词典的加密
    L=0
    random.seed(rdseed)
    plaintext=""
    while(L<500):
        plaintext=plaintext+random.choice(words)+" "
        L=len(plaintext)
    ciphertext=""
    message_pointer =0
    cipher_pointer=0
    t=len(key)
    for plainchar in plaintext:

        if coin_gen()<0.05:
            ciphertext=ciphertext+random_char()
            cipher_pointer=cipher_pointer+1

        # j=key_character_scheduling_algorithm(message_pointer,)
        j=key_character_scheduling_algorithm1(message_pointer, t=t)
        ciphertext=ciphertext+shifting(plainchar,key[j])
        message_pointer=message_pointer+1
        cipher_pointer=cipher_pointer+1
    
    return (plaintext,ciphertext)
def test2(ciphertext):
    for w in words:
        #随便选一个当明文，计算秘钥
        L=len(w)
        key=test2_guesskey(w,ciphertext)
        #print("{:20}->{}".format(w,key))
        test2_use_key_to_decryp(key,ciphertext)
    pass
def test2_guesskey(w,ciphertext):
    #返回一个秘钥
    L=len(w)
    key=""
    for i in range(L):
        k=alphabeta.index( ciphertext[i])-alphabeta.index( w[i])-1 
        key=key+alphabeta[k]
    return key;
def test2_use_key_to_decryp(key,ciphertext):
    keyL=len(key)
    
    for i in range(len(ciphertext)-keyL):
        guessword=shifting_words(ciphertext[i:i+keyL],key,forward=False)
        for gs in guessword.split():

            for w in words:
                score=difflib.SequenceMatcher(a=gs,b=w).ratio()
                if score >0.6:
                    print(score)
                    print("{}  {:20}{:20}{:20}".format(i,gs,w,key))
        # print(guessword)
    return 1




if __name__ =="__main__":
    print("haha")
    print(coin_generation_algorithm())
#    print(random_char())
    print(shifting("y",4,forward=True))
    print(shifting("b",4,forward=False))
    key="randomkey"
    # ppl=cryp1(candidates[2],randomkey(7),coin_gen=no_rand)
    # ppl=cryp1(candidates[3],key)
    # printkey(key)
    # print(key)
    # # plaintext_ciphertext(ppl,candidates[1])
    # for i in candidates:

    #     plaintext_ciphertext_with_random(ppl,i)
    #     plaintext_ciphertext_with_random_no_cycle(ppl,i)
    # print(len(ppl))
    key=randomkey(7)
    (ppl,ccl)=cryp2(key=key)
    print(ppl)
    print(ccl)
    printkey(key)
    test2(ccl)
    #favouring
    #xbisidtserc
    shifting_words("favouring",key=key,forward=True)
    shifting_words("xbisidtse",key=key,forward=False)