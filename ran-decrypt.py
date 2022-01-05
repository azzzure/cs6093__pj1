
import crypto
import test1
import test2
from util import *
if __name__ =="__main__":
    # key=randomkey(10)
    # ciphertext=crypto.cryptest1(candidates[3],key,crypto.coin_generation_algorithm1,sched=crypto.key_character_scheduling_algorithm2)
    ciphertext=input("please input ciphertest for test 1\n")
    test1.test1_dec(ciphertext)
    # pliantext,ciphertext=crypto.cryptest2(key,crypto.coin_generation_algorithm1,sched=crypto.key_character_scheduling_algorithm1)
    ciphertext=input("please input ciphertest for test 2\n")
    test2.test2_dec(ciphertext)