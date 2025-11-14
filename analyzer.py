import numpy as np

print("="*60)
print("📊 NumPy Data Analyzer")
print("="*60)

while True:
  try:
    data_num = int(input("How many numbers do you want to enter?: "))
    break
  except ValueError:
    print("Please enter numerical values only!")

while True:
  try:
    values =[int(input(f"Enter value {i + 1}: ")) for i in range(data_num)]
    print("~" * 60)
    break
  except ValueError:
    print("Please enter numerical values only!")


array = np.array(values)

print("Data Analysis report📊")
print("~" * 60)
print(f"Count              :- {array.size}")
print(f"Mean               :- {np.mean(array):.2f}")
print(f"Median             :- {np.median(array):.2f}")
print(f"Standard deviation :- {np.std(array):.2f}")
print(f"Maximum value      :- {np.max(array)}")
print(f"Minimum value      :- {np.min(array)}")
print(f"Above Mean         :- {np.sort(array[array > np.mean(array)])}")
print(f"Normalized Data    :- {np.round((array - array.min()) / (array.max() - array.min()), 3)}")
print("~" * 60)
