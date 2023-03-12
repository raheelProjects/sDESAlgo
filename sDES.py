import random

lst =[random.randint(0,1) for x in range(10)]
key ="".join(map(str,lst))

def keys(key):

    def passwithtable(num):
        return key[num-1]

    def performls(word,shifting=1):
        last = word[:shifting]
        first = word[shifting:]
        return first+last

    p10 = [3,5,2,7,4,10,1,9,8,6]
    p8 =[6,3,7,4,8,5,10,9]
    print("Step 1 : Passing with p10 table")
    print("before :"+key)
    newstate="".join(map(passwithtable,p10))
    print("after :",newstate)
    print("\n step 2 : break into two half")
    half =int(len(newstate)/2)
    left = newstate[:half]
    right =newstate[half:]
    print(f"l = {left}  r= '{right}' ")

    print("\n step 3 : perform left shift")
    left = performls(left)
    right = performls(right)

    print(f"l = {left}  r= '{right}' ")

    print("\n step 4: pass step3 with p8 table")
    key = left+right
    k1 = "".join(map(passwithtable,p8))

    print(f"k1 = {k1}")

    print("\n step 5 : perform left shift 2 on step 3")
    left = performls(left,shifting=2)
    right = performls(right,shifting=2)

    print(f"l = {left}  r= '{right}' ")

    print("\n step 5: pass step 5 with p8 table")
    key = left+right
    k2 = "".join(map(passwithtable,p8))

    print(f"k2 = {k2}")

    return k1,k2


k1,k2 =keys(key)

print(f"\n final result \n k1: {k1} \n k2: {k2}")

def s_des():
    plaintext="01110010"


    # identify
    iptable = [2,6,3,1,4,8,5,7]
    eptable = [4,1,2,3,2,3,4,1]
    p4 = [2,4,3,1]
    ipinversetable =[4,1,3,5,7,2,8,6]

    sobox ={
    "00":{"00":1,"01":0,"10":3,"11":2},
    "01":{"00":3,"01":2,"10":1,"11":0},
    "10":{"00":0,"01":2,"10":1,"11":3},
    "11":{"00":3,"01":1,"10":3,"11":2}
    }

    s1box ={
    "00":{"00":0,"01":1,"10":2,"11":3},
    "01":{"00":2,"01":0,"10":1,"11":3},
    "10":{"00":3,"01":0,"10":1,"11":0},
    "11":{"00":2,"01":1,"10":0,"11":3}
    }

    convertion ={
        0:"00",
        1:"01",
        2:"10",
        3:"11"
    }

    # functions

    def passwithtable(num):
        return plaintext[num-1]
    
    def passRight(num):
        return right[num-1]
    
    def passwithp4(num):
        return str(so+s1)[num-1]
    
    def xor(word,key):
        lst =[0 if word[x]==key[x] else 1 for x in range(len(key))]
        return "".join(map(str,lst))

    # solution

    print("Step 1 : Passing with ip table")
    print("before :"+plaintext)
    newstate="".join(map(passwithtable,iptable))
    print("after :"+newstate)
    print("\n step 2 : break into two half")
    half =int(len(newstate)/2)
    left = newstate[:half]
    right =newstate[half:]
    print(f"l = {left}  r= '{right}' ")

    print("\n step 3 : pass right with e/p table")
    rightnew = "".join(map(passRight,eptable))
    print(f"=> {rightnew} ")

    print("\n step 4 : xor with k1")
    rightnew =xor(rightnew,k1)
    print(f"=> {rightnew} ")
    half =int(len(rightnew)/2)
    left2 = rightnew[:half]
    right2 =rightnew[half:]
    print(f"l = {left2}  r= '{right2}' ")

    print("\n step 5 : pass left with so box and right with s1box")
    so = convertion[sobox[left2[0]+left2[-1]][left2[1:3]]]
    print(f"left = {left2} => {so}")
    s1 = convertion[s1box[right2[0]+right2[-1]][right2[1:3]]]
    print(f"right = {right2} => {s1}")

    print("\n step 6 : rearrange step 5 and pass with p4 table ")
    val = "".join(map(passwithp4,p4))
    print(f"{so+s1} ==> {val}")

    print("\n step 7 : xor step 6 with left of step 2 ")
    val = xor(val,left)
    print(f"after xor  => {val}")

    print("\n step 8 : re arrange step 7 as left and step 2 as right and then switch them ")
    left,right = val,right
    print(f"left ={left} , right = {right}",end="")
    left,right = right,left
    print(f" ==> left ={left} , right = {right}")

    print("\n step 9 : pass right with e/p table")
    rightnew = "".join(map(passRight,eptable))
    print(f"=> {rightnew} ")

    print("\n step 10 : xor with k2")
    rightnew =xor(rightnew,k2)
    print(f"=> {rightnew} ")
    half =int(len(rightnew)/2)
    left2 = rightnew[:half]
    right2 =rightnew[half:]
    print(f"l = {left2}  r= '{right2}' ")

    print("\n step 11 : pass left with so box and right with s1box")
    so = convertion[sobox[left2[0]+left2[-1]][left2[1:3]]]
    print(f"left = {left2} => {so}")
    s1 = convertion[s1box[right2[0]+right2[-1]][right2[1:3]]]
    print(f"right = {right2} => {s1}")

    print("\n step 12 : rearrange and pass with p4 table ")
    val = "".join(map(passwithp4,p4))
    print(f"{so+s1} ==> {val}")

    print("\n step 13 : xor with left of step 8 ")
    val = xor(val,left)
    print(f"after xor  => {val}")

    print("\n step 14 : re arrange step 13 as left and step 8 as right and then pass with ip-1 table ")
    newstate = val+right

    ct = "".join(map(lambda x: newstate[x-1],ipinversetable))

    print(f" plaintext : {plaintext} =====> ciphertext : {ct}")

    an_integer = int(plaintext, 2)
    ascii_character = chr(an_integer)
    an_ = int(ct, 2)
    ascii_ = chr(an_)

    print(f"plaintext : {ascii_character}  to ct :{ascii_}")

s_des()