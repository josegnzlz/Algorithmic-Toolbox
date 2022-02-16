values = [10, 5, 6, 12, 20, 8, 7]
weights = [5, 5, 2, 2, 10, 2, 1]

compute = [values[i] / weights[i] for i in range(0,len(values))]

print(compute)

zipped_lists = zip(compute, values, weights)
sorted_zipped_lists = sorted(zipped_lists, reverse=True)

values_sorted = [value for _, value, _ in sorted_zipped_lists]
weights_sorted = [weight for _, _, weight in sorted_zipped_lists]
print(weights_sorted)
print(values_sorted)