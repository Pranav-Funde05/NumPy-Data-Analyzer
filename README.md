
# 📊 NumPy Data Analyzer

A simple and beginner-friendly Python project that uses **NumPy** to analyze numerical datasets.  
You enter a list of numbers, and the program instantly computes useful statistics like mean, median, standard deviation, range values, and also provides a normalized version of your dataset.

This project is perfect for beginners learning:
- Python basics  
- Exception handling  
- NumPy fundamentals  
- Data preprocessing concepts  

---

## 🚀 Features
- Takes user input safely (with error handling)
- Converts the list into a NumPy array
- Calculates:
  - ✔ Count  
  - ✔ Mean  
  - ✔ Median  
  - ✔ Standard Deviation  
  - ✔ Max & Min  
  - ✔ Values above mean  
  - ✔ Normalized dataset  
- Clean and well-formatted output
- Beginner-friendly and easy to expand

---

## 🧠 What You Learn From This Project
- Using `numpy.mean()`, `numpy.median()`, `numpy.std()`
- Boolean indexing (`array[array > mean]`)
- Normalization formula:
  ```
  (x - min) / (max - min)
  ```
- How to handle invalid user inputs using `try-except`

---

## 📸 Sample Output

```
============================================================
📊 NumPy Data Analyzer
============================================================
How many numbers do you want to enter?: 5
Enter value 1: 10
Enter value 2: 40
Enter value 3: 25
Enter value 4: 90
Enter value 5: 60
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Data Analysis report📊
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Count              :- 5
Mean               :- 45.00
Median             :- 40.00
Standard deviation :- 27.38
Maximum value      :- 90
Minimum value      :- 10
Above Mean         :- [60 90]
Normalized Data    :- [0. 0. 0. 1. 1.]
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
```

---

## 🛠 Requirements
- Python 3.8+
- NumPy

Install NumPy using:

```
pip install numpy
```

---

## 📦 How to Run

```
python analyzer.py
```

(Replace `analyzer.py` with your filename.)

---

## 📁 Code (Main Script)

```python
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
print(f"Normalized Data    :- {np.round((array - array.min()) / (array.max() - array.min()))}")
print("~" * 60)
```

---

## 🧩 Future Improvements
- Add file input/output (save reports)
- Graph visualizations using matplotlib
- CSV data support
- Outlier detection
- z-score normalization
- GUI version (Tkinter)

---

## 🤝 Contributions
Pull requests are welcome!  
This is a beginner-friendly project — feel free to build on top of it.

---

## ⭐ Show Support
If you like this project, give it a ⭐ on GitHub!
```
