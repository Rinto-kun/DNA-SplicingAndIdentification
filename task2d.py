from task2b import LongestCommonDNASeq
from itertools import combinations

def LongestCommonDNASeqBetweenKStrands(dna_strands,k):
    res = []
    for dna_comb in combinations(dna_strands,r=k):
        maxi = dna_comb[0]
        for strand in dna_comb[1:]:
            maxi = LongestCommonDNASeq(strand,maxi)
        res.append(maxi)
    return sorted(res,key=len)[-1]

def main():
    from sys import stdin

    n, m, l = map(int,stdin.readline().split()) # n - number of strands to compare, 
    dna = ["" for _ in range(n)]                # m - number of strands needing to share it, l - length of strands
    for i in range(n):
        dna[i] = stdin.readline().rstrip()
    print(LongestCommonDNASeqBetweenKStrands(dna,m))

if __name__ == "__main__":
    main()