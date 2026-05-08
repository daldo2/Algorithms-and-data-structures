# Python Algorithms and Data Structures

Implementation of fundamental data structures and algorithmic solutions to classic computational problems using Python.

## Implementations

### Stack (Static Array)
A fixed-capacity stack implementation using a Python list to demonstrate low-level memory management concepts in a high-level language.
* **Capacity**: 20 elements.
* **Complexity**: $O(1)$ for all core operations (`push`, `pop`, `top`, `is_empty`).
* **Design**: Manual pointer management via `top_index`.



### Expression Evaluator
A two-stage mathematical expression processor.
* **Algorithm**: Shunting-Yard (Infix to Postfix conversion).
* **Precedence Logic**: Handles operator priority and parenthesis nesting.
* **Evaluation**: Reverse Polish Notation (RPN) evaluation using the custom Stack class.



### Palindrome Checker
A hybrid approach using Linked Lists and Stacks to verify string symmetry.
* **Structure**: Singly Linked List with `Node` objects.
* **Logic**: Elements are pushed to a stack during list traversal; a secondary traversal compares list data against stack pops to verify character order reversal.



---

## Technical Skills Demonstrated

* **Data Structures**: Stacks, Singly Linked Lists, Nodes.
* **Algorithms**: Shunting-Yard, Postfix Evaluation, String Manipulation.
* **Paradigm**: Object-Oriented Programming (OOP).

---

## Directory Structure

* `expression_evaluator.py`: Logic for Shunting-Yard and RPN calculation.
* `palindrome_checker.py`: Linked List and verification logic.
* `README.md`: Project documentation.

---

## Execution

Run scripts via the command line:

```bash
python expression_evaluator.py
python palindrome_checker.py
```
