from scipy.stats import t
import math
# ENSURE: input a non-empty lists of sample data
# ASSERT: output sample size, mean, and standard deviation as a 3-tuple
def parameter(sample):
    sample_size = len(sample)
    sample_average = sum(sample) / sample_size
    sqr_sum = 0
    for elem in sample:
        sqr_sum += (elem - sample_average) ** 2
    return (sample_size, sample_average, (sqr_sum / (sample_size - 1)) ** .5)
        
# ENSURE: input a positive integer for size and alpha
# ASSERT: output the corresponding critical value
def critical_value(size, prob):
    df = size - 1
    val = t.ppf(prob, df)
    return val
    
# Grubbs Test
# ENSURE: input a non-empty list and confidence interval
# ASSERT: output outlier if exists
def Grubbs(sample, confidence):
    sample_size, sample_average, sample_deviation = parameter(sample)
    critical_val = critical_value(sample_size, confidence)
    max_outlier = -float('inf')
    max_g = 0
    max_idx = -1
    for i in range(sample_size):
        G_exp = abs(sample[i] - sample_average) / sample_deviation
        if (G_exp > critical_val):
            max_outlier = sample[i]
            max_idx = i
            max_g = G_exp
    if (max_idx == -1):
        print("No outliers found")
        return ((False, None))
    else:
        print("%0.2f is an outlier, since %0.2f > %0.2f" 
            % (max_outlier, max_g, critical_val))
        return ((True, max_outlier))

#test cases
Grubbs([4.51,4.63,4.49,4.45,4.90,4.59],.95)
