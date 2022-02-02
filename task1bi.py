from random import choices,seed
import time
from LinkedList import LinkedList

def splice_dna(dna_seq: LinkedList, dna_to_search: LinkedList, index:int, dna_to_add: LinkedList):
    cur = dna_seq.head # making a reference to it

    while cur is not None:

        val = cur
        node = dna_to_search.head
        while val is not None and val == node:
            node = node.next
            
            if node is None:
                cur = cur.insert_nodes(dna_to_add,index)
                break
            val = val.next
        cur = cur.next

    return dna_seq

def test(num_tests, dna_length, length_binding_site, length_splice, splice_index, _seed):
    nucleotide_bases = ["C","T","A","G"]
    times = [0]*num_tests
    
    seed(_seed)
    
    for i in range(num_tests):
        
        start_time = time.perf_counter()
        
        strand = "".join(choices(nucleotide_bases, k=dna_length))
        dna = LinkedList(strand)
        
        dna_to_search = LinkedList(strand[splice_index:splice_index+length_binding_site])
        
        dna_to_splice = LinkedList("".join(choices(nucleotide_bases,k=length_splice)))
        
        dna_splice_data = [
            # LENGTH OF BINDING SITE
            length_binding_site,
            # LENGTH OF PATTERN TO BE INSERTED/SPLICED IN
            length_splice,
            # BINDING SITE
            dna_to_search,
            # INDEX OF INSERTING/SPLICING
            splice_index,
            # PATTERN TO BE INSERTED/SPLICED IN
            dna_to_splice
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
        
        strand = "".join(choices(nucleotide_bases, k=dna_length))
        dna = LinkedList(strand)
        
        dna_to_search = LinkedList(strand[splice_index:splice_index+length_binding_site])
        
        dna_to_splice = LinkedList("".join(choices(nucleotide_bases,k=length_splice)))
        
        dna_splice_data = [
            # LENGTH OF BINDING SITE
            length_binding_site,
            # LENGTH OF PATTERN TO BE INSERTED/SPLICED IN
            length_splice,
            # BINDING SITE
            dna_to_search,
            # INDEX OF INSERTING/SPLICING
            splice_index,
            # PATTERN TO BE INSERTED/SPLICED IN
            dna_to_splice
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
        
        strand = "".join(choices(nucleotide_bases, k=dna_length))
        dna = LinkedList(strand)
        
        dna_to_search = LinkedList(strand[splice_index:splice_index+length_binding_site])
        
        dna_to_splice = LinkedList("".join(choices(nucleotide_bases,k=length_splice)))
        
        dna_splice_data = [
            # LENGTH OF BINDING SITE
            length_binding_site,
            # LENGTH OF PATTERN TO BE INSERTED/SPLICED IN
            length_splice,
            # BINDING SITE
            dna_to_search,
            # INDEX OF INSERTING/SPLICING
            splice_index,
            # PATTERN TO BE INSERTED/SPLICED IN
            dna_to_splice
        ]
        
        time_for_construction = time.perf_counter()-start_time
        
        splice_dna(dna,*dna_splice_data[2:])
        
        times[i] = time.perf_counter()- time_for_construction - start_time
    return sum(times)/num_tests

def main():
    from sys import stdin
    m, n = map(int, stdin.readline().split()) # m - length of strand, n - number of splices
    
    dna = LinkedList(stdin.readline().rstrip())

    dna_splice = [[None for _ in range(5)] for _ in range(n)]
    for i in range(n):
        splice_data = stdin.readline().rstrip().split()
        
        # LENGTH OF BINDING SITE
        dna_splice[i][0] = int(splice_data[0])
        
        # LENGTH OF PATTERN TO BE INSERTED/SPLICED IN
        dna_splice[i][1] = int(splice_data[1])
        
        # BINDING SITE
        dna_splice[i][2] = LinkedList(splice_data[2])
        
        # INDEX OF INSERTING/SPLICING
        dna_splice[i][3] = int(splice_data[3])
        
        # PATTERN TO BE INSERTED/SPLICED IN
        dna_splice[i][4] = LinkedList(splice_data[4])
    # print(dna_splice)
    
    for splice in dna_splice:
        dna = splice_dna(dna,*splice[2:])
        # print(dna)
    print(dna)

if __name__ == "__main__":
    main()
    
    # dna = LinkedList("AAAAAA")    
    # dna_to_search = LinkedList("AAA")
    # dna_to_add = LinkedList("T")
    # print(splice_dna(dna,dna_to_search,1,dna_to_add))
    
    # dna = LinkedList("CAAT")    
    # dna_to_search = LinkedList("A")
    # dna_to_add = LinkedList("GA")
    # print(splice_dna(dna,dna_to_search,1,dna_to_add))
    
    # dna = LinkedList("AATCCGAATTCGTATC")    
    # dna_to_search = LinkedList("GAATTC")
    # dna_to_add = LinkedList("TGATA")
    # print(splice_dna(dna,dna_to_search,1,dna_to_add))