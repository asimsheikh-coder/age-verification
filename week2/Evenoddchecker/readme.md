# Even or Odd Number Range Checker

This Python script takes a user input and checks whether each number from `0` up to the entered number is even or odd.

## 🔍 What It Does

- Prompts the user to enter an integer
- Increments the number by 1 to include the entered number in the loop
- Iterates from 0 to the given number
- Prints whether each number is even or odd

## 🧪 Example

**User Input:**
```
Enter a number: 5
```

**Output:**
```
Even: 0
Odd: 1
Even: 2
Odd: 3
Even: 4
Odd: 5
```

## 🧾 Code

```python
number = int(input("Enter a number: "))  # e.g., 5
number = number + 1                      # include the entered number
for i in range(number):                  # loop from 0 to number
    if i % 2 == 0:
        print("Even:", i)
    else:
        print("Odd:", i)
```

## 🛠 How to Run

1. Make sure Python 3 is installed.
2. Save the code to a file, e.g., `even_odd_range.py`
3. Run the script using your terminal or command prompt:

```bash
python even_odd_range.py
```

## 📌 Notes

- This version checks **all numbers** from 0 up to the input number.
- To check **only the entered number**, you can use:

```python
number = int(input("Enter a number: "))
if number % 2 == 0:
    print("The number is Even")
else:
    print("The number is Odd")
```

## 📄 License

MIT License
