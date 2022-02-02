from random import choices, seed
import time

""" def LongestCommonDNASeq(s, t):
    r, n = len(s), len(t)
    l = [[0 for _ in range(n)] for _ in range(r)]
    z = 0
    ret = []
    
    for i in range(r):
        for j in range(n):
            if s[i] == t[j]:
                if i == 0 or j == 0:
                    l[i][j] = 1
                else:
                    l[i][j] = l[i-1][j-1] + 1
                if l[i][j] > z:
                    z = l[i][j]
                    ret = s[i-z+1:i+1]
                elif l[i][j] == z:
                    ret += s[i-z+1:i+1]
            else:
                l[i][j] = 0
    return ret """

def LongestCommonDNASeq(s, t):
    if len(t) > len(s):
        s, t = t, s
    r, n = len(s), len(t)
    lookup = [[0 for _ in range(r+1)] for _ in range(2)]
    z = 0
    ret = ""
    
    for i in range(1,r+1):
        for j in range(1,n+1):
            if s[i-1] == t[j-1]:
                lookup[i%2][j] = lookup[(i-1)%2][j-1] + 1
                if lookup[i%2][j] > z:
                    z = lookup[i%2][j]
                    ret = s[i-z:i]
            else:
                lookup[i%2][j] = 0
    return ret


def test(num_tests, dna_length,seed_):
    nucleotide_bases = ["C","T","A","G"]
    times = [0]*num_tests
    
    seed(seed_)
    
    for i in range(num_tests):
        starting_time = time.time()
        dna = "".join(choices(nucleotide_bases,k=dna_length))
        dna_2 = "".join(choices(nucleotide_bases,k=dna_length))
        LongestCommonDNASeq(dna,dna_2)
        times[i] = time.time() - starting_time    
    
    return sum(times)/num_tests



def main():
    from sys import stdin

    dna = stdin.readline().rstrip()
    dna_2 = stdin.readline().rstrip()

    # dna = "AAAACCCTTG"
    # dna_2 = "CCAAAACCTA"
    
    # dna = "GGGGTTATGGGGGATATATATATA"
    # dna_2 = "GTGGGGTTATGGATATATATATG"
    
    print(LongestCommonDNASeq(dna,dna_2))

if __name__ == "__main__":
    main()
    # print(test(1,1300,2048))
