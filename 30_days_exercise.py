import statistics 

class Statistics:
    def __init__(self,ages):
        return None
    
    def count(self):
        return len(ages)
    
    def sum(self):
        total = 0
        for age in ages:
            total += age
        return total
    
    def min(self):
        min = float('inf')
        for age in ages:
            if min > age:
                min = age
        return min
    
    def max(self):
        max = 0
        for age in ages:
            if max < age:
                max = age
        return max
        
    def range(self):
        range = self.max() - self.min()
        return range
    
    def mean(self):
        mean = self.sum() / self.count()
        return round(mean)
        
    def median(self):
        return statistics.median(ages)

    def mode(self):
        return statistics.mode(ages)

    def std(self):
        return statistics.stdev(ages)
    
    def var(self):
        return statistics.variance(ages)
    
    # def freq_dist(self):
    #     return statistics.



ages = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]
data = Statistics(ages)
print('Count:', data.count()) # 25
print('Sum: ', data.sum()) # 744
print('Min: ', data.min()) # 24
print('Max: ', data.max()) # 38
print('Range: ', data.range()) # 14
print('Mean: ', data.mean()) # 30
print('Median: ', data.median()) # 29
print('Mode: ', data.mode()) # {'mode': 26, 'count': 5}
print('Standard Deviation: ', data.std()) # 4.2
print('Variance: ', data.var()) # 17.5
# print('Frequency Distribution: ', data.freq_dist()) # [(20.0, 26), (16.0, 27), (12.0, 32), (8.0, 37), (8.0, 34), (8.0, 33), (8.0, 31), (8.0, 24), (4.0, 38), (4.0, 29), (4.0, 25)]