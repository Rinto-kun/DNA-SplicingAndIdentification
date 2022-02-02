import task1a as t1a
import task1bi as t1bi
import task1bii as t1bii
import matplotlib.pyplot as plt
power = 7
seed = 2048
numtests = 20
tests = [
            [numtests, 10**power, 10, 10, 10],
            [numtests, 10**power, 100, 10, 10],
            [numtests, 10**power, 1000, 10, 10]]
# tests = [
#             [numtests, 15000000, 10, 10, 10],
#             [numtests, 15000000, 100, 10, 10],
#             [numtests, 15000000, 1000, 10, 10]]
def test_1a():
    results = [0]*len(tests)
    for i in range(len(tests)):
        results[i] = t1a.test(*tests[i],seed)
        print(f"1a:\tDone with test {tests[i]}. \tTime elapsed: {results[i]}")
    return results
def test_1bi():
    results = [0]*len(tests)
    for i in range(len(tests)):
        results[i] = t1bi.test(*tests[i],seed)
        print(f"1bi:\tDone with test {tests[i]}. \tTime elapsed: {results[i]}")
    return results
def test_1bii():
    results = [0]*len(tests)
    for i in range(len(tests)):
        results[i] = t1bii.test(*tests[i],seed)
        print(f"1bii:\tDone with test {tests[i]}. \tTime elapsed: {results[i]}")
    return results


def test_1a_construction():
    results = [0]*len(tests)
    for i in range(len(tests)):
        results[i] = t1a.test_construction(*tests[i],seed)
        print(f"1a:\tDone with test {tests[i]}. \tTime elapsed: {results[i]}")
    return results
def test_1bi_construction():
    results = [0]*len(tests)
    for i in range(len(tests)):
        results[i] = t1bi.test_construction(*tests[i],seed)
        print(f"1bi:\tDone with test {tests[i]}. \tTime elapsed: {results[i]}")
    return results
def test_1bii_construction():
    results = [0]*len(tests)
    for i in range(len(tests)):
        results[i] = t1bii.test_construction(*tests[i],seed)
        print(f"1bii:\tDone with test {tests[i]}. \tTime elapsed: {results[i]}")
    return results

def test_1a_splicing():
    results = [0]*len(tests)
    for i in range(len(tests)):
        results[i] = t1a.test_splicing(*tests[i],seed)
        print(f"1a:\tDone with test {tests[i]}. \tTime elapsed: {results[i]}")
    return results
def test_1bi_splicing():
    results = [0]*len(tests)
    for i in range(len(tests)):
        results[i] = t1bi.test_splicing(*tests[i],seed)
        print(f"1bi:\tDone with test {tests[i]}. \tTime elapsed: {results[i]}")
    return results
def test_1bii_splicing():
    results = [0]*len(tests)
    for i in range(len(tests)):
        results[i] = t1bii.test_splicing(*tests[i],seed)
        print(f"1bii:\tDone with test {tests[i]}. \tTime elapsed: {results[i]}")
    return results

def test_splicing():
    x_axis = [n[2] for n in tests]
    results_a = test_1a_splicing()
    results_bi = test_1bi_splicing()
    results_bii = test_1bii_splicing()
    
    fig, ax = plt.subplots()
    plt.plot(x_axis,results_a, label="String")
    plt.plot(x_axis,results_bi, label="Linked List Linear")
    plt.plot(x_axis,results_bii, label="Linked List Hash")
    ax.legend()
    
    ax.set(title="Performance of splice_dna", xlabel ="Length of splice", ylabel ="Time (s)"
        #    ,xscale="log"
    )
    # fig.savefig("test.png")
    plt.show()
    
def test_construction():
    x_axis = [n[2] for n in tests]
    results_a = test_1a_construction()
    results_bi = test_1bi_construction()
    results_bii = test_1bii_construction()
    
    fig, ax = plt.subplots()
    plt.plot(x_axis,results_a, label="String")
    plt.plot(x_axis,results_bi, label="Linked List Linear")
    plt.plot(x_axis,results_bii, label="Linked List Hash")
    ax.legend()
    
    ax.set(title="Performance of Construction", xlabel ="Length of splice", ylabel ="Time (s)"
        #    ,xscale="log"
    )
    # fig.savefig("test.png")
    plt.show()

def test_general():
    x_axis = [n[2] for n in tests]
    results_a = test_1a()
    results_bi = test_1bi()
    results_bii = test_1bii()
    
    fig, ax = plt.subplots()
    plt.plot(x_axis,results_a, label="String")
    plt.plot(x_axis,results_bi, label="Linked List Linear")
    plt.plot(x_axis,results_bii, label="Linked List Hash")
    ax.legend()
    
    ax.set(title="Performance of LL vs String", xlabel ="Length of splice", ylabel ="Time (s)"
        #    ,xscale="log"
    )
    # fig.savefig("test.png")
    plt.show()

def main():
    test_general()
    test_construction()
    test_splicing()
    # x_axis = [n[2] for n in tests] #15mil
    # results_a = [7.405,7.275,6.712]
    # results_bi = [34.801,33.237,35.970]
    # results_bii = [48.340,48.208,43.562]    

if __name__ == "__main__":
    main()