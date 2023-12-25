# Box Demand Optimization

This repository contains a Python script for optimizing box production to meet demand with minimal cost using integer programming. The optimization problem is formulated and solved using Google's Operations Research tools (OR-Tools).

## Problem Statement

A company sells seven types of boxes with varying sizes. The cost of producing each box is proportional to its size plus a fixed cost. The demand for a smaller box can be satisfied by a larger box. The goal is to minimize the total cost of meeting the demand for all box sizes.

## Dependencies

- Python 3.x
- Google OR-Tools

To install OR-Tools, run:
```bash
pip install ortools
```

To run the file, execute:
```bash
python bonus_question.py
```

For course: IME 312  Operations Research
Under Supervision of Prof. Islam Ali
