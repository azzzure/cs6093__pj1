import random
candidates=[
 "dispossess drencher barstool interval cardiacs vixens mooncalves tinnily perineal panamanian unparalleled unsoundness goalkeeper torchier eclat bartisans jewed claudius evading monogamy automatically shuckings electromagnetic coatee swallowing padrone dispensaries mexicans opulently monumentally intent homebreds concordantly elitists monopolism crimps catastrophical vulnerable bicepses julius brainier sinker supt sluggishly doctrine revives pupate towability openendedness bagginess transcribing "
,"portaled grouter martha staving convinces glucoses engild slideways brewages recommend retorted duchesses temporalties architecturally sneered nonresidence enfilade attn buxomest delouses whammy humiliation larker inhabiter drowsiness cobbles femaleness redeemability peremptorily fluencies chemosensitivities duality semestrial adsorbates upholder obligator resituating prolix unassailable diminishments manipulating winnable bedazzling whereby libeled theologians attentiveness pillboxes idolisms i"
,"mopeds exemptions finial misfiles dandyism transistors chemoreceptivity pickerels opprobriums pessimist livingly formulary entombment pratfalls libelously yahooism zippier conventionalizing reconsolidates draftsmen playoff dissonant assert belgrade cosecs chamfer outrageously buglers blouses denigrates sequencies nonactives steers reassumed tenantry operated panty white retsina mystifiers eyedropperful management bindweed hansom verbalizing overacted interlaced scavengery spattering lurcher obla"
,"corpuscular malines kit abortiveness beseemed pyramidal scollops vinously loggerhead stockrooms kabob stilbestrol vascularly digraph rapport repressively herpetological shushes toothless huddled backtracks diabetics darklier waning coplots heartlessness reconstitution camellia seral abattoir nonmembership whisper jaywalked misinstruction joggled courteous mandarin wavelets soother marginality guttering maladroit oblong nomadism greenwood postelection cinquefoils dubiety webless marts questor sco"
,"stratocumuli diesels pegless queuers invaluably halberd gluteal administration midbody fault stub recrate transship unthawed coercions lunations slangs moults gracing incompletely circumnavigate impeded inning windiness developments peculates insensateness forevermore unsteady houston assonant dicotyledons douser biotins rebaptized tinny majorem sociosexualities informatively throve bruited grassy hermeneutical reindexed screwier doubter guiltlessly monomaniacs hygienist wearying triune chias bu"
]
words=['lacrosses', 'protectional', 'blistered', 'leaseback', 'assurers', 'frizzlers', 'submerse', 'rankness', 'moonset', 'farcer', 'brickyard', 'stolonic', 'trimmings', 'glottic', 'rotates', 'twirlier', 'stuffer', 'publishable', 'invalided', 'harshens', 'tortoni', 'unlikely', 'alefs', 'gladding', 'favouring', 'particulate', 'baldpates', 'changeover', 'lingua', 'proctological', 'freaking', 'outflanked', 'amulets', 'imagist', 'hyped', 'pilfers', 'overachiever', 'clarence', 'outdates', 'smeltery']

alphabeta="abcdefghijklmnopqrstuvwxyz "

def distance(a,b):
    a=alphabeta.index(a)
    b=alphabeta.index(b)
    return (a-b)%27

def print_dict_by_seq(dc)  :
    #按照字母顺序显示频率
    for char in "abcdefghijklmnopqrstuvwxzy ":
        if char in dc:
            print("<{}>={:>2} ".format(char,dc[char]),end="")
        else:
            print("<{}>={:>2} ".format(char, 0),end="")
    print()
def extract_max_n_freq(dc,n=6):
    v=list(dc.values())
    v=sorted(v,reverse=True)

    return v[0:n]
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
    return kv[0]

def char_freq_anal(ciphertext):
    #接受一段密文，统计每个字符出现的频率
    freq={}
    for char in ciphertext:
        if char in freq:
            freq[char]=freq[char]+1
        else:
            freq[char]=1
    return freq

def printkey(key):
    keystr=""
    for i in key:
        keystr=keystr+chr(i+97)
    print(keystr)
    return keystr
def shifting(char,shift,forward=True):
    #shift a char
    if isinstance(shift,str):
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
    #shift a words
    Ls=len(string)
    Lk=len(key)
    w=""
    for i in range(len(string)):
        w=w+shifting(string[i],key[i%Lk],forward=forward)
    return w
def randomkey(t=10):
    key=[]
    for i in range(t):
        key.append(random.randint(0,26))
    return key
