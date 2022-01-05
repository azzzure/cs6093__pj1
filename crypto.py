from util import *
import random
def coin_generation_algorithm1(ciphertext_pointer=0,t=0,L=0):
    '''random coin'''
    return random.uniform(0,1)
def coin_generation_algorithm2(ciphertext_pointer=0,t=0,L=0):
    '''no random coin'''
    return 1
def random_char():
    rdint =random.randint(0,26)
    return alphabeta[rdint]
def key_character_scheduling_algorithm2(message_pointer=0,t=26,L=0):
    '''totally random'''
    #totall random
    return random.randint(0,t-1)
def key_character_scheduling_algorithm(message_pointer=0,t=26,L=0):
    '''no random'''
    #no random
    return message_pointer%t
    pass
def key_character_scheduling_algorithm1(message_pointer,t,L=0):
    #no random
    return message_pointer%t
def randomkey(t=10):
    #return a random key
    key=[]
    for i in range(t):
        key.append(random.randint(0,26))
    return key
def cryptest1(plaintext,key,coin_gen=coin_generation_algorithm1,sched=key_character_scheduling_algorithm2):
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
        j=sched(message_pointer, t=t)
        ciphertext=ciphertext+shifting(plainchar,key[j])
        message_pointer=message_pointer+1
        cipher_pointer=cipher_pointer+1

    return ciphertext


def cryptest2(key,coin_gen=coin_generation_algorithm1,sched=key_character_scheduling_algorithm2,rdseed=0):
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