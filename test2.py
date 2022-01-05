from util import *
import difflib
def test2_dec(ciphertext):
    score=[]
    for w1 in words:

        L=len(w1)
        key=test2_guesskey(w1,ciphertext)
        #print("{:20}->{}".format(w,key))
        score.append(test2_use_key_to_decryp(key,ciphertext))
    # print(score)
    firstword_index= score.index(max(score))
    firstword=words[firstword_index]
    guessedkey=test2_guesskey(firstword,ciphertext)
    print("{}".format(firstword))
    test2_key_gen_plaintext(guessedkey,ciphertext)

    pass
def test2_key_gen_plaintext(guessedkey,ciphertext):
    keyL=len(guessedkey)
    for i in range(len(ciphertext)-keyL):
        guessword=shifting_words(ciphertext[i:i+keyL],guessedkey,forward=False)
        for gs in guessword.split():
            for w in words:
                score=difflib.SequenceMatcher(a=gs,b=w).ratio()
                if score>0.7:
                    print("{}".format(w),end=" ")
                
    pass
def test2_guesskey(w,ciphertext):
    #返回一个秘钥
    L=len(w)
    key=""
    for i in range(L):
        k=alphabeta.index(ciphertext[i])-alphabeta.index(w[i])-1 
        key=key+alphabeta[k]
    return key;
def test2_use_key_to_decryp(key,ciphertext):
    keyL=len(key)
    score=0
    for i in range(len(ciphertext)-keyL):
        guessword=shifting_words(ciphertext[i:i+keyL],key,forward=False)
        for gs in guessword.split():
            for w in words:
                ratio=difflib.SequenceMatcher(a=gs,b=w).ratio()
                if ratio >0.6:
                    score=score+1
        # print(guessword)
    return score