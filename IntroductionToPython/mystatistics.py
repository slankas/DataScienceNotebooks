"""mystatistics provides implementations of common descriptive statistical functions
   - min
   - max
   - range
   - mean
   - median
   - variance
   - std_dev

   Each funtion takes a single list.  All contents of that should be a float or an integer
"""

def min(l):
    """ returns the minimum value in the list.  Raises exception if empty"""
    if l:
        s_list = sorted(l)
        return s_list[0]
    else:
        raise ValueError("list empty")

def max(l):
    """ returns the maximum value in the list.  Raises exception if empty"""
    if l:
        s_list = sorted(l)
        return s_list[-1]
    else:
        raise ValueError("list empty")
        
def range(l):
    """ returns the difference between the minimum and maximum value in the list.  Raises exception if empty"""
    if l:
        s_list = sorted(l)
        return s_list[-1] - s_list[0]
    else:
        raise ValueError("list empty")
        
        
def mean(l):
    """computes the mean of the list"""
    if l:
        return sum(l)/len(l)
    else:
        raise ValueError("list empty")

def median(l):
    """Finds the median value of the list"""
    if l:
        s_list = sorted(l)
        return s_list[len(s_list)//2] if len(s_list)%2 == 1 else (s_list[len(s_list)//2] +s_list[1 +len(s_list)//2])/2
    else:
        raise ValueError("list empty")
    
def variance(l):
    """Calculates the population variance for the list"""
    m   = mean(l)
    dif = 0
    for x in l:
        dif += (m-x)**2
    return dif/len(l)

def std_dev(l):
    """Calculates the population standard deviation for list"""
    return variance(l)**.5

if __name__ == "__main__":
    test_list = [10,12,14]
    print("Min:", min(test_list))
    print("Max:", max(test_list))
    print("Range:", range(test_list))
    print("Mean:", mean(test_list))
    print("Median:", median(test_list))
    print("Variance:", variance(test_list))
    print("Std Dev:", std_dev(test_list))