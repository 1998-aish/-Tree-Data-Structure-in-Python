🌳 Tree Data Structure in Python — Practice & Exercises
This project implements and expands on the concept of a generic multi-child Tree data structure using Python. It includes both custom class development and applied exercises to reinforce core data structure skills — making it ideal for your portfolio, coding practice, or interview preparation.
📁 What’s in This Repository?
1. Base Tree Implementation
- A reusable `TreeNode` class representing nodes in a generic tree.
- Supports parent-child relationships, hierarchical levels, and recursive traversal.
- Includes a sample tree of world locations (continents → countries → states → cities).
2. Exercise 1: Management Hierarchy Tree
📄 `General_tree1.py`

This exercise extends the `TreeNode` class to include:
- Name and Designation in each node.
- A flexible `print_tree(view_mode)` method that prints the tree in different formats:
  - `view_mode = "name"` → Only names
  - `view_mode = "designation"` → Only designations
  - `view_mode = "both"` → Name and designation combined

**Skills Practiced**:
- Data encapsulation
- Method overloading
- Tree visualization with different views
3. Exercise 2: Location Tree with Depth Limiting
📄 `General_tree2.py`

Enhances the base tree to:
- Build a location-based tree (Global → Countries → States → Cities)
- Modify `print_tree(level)` to print only up to a specified depth in the tree.

**Skills Practiced**:
- Tree depth calculation
- Controlled traversal
- Real-world data modeling using trees
✅ Skills You'll Demonstrate
- Object-oriented programming
- Tree-based recursion
- Level-order and conditional tree traversal
- Customizable `print_tree()` functions
- Data modeling with real-world use cases
🚀 How to Run
```bash
python General_tree1.py
python General_tree2.py
```
📌 Why Add This to GitHub?
- Showcases hands-on understanding of tree structures.
- Demonstrates ability to extend and customize data models.
- Helps others learning data structures with clearly explained, real examples.
- Makes your GitHub more professional with clean, modular Python code.


