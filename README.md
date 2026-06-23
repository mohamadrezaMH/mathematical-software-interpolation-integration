# Mathematical Software Project 3

This repository contains the implementation of **Project 3** for the **Mathematical Software** course.

## Project Overview

The project covers three major topics:

1. **Interpolation**

   * Lagrange Polynomial Interpolation
   * Cubic Spline Interpolation

2. **Data Analysis and Visualization**

   * Reading data directly from an Excel file
   * Bar Chart Visualization
   * Line Chart Visualization
   * Box Plot Visualization
   * Statistical Analysis

3. **Numerical Integration**

   * Trapezoidal Rule
   * Simpson's Rule
   * Gaussian Quadrature

---

## Part 1: Interpolation

Given the following data points:

| x | y |
| - | - |
| 1 | 1 |
| 2 | 3 |
| 3 | 5 |
| 4 | 8 |
| 5 | 5 |
| 6 | 2 |

The project computes:

* Exact Lagrange interpolation polynomial
* Piecewise cubic spline equations
* Comparison plot between interpolation methods

### Generated Figure

* ![Interpolation Plot](./Project%20Report/interpolation.png)

---

## Part 2: Algorithm Runtime Analysis

The project reads execution times of three algorithms from an Excel file and automatically generates visualizations.

### Generated Charts

* `bar_chart.png`
* `line_chart.png`
* `box_plot.png`

### Features

* No manual data entry
* Automatic Excel parsing
* Automatic chart updates after adding new records
* Mean execution time calculation for Algorithm 2

---

## Part 3: Numerical Integration

The following function is evaluated:

[
f(x)=e^{x^2}
]

on the interval:

[
[0,1]
]

### Methods Used

* Trapezoidal Rule
* Simpson's Rule
* Gaussian Quadrature

### Results

| Method              | Result             |
| ------------------- | ------------------ |
| Trapezoidal         | 1.462652199861532  |
| Simpson             | 1.4626517459097506 |
| Gaussian Quadrature | 1.4626516680186823 |

The obtained values are highly consistent, demonstrating the accuracy of the implemented numerical methods.

---

## Technologies

* Python 3
* NumPy
* Pandas
* Matplotlib
* SciPy
* SymPy

---

## Repository Structure

```text
.
├── Lagrange_Interpolation.py
├── read_excel.py
├── Trapezodial.py
├── update_excel.py
├── Project Report
├── project_data.xlsx
├── Figures
└── README.md
```

---

## Course

Mathematical Software

---

## Author

Mohammadreza Mohammdi
