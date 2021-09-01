total = 0 
value_counter = 0
values = sorted([47, 95, 88, 73, 88, 84])
values
[47, 73, 84, 88, 88, 95]
import statistics 
print('1. Count: ', len(values))
print('2. Sum:', sum(values))
print('3. Mean:', statistics.mean(values))
print('4. Mode:', statistics.mode(values))
print('5. meadian:', statistics.median(values))
