# Basic Statistics Calculator

## Project Description

The **Basic Statistics Calculator** is a Python program that allows users to perform fundamental statistical operations on a given dataset. The program provides an interactive menu-driven interface to calculate essential statistical measures such as **Mean, Median, Variance, Standard Deviation**, and **Sorting the dataset**. It is implemented using the **NumPy** library for efficient numerical computations.

## Features

- **Compute Mean** (Average value of the dataset)
- **Compute Median** (Middle value of the dataset)
- **Compute Variance** (Measure of dispersion)
- **Compute Standard Deviation** (Measure of data spread)
- **Sort the dataset** in ascending order
- **Perform all operations** at once
- **Exit option** to terminate the program

## Requirements

- Python 3.x
- NumPy library

## Installation

To use this program, ensure you have Python installed. You also need the **NumPy** library, which you can install using:

```bash
pip install numpy
```

## Usage

1. **Run the script** in a Python environment.
2. **Enter a list** of space-separated integers when prompted.
3. **Choose an operation** from the menu by entering the corresponding number.
4. **View the result** of the selected operation.
5. **To exit**, select option `7`.

## Example Execution

```bash
Enter space-separated integers (Ex: 1 2 3 4 5 6): 4 8 2 6 9 1

---Basic Statistics Calculator---

1. Mean
2. Median
3. Variance
4. Standard Deviation
5. Sort the Array
6. All the above operations
7. Exit

Enter the option to proceed: 1
The mean of the array is: 5.0
```

## Code Explanation

### `basic_stat_calculator(data)`
- Main function that processes user input and performs calculations.

### Helper Functions:
- **`mean()`**: Computes the mean using `np.mean()`.
- **`median()`**: Computes the median using `np.median()`.
- **`variance()`**: Computes variance using `np.var()`.
- **`standard_deviation()`**: Computes standard deviation using `np.std()`.
- **`sort()`**: Sorts the dataset using `np.sort()`.

### Loop-based Menu System:
- Continuously prompts the user for an option.
- Calls the respective function based on user selection.
- Exits when the user selects option `7`.
