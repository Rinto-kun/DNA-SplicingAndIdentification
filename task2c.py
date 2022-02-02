import task2a as t2a
import task2b as t2b
import matplotlib.pyplot as plt
n = 4
# tests = [[20,10**(n-3)],
        #  [20,10**(n-2)],
        #  [20,10**(n-1)],
        #  [20,10**n]
        # ]
# tests = [[20, 200],[20,400],[20,800]]
tests = [[20,9],[20, 10],[20,11],[20,12],[20,13]]
seed = 2048

def test_2a():
    results = [0]*len(tests)
    for i in range(len(tests)):
        results[i] = t2a.test(*tests[i],seed)
        print(f"2a: Done with test {tests[i]}. Time elapsed: {results[i]}")
    return results

def test_2b():
    results = [0]*len(tests)
    for i in range(len(tests)):
        results[i] = t2b.test(*tests[i],seed)
        print(f"2b: Done with test {tests[i]}. Time elapsed: {results[i]}")
    return results

def main():
    x_axis = [test[1] for test in tests]
    
    results_2a = test_2a()
    
    results_2b = test_2b()

    # results_2b = [0.0002,0.009,0.909,28.635]
    
    fig, ax = plt.subplots()
    plt.plot(x_axis,results_2b, label="DP")
    plt.plot(x_axis,results_2a, label="Recursion")
    ax.legend()
    
    ax.set(title="Performance", xlabel ="Length of strands", ylabel ="Time (s)",xscale="linear")
    # fig.savefig("test.png")
    plt.show()

if __name__ == "__main__":
    main()