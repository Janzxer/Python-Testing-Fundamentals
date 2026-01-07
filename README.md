# Python Unit Testing & Modular Design

## Overview
This repository demonstrates software testing principles, specifically **Test-Driven Development (TDD)** and **Separation of Concerns**. The code is structured into three distinct layers:
1.  **Utils:** Pure business logic.
2.  **UI:** User interaction (Console).
3.  **Tests:** Automated test suites covering boundary values and edge cases.

## Modules

### 1. Calculator
* **Logic:** `CalculatorUtils.py` handles arithmetic operations.
* **Testing:** `MyCalculatorTest.py` validates operations and prevents crashes on division by zero.

### 2. Triangle Classifier
* **Logic:** `TriangleUtils.py` determines if a triangle is Equilateral, Isosceles, or Scalene.
* **Testing:** `TriangleTests.py` validates logic against invalid inputs (e.g., negative sides, inequality violations).

### 3. Age Validator
* **Logic:** `AgeUtils.py` processes user age input into categories.
* **Testing:** `MyAgeTest.py` performs **Boundary Value Analysis** (e.g., testing ages 17, 18, 19, 64, 65).

## How to Run Tests
You can execute the test suites directly from the command line:

```bash
# Run All Tests (Auto-discovery)
python -m unittest discover -p "*Test.py"

# Run Specific Suites
python -m unittest MyCalculatorTest.py
python -m unittest TriangleTests.py
python -m unittest MyAgeTest.py
