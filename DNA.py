import numpy as np

def BilistToDNA(data):
    '''
    二进制字符串转DNA
    data: list 二进制字符 表示方法为["1010100101101111","1010100101100110"]
    output list DNA序列 表示方法为['GGGCCGTT', 'GGGCCGCG']
    '''

    A = "00"
    G = "10"
    C = "01"
    T = "11"
    output =[]
    for i in data:
        s = ""
        j=0
        while(j<len(i)):
            str1 = i[j:j+2]
            if str1 == A:
                s+="A"
            if str1 == G:
                s+="G"
            if str1 == C:
                s+="C"
            if str1 == T:
                s+="T"
            j+=2
        output.append(s)
    return output
#print(BistrToDNA(["1010100101101111","1010100101100110"]))

def BistrToDNA(rule,data, split = False):
    '''
    二进制字符串转DNA
    rule: int 将转化的DNA字符串按rule分区 此时output变为 ['GGGCCGTT', 'GGGCCGCG']
    data:  二进制字符串 "10101001011011111010100101100110"
    split: bool类型 True表示需要将DNA进行分块 False反之
    output: 输出 如果split为FalseDNA序列串 表示方法为'GGGCCGTTGGGCCGCG' 反之output变为 ['GGGCCGTT', 'GGGCCGCG']
    '''
    A = "00"
    G = "10"
    C = "01"
    T = "11"
    if split:
        s = ""
        output = []
        j = 0
        i = 0
        while (j < len(data)):
            i += 1
            str1 = data[j:j + 2]
            if str1 == A:
                s += "A"
            if str1 == G:
                s += "G"
            if str1 == C:
                s += "C"
            if str1 == T:
                s += "T"
            j += 2
            if (i % rule == 0):
                output.append(s)
                s = ""
    else:
        output =""
        j = 0
        while(j<len(data)):
            str1 = data[j:j+2]
            if str1 == A:
                output+="A"
            if str1 == G:
                output+="G"
            if str1 == C:
                output+="C"
            if str1 == T:
                output+="T"
            j+=2
    return output


def substraction(m,n):
    if m == n :
        v = "A"
    elif( n =="A"):
        v = m
    elif(m == "T"):
        if n == "G":
            v = "C"
        if m == "C":
            v = "G"
    elif((m == "C" and n == "G") or (m == "A" and n == "C") or (m == "G" and n =="T")):
        v = "T"
    elif((m == "A" and n == "G") or (m == "C"  and n == "T")):
        v = "G"
    elif((m== "G" and n == "C") or (m == "A" and n == "T")):
        v = "C"

    return v

def add(m,n):
    if m == "A" :
        v = n
    elif n=="A":
        v = m
    elif  (m == "G" and n == "C") or (m =="C" and n=="G"):
        v = "T"
    elif m == "G" and m =="G":
        v = "A"
    elif (m == "T" and n == "T") or (m =="C" and n == "C"):
        v = "G"
    elif (m == "C" and n == "T") or (m == "T" and n == "C"):
        v = "A"
    elif (m == "G" and n == "T") or (m == "T" and n == "G" ):
        v = "C"
    return v

#DNA加法
def add_DNA(dna1,dna2):
    '''
    :param dna1: list DNA序列 表示["1010100101101111","1010100101100110"]
    :param dna2: list DNA序列 表示["1010100101101111","1010100101100110"]
    :return: result list序列  表示['AAAGGAGG', 'AAAGGAGA']
    '''
    result = []
    for i,j in zip(dna1,dna2):
        str1 = ""
        for m,n in zip(range(len(i)),range(len(j))):
            value = add(i[m],j[n])
            str1+=value
        result.append(str1)
    return result

#DNA减法
def sub_DNA(dna1,dna2):
    '''
      :param dna1: list DNA序列 表示["1010100101101111","1010100101100110"]
      :param dna2: list DNA序列 表示["1010100101101111","1010100101100110"]
      :return: result list序列  表示['AAAAAAAA', 'AAAAAAAA']
      '''
    result = []
    for i, j in zip(dna1, dna2):
        i = list(i)
        j = list(j)
        str1 = ""
        for m, n in zip(i, j):
            value = substraction(m, n)
            str1 += value
        result.append(str1)
    return result

# result = sub_DNA(BilistToDNA(["1010100101101111","1010100101100110"]),BilistToDNA(["1010100101101111","1010100101100110"]))
# # print(BistrToDNA(8,"10101001011011111010100101100110",split=True))
# print(result)
