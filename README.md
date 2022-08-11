# Sorting Visualizer

## Function Descriptions

1. **[colors.py](colors.py)**

    In `colors.py` we will store some hexadecimal values of colors as variables. We will use these colors in our project.

2. **[main.py](main.py)**

    `main.py` will be our main executable file that will run our project. We will import all packages and modules in this file. First, we will import some stuff and set up a basic interface.

    * 2.1 **drawData()**
    <br>This function will convert the elements of `data[]` into vertical bars and draw them into the window.

    * 2.2 **generate()**
    <br>It will reate an array with random values with the help of random module. After creating the array we will store them in `data[]`. Then we will call the `drawData()` function from this function.

    * 2.3
    <br>Now the program will create a random array on the window every time we hit the **Generate Array** button.

    * 2.4 **set_speed()**
    <br>This function will determine how fast or slow we want to see the sorting comparisons.

    * 2.5 **sort()**

3. **[bubbleSort.py](algorithms/bubbleSort.py)**
<br>The bubble sort algorithm to sort an array.

4. **[mergeSort.py](algorithms/mergeSort.py)**
<br>The merger sort algorithm to sort an array.
