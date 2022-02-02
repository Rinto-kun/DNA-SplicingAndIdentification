#%%
from random import choices,seed
import time

def splice_dna(dna_seq: str, dna_to_search: str, index: int, dna_to_add:str):
    
    # dna_replacement = dna_to_search[:index] + dna_to_add + dna_to_search[index:]
    # dna_seq = dna_seq.replace(dna_to_search,dna_replacement,1)
    # for i in range(len(dna_seq)-len(dna_to_search)):
    #     dna_seq = dna_seq.replace(dna_to_search,dna_replacement,1)
    
    # I leave this one because it exposes what is being done - better,
    # although a bit more unsightly.
    lt = len(dna_to_search)
    i = 0
    while i <= len(dna_seq)-lt:
        # Dynamically acquired as the sequence is being modified in place. 
        # Thanks (3 1 AAA 1 T) and (1 2 A 1 GA) for making this weirder, harder and more computationally expensive.
        j = 0
        while j<lt and dna_seq[i+j] == dna_to_search[j]:
            j += 1
            if j == lt:
                dna_seq = dna_seq[:i+index] + dna_to_add + dna_seq[i+index:]
                i += len(dna_to_add)
        i += 1
    return dna_seq

def test(num_tests, dna_length, length_binding_site, length_splice, splice_index, _seed):
    nucleotide_bases = ["C","T","A","G"]
    times = [0]*num_tests

    seed(_seed)
    for i in range(num_tests):
        start_time = time.perf_counter()
        dna = "".join(choices(nucleotide_bases, k=dna_length))
        
        dna_splice_data = [
            # LENGTH OF BINDING SITE
            length_binding_site,
            # LENGTH OF PATTERN TO BE INSERTED/SPLICED IN
            length_splice,
            # BINDING SITE
            dna[splice_index:splice_index+length_binding_site],
            # INDEX OF INSERTING/SPLICING
            splice_index,
            # PATTERN TO BE INSERTED/SPLICED IN
            "".join(choices(nucleotide_bases,k=length_splice))
        ]
        
        splice_dna(dna,*dna_splice_data[2:])
        
        times[i] = time.perf_counter()-start_time
    return sum(times)/num_tests

def test_construction(num_tests, dna_length, length_binding_site, length_splice, splice_index, _seed):
    nucleotide_bases = ["C","T","A","G"]
    times = [0]*num_tests

    seed(_seed)
    for i in range(num_tests):
        start_time = time.perf_counter()
        dna = "".join(choices(nucleotide_bases, k=dna_length))
        
        dna_splice_data = [
            # LENGTH OF BINDING SITE
            length_binding_site,
            # LENGTH OF PATTERN TO BE INSERTED/SPLICED IN
            length_splice,
            # BINDING SITE
            dna[splice_index:splice_index+length_binding_site],
            # INDEX OF INSERTING/SPLICING
            splice_index,
            # PATTERN TO BE INSERTED/SPLICED IN
            "".join(choices(nucleotide_bases,k=length_splice))
        ]
        
        # splice_dna(dna,*dna_splice_data[2:])
        
        times[i] = time.perf_counter()-start_time
    return sum(times)/num_tests

def test_splicing(num_tests, dna_length, length_binding_site, length_splice, splice_index, _seed):
    nucleotide_bases = ["C","T","A","G"]
    times = [0]*num_tests

    seed(_seed)
    for i in range(num_tests):
        start_time = time.perf_counter()
        dna = "".join(choices(nucleotide_bases, k=dna_length))
        
        dna_splice_data = [
            # LENGTH OF BINDING SITE
            length_binding_site,
            # LENGTH OF PATTERN TO BE INSERTED/SPLICED IN
            length_splice,
            # BINDING SITE
            dna[splice_index:splice_index+length_binding_site],
            # INDEX OF INSERTING/SPLICING
            splice_index,
            # PATTERN TO BE INSERTED/SPLICED IN
            "".join(choices(nucleotide_bases,k=length_splice))
        ]
        
        time_for_construction = time.perf_counter()-start_time

        splice_dna(dna,*dna_splice_data[2:])
        
        times[i] = time.perf_counter()-time_for_construction - start_time
    return sum(times)/num_tests

def main():
    from sys import stdin
    m, n = map(int, stdin.readline().split())
    
    dna = stdin.readline().strip()

    dna_splice = [[None for _ in range(5)] for _ in range(n)]
    for i in range(n):
        splice_data = stdin.readline().split()
        
        # LENGTH OF BINDING SITE
        dna_splice[i][0] = int(splice_data[0])
        
        # LENGTH OF PATTERN TO BE INSERTED/SPLICED IN
        dna_splice[i][1] = int(splice_data[1])
        
        # BINDING SITE
        dna_splice[i][2] = splice_data[2]
        
        # INDEX OF INSERTING/SPLICING
        dna_splice[i][3] = int(splice_data[3])
        
        # PATTERN TO BE INSERTED/SPLICED IN
        dna_splice[i][4] = splice_data[4]
    # print(dna_splice)
    
    for splice in dna_splice:
        dna = splice_dna(dna,*splice[2:])
        print(dna)


if __name__ == "__main__":
    main()
    # dna = "AAAAAA"
    # dna_to_search = "AAA"
    # dna_to_add = "T"
    # print(splice_dna(dna,dna_to_search,3,dna_to_add))
    
    # dna = "CAAT"  
    # dna_to_search = "A"
    # dna_to_add = "GA"
    # print(splice_dna(dna,dna_to_search,1,dna_to_add))
    
    
    # dna = "AATCCGAATTCGTATC"   
    # dna_to_search = "GAATTC"
    # dna_to_add = "TGATA"
    # print(splice_dna(dna,dna_to_search,1,dna_to_add))
