# Pathfinder-For-Python

**Pathfinder** is an algorithm that finds the shortest path using a graph.

# Library

You may need a **pygame** library to run this project.
You can use this in your **terminal** to install the **pygame**: 

` pip install pygame `

# Button

### Keybord
- `c` : clear all
- `space` : start
- ` left ` : change mode to the left
- ` right ` : change mode to the right

### Mouse

- `first left click` : mark as start point
- `seccon left click` : mark as end point
- `other left click` : mark as wall point

- `right click` : mark as empty

# BFS

You can call ` Bfs_alogorithm() ` from ` general_algorithm.py `, it had 8 parameters:

- **screen**
    - A **pygame screen object** used to disply the process.
- **grid**
    - A grid that made by ` create_grid() ` function in ` general_algorithm.py `.
- **start**
    - A **starting node** of the path.
- **end**
    - An **destination node** of the path.
- **rows**
    - **Totol rows** of the grid.
- **width**
    - The width of your screen
- **step_by_step**
    - If set to ` True `, the process is displayed **step by step**. If set to ` False `, the entrie process is displayed **all at once**. The **Default** is ` False `
- **delay**
    - Controls how long the screen update is delayed, measured in **milliseconds**. The **Default** is ` 1 `

# DFS

You can call ` Dfs_alogorithm() ` from ` general_algorithm.py `, it had 8 parameters:

- **screen**
    - A **pygame screen object** used to disply the process.
- **grid**
    - A grid that made by ` create_grid() ` function in ` general_algorithm.py `.
- **start**
    - A **starting node** of the path.
- **end**
    - An **destination node** of the path.
- **rows**
    - **Totol rows** of the grid.
- **width**
    - The width of your screen
- **step_by_step**
    - If set to ` True `, the process is displayed **step by step**. If set to ` False `, the entrie process is displayed **all at once**. The **Default** is ` False `
- **delay**
    - Controls how long the screen update is delayed, measured in **milliseconds**. The **Default** is ` 1 `