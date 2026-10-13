# 🔷 Pattern_DSA

A collection of **pattern-printing programs** written in a simple, beginner-friendly style. Pattern problems are one of the best ways to build strong **loop logic**, **index control**, and **problem-solving skills**, which are the foundation of Data Structures & Algorithms (DSA).

Every pattern in this repository comes with:

- the **expected output**
- the **logic / approach** in plain words
- **basic code** (nested loops only, no tricks)
- the **time complexity**

---

## 📑 Table of Contents

1. [About the Project](#-about-the-project)
2. [Why Patterns Matter for DSA](#-why-patterns-matter-for-dsa)
3. [Prerequisites](#-prerequisites)
4. [Project Structure](#-project-structure)
5. [How to Run](#-how-to-run)
6. [Patterns Included](#-patterns-included)
7. [How to Think About Any Pattern](#-how-to-think-about-any-pattern)
8. [Complexity Summary](#-complexity-summary)
9. [Practice Ideas](#-practice-ideas)
10. [Contributing](#-contributing)
11. [License](#-license)

---

## 📖 About the Project

**Pattern_DSA** contains programs that print different shapes using stars (`*`), numbers, and alphabets. The code is deliberately written in a **basic way**: plain `for` loops, simple variables, and clear names, so that anyone starting with DSA can read, understand, and modify it.

---

## 🎯 Why Patterns Matter for DSA

| Skill you build | Where it helps later |
|---|---|
| Nested loop control | Matrix problems, 2D arrays, dynamic programming tables |
| Index and boundary thinking | Arrays, strings, two pointers, sliding window |
| Counting rows, columns, spaces | Time complexity analysis |
| Breaking a big problem into small parts | Recursion, divide and conquer |
| Spotting a formula in a shape | Mathematical and logic-based questions |

---

## ✅ Prerequisites

- Python 3.x installed (check with `python --version`)
- Basic knowledge of:
  - `for` loops and `range()`
  - `print()` and the `end` parameter
  - Variables and simple arithmetic

---

## 📁 Project Structure

```
Pattern_DSA/
│
├── README.md
├── star_patterns/
│   ├── square.py
│   ├── right_triangle.py
│   ├── inverted_triangle.py
│   ├── pyramid.py
│   ├── diamond.py
│   ├── hollow_square.py
│   └── butterfly.py
├── number_patterns/
│   ├── number_triangle.py
│   ├── floyds_triangle.py
│   └── pascals_triangle.py
└── alphabet_patterns/
    └── alphabet_triangle.py
```

> You can organize files however you like. Just keep one pattern per file so they are easy to find.

---

## ▶️ How to Run

```bash
# 1. Clone the repository
git clone https://github.com/<your-username>/Pattern_DSA.git

# 2. Go inside the folder
cd Pattern_DSA

# 3. Run any pattern file
python star_patterns/pyramid.py
```

Each program asks for (or has a variable for) `n`, the number of rows. Change `n` and run again to see how the pattern grows.

---

## 🌟 Patterns Included

### 1. Square Pattern

**Output (n = 4)**
```
****
****
****
****
```

**Logic**
- Outer loop runs `n` times (rows).
- Inner loop runs `n` times (columns).
- Print one `*` per column, then move to the next line.

**Code**
```python
n = 4

for i in range(n):
    for j in range(n):
        print("*", end="")
    print()
```

**Time Complexity:** O(n²)

---

### 2. Right-Angled Triangle

**Output (n = 4)**
```
*
**
***
****
```

**Logic**
- Row `i` (starting from 1) prints exactly `i` stars.

**Code**
```python
n = 4

for i in range(1, n + 1):
    for j in range(i):
        print("*", end="")
    print()
```

**Time Complexity:** O(n²)

---

### 3. Inverted Right-Angled Triangle

**Output (n = 4)**
```
****
***
**
*
```

**Logic**
- Start from `n` and go down to 1.
- Row with value `i` prints `i` stars.

**Code**
```python
n = 4

for i in range(n, 0, -1):
    for j in range(i):
        print("*", end="")
    print()
```

**Time Complexity:** O(n²)

---

### 4. Pyramid Pattern

**Output (n = 4)**
```
   *
  ***
 *****
*******
```

**Logic**
- In row `i` (1 to n):
  - spaces = `n - i`
  - stars = `2 * i - 1`

**Code**
```python
n = 4

for i in range(1, n + 1):
    for s in range(n - i):
        print(" ", end="")
    for k in range(2 * i - 1):
        print("*", end="")
    print()
```

**Time Complexity:** O(n²)

---

### 5. Diamond Pattern

**Output (n = 4)**
```
   *
  ***
 *****
*******
 *****
  ***
   *
```

**Logic**
- Upper half is the pyramid from the previous pattern.
- Lower half is the same pyramid upside down, starting from `n - 1` so the middle row is not repeated.

**Code**
```python
n = 4

# upper half
for i in range(1, n + 1):
    for s in range(n - i):
        print(" ", end="")
    for k in range(2 * i - 1):
        print("*", end="")
    print()

# lower half
for i in range(n - 1, 0, -1):
    for s in range(n - i):
        print(" ", end="")
    for k in range(2 * i - 1):
        print("*", end="")
    print()
```

**Time Complexity:** O(n²)

---

### 6. Hollow Square

**Output (n = 5)**
```
*****
*   *
*   *
*   *
*****
```

**Logic**
- Print `*` only on the border: first row, last row, first column, last column.
- Otherwise print a space.

**Code**
```python
n = 5

for i in range(n):
    for j in range(n):
        if i == 0 or i == n - 1 or j == 0 or j == n - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()
```

**Time Complexity:** O(n²)

---

### 7. Butterfly Pattern

**Output (n = 3)**
```
*    *
**  **
******
**  **
*    *
```

**Logic**
- Each row has: left stars, middle spaces, right stars.
- Upper half: stars = `i`, spaces = `2 * (n - i)`.
- Lower half repeats the same rule while `i` goes back down.

**Code**
```python
n = 3

# upper half
for i in range(1, n + 1):
    for j in range(i):
        print("*", end="")
    for j in range(2 * (n - i)):
        print(" ", end="")
    for j in range(i):
        print("*", end="")
    print()

# lower half
for i in range(n - 1, 0, -1):
    for j in range(i):
        print("*", end="")
    for j in range(2 * (n - i)):
        print(" ", end="")
    for j in range(i):
        print("*", end="")
    print()
```

**Time Complexity:** O(n²)

---

### 8. Number Triangle

**Output (n = 4)**
```
1
1 2
1 2 3
1 2 3 4
```

**Logic**
- Row `i` prints numbers from 1 to `i`.
- The column number `j` is the value to print.

**Code**
```python
n = 4

for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
```

**Time Complexity:** O(n²)

---

### 9. Floyd's Triangle

**Output (n = 4)**
```
1
2 3
4 5 6
7 8 9 10
```

**Logic**
- Keep one counter that never resets.
- Print the counter, then increase it by 1.

**Code**
```python
n = 4
num = 1

for i in range(1, n + 1):
    for j in range(i):
        print(num, end=" ")
        num = num + 1
    print()
```

**Time Complexity:** O(n²)

---

### 10. Alphabet Triangle

**Output (n = 4)**
```
A
A B
A B C
A B C D
```

**Logic**
- The letter `A` has ASCII value 65.
- For column `j` (starting at 1), the letter is `chr(64 + j)`.

**Code**
```python
n = 4

for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(chr(64 + j), end=" ")
    print()
```

**Time Complexity:** O(n²)

---

### 11. Pascal's Triangle

**Output (n = 5)**
```
    1
   1 1
  1 2 1
 1 3 3 1
1 4 6 4 1
```

**Logic**
- Each value is a binomial coefficient.
- Start every row with `1`, then compute the next value using
  `value = value * (i - j) // (j + 1)`.
- Print spaces first to center the triangle.

**Code**
```python
n = 5

for i in range(n):
    for s in range(n - i - 1):
        print(" ", end="")

    value = 1
    for j in range(i + 1):
        print(value, end=" ")
        value = value * (i - j) // (j + 1)
    print()
```

**Time Complexity:** O(n²)

---

## 🧠 How to Think About Any Pattern

Use this 4-step method for every new pattern:

1. **Count the rows.** This is your outer loop.
2. **For each row, count what is printed.** Spaces, stars, numbers, or letters.
3. **Find the relation with the row number `i`.** Example: stars = `i` or `2 * i - 1`, spaces = `n - i`.
4. **Write one inner loop per thing printed**, then add `print()` at the end of the row.

**Quick tips**

- `print("*", end="")` keeps printing on the same line.
- An empty `print()` moves to the next line.
- If the shape grows then shrinks, use two separate loops (top half and bottom half).
- Dry run with a small `n` (like 3 or 4) before coding.

---

## ⏱️ Complexity Summary

| Pattern | Time | Space |
|---|---|---|
| Square | O(n²) | O(1) |
| Right Triangle | O(n²) | O(1) |
| Inverted Triangle | O(n²) | O(1) |
| Pyramid | O(n²) | O(1) |
| Diamond | O(n²) | O(1) |
| Hollow Square | O(n²) | O(1) |
| Butterfly | O(n²) | O(1) |
| Number Triangle | O(n²) | O(1) |
| Floyd's Triangle | O(n²) | O(1) |
| Alphabet Triangle | O(n²) | O(1) |
| Pascal's Triangle | O(n²) | O(1) |

All patterns print directly, so no extra memory grows with `n`.

---

## 🏋️ Practice Ideas

Try these yourself after understanding the ones above:

- Hollow pyramid
- Hollow diamond
- Right-aligned triangle
- Number pyramid (1, 121, 12321)
- Zig-zag number pattern
- Hourglass pattern
- Palindromic triangle
- X-shaped pattern
- Spiral number matrix

---

## 🤝 Contributing

Contributions are welcome!

1. Fork this repository
2. Create a new branch: `git checkout -b add-new-pattern`
3. Add your pattern file with output, logic, and basic code
4. Commit: `git commit -m "Add <pattern name>"`
5. Push and open a Pull Request

**Guidelines**

- Keep the code simple and beginner-friendly.
- Add comments and a sample output.
- One pattern per file.

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

## ⭐ Support

If this repository helped you, please give it a **star** and share it with others learning DSA. Happy coding! 🚀
