import functools
import sys
sys.setrecursionlimit(2**31-1)

# @functools.lru_cache(maxsize=None) # cache makes it a lot faster (still not faster than DP) but I suppose it's not what the assignment expects
def LongestCommonDNASeq(x,y, m, n, dna_seq):
    # Demonstrating the beauty of Python, here is a one-line solution.
    # return dna_seq if (m<=0 or n<=0) else max(LongestCommonDNASeq(x,y,m-1,n-1,x[m-1]+dna_seq) if x[m-1]==y[n-1] else dna_seq, LongestCommonDNASeq(x,y,m,n-1,""), LongestCommonDNASeq(x,y,m-1,n,""), key=len)

    if m<= 0 or n <= 0:
        return dna_seq
    return max(LongestCommonDNASeq(x,y,m-1,n-1,x[m-1]+dna_seq) if x[m-1]==y[n-1] else dna_seq, 
               LongestCommonDNASeq(x,y,m,n-1,""), 
               LongestCommonDNASeq(x,y,m-1,n,""), key=len)


def test(num_tests, dna_length,seed_):
    from random import choices,seed
    from time import time
    nucleotide_bases = ["C","T","A","G"]
    times = [0]*num_tests
    
    seed(seed_)
    for i in range(num_tests):
        starting_time = time()
        dna = "".join(choices(nucleotide_bases,k=dna_length))
        dna_2 = "".join(choices(nucleotide_bases,k=dna_length))
        LongestCommonDNASeq(dna,dna_2,len(dna),len(dna_2),"")
        times[i] = time() - starting_time
    
    return sum(times)/num_tests

def main():
    from sys import stdin
    dna = stdin.readline().rstrip()
    dna_2 = stdin.readline().rstrip()
    
    # dna = "GAAAACCCTTG"
    # dna_2 = "GCCAAAACCTA"
    print(LongestCommonDNASeq(dna,dna_2,len(dna),len(dna_2),""))

if __name__ == "__main__":
    main()
    # print(test(1,12,2048))         # More than 890 breaks for now.