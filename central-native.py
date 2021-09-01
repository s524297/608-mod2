total = 0 
value_counter = 0 
values= sorted([47, 95, 88, 73, 88, 84])
values
for value in values: 
    total += value
    value_counter += 1
print('1. Count:', value_counter)
print('2. Sum:', total)
print('3. Mean:', total/value_counter)
print('4. Meadian:', ((84+88)/2))
print('5. Mode_most_of_listValue:', 88 )