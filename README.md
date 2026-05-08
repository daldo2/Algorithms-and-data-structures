# Algorithms-and-data-structures
Python Algorithms and Data Structures
This repository contains implementations of essential Abstract Data Types (ADTs) and algorithmic solutions to classic computational problems.

Implementations
1. Stack (Static Array)
A fixed-capacity stack implementation using a Python list.

Capacity: 20 elements.

Complexity: O(1) for all core operations (push, pop, top, is_empty).

Design: Manual pointer management via top_index.

2. Expression Evaluator
A two-stage mathematical expression processor.

Algorithm: Shunting-Yard (Infix to Postfix conversion).

Precedence: Handles operator priority and parenthesis nesting.

Evaluation: Postfix evaluation using the custom Stack class.

3. Palindrome Checker
A hybrid approach using Linked Lists and Stacks to verify string symmetry.

Structure: Singly Linked List with Node objects.

Logic: Elements are pushed to a stack during list traversal; a secondary traversal compares list data against stack pops to verify order reversal.

Directory Structure
expression_evaluator.py: Logic for Shunting-Yard and RPN calculation.

palindrome_checker.py: Linked List and verification logic.

README.md: Project documentation.

Technical Skills Demonstrated
Data Structures: Stacks, Singly Linked Lists, Nodes.

Algorithms: Shunting-Yard, Postfix Evaluation, String Manipulation.

Paradigm: Object-Oriented Programming (OOP).

Execution
Run scripts via the command line:

Bash
python expression_evaluator.py
python palindrome_checker.py
