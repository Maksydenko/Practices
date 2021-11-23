# **KROK University**

<img src="https://cabinet.krok.edu.ua:8443/img/logo.png">

### **Practice 1**

**📅 Date:** 17.09.2021

**📁 Project:** [link](practice_01.py)

<details>
<summary><b>📋 Specification:</b></summary>

1. Write a Python-script that displays the message “Hello world”.<br>
2. Rewrite the first script to display three any messages.<br>
3. Write a Python-script to reads values for the length and width of a rectangle and returns the area of the rectangle.<br>
4. Write a program that requests the user to enter two numbers and prints the sum, product, difference and quotient of the two numbers.<br>
5. Write a program that reads in the radius of a circle and prints the circle’s diameter, circumference and area. Use the constant value 3.14159 for π. Do these calculations in output statements.
</details>

### **Practical work 1**

**📅 Date:** 04.04.2021

**📁 Project:** [link](practical_work_01.py)

<details>
<summary><b>📋 Specification:</b></summary>

1. Construct these numeric values:
   * Integer zero;
   * Floating point zero;
   * Integer one hundred and one;
   * Floating point one thousand;
   * Floating point one thousand using scientific notation;
   * Create a positive integer, a negative integer, and zero. Assign them to variables;
   * Write several arithmetic expressions. Bind the values to variables. Use a variety of operators, e.g. +, -, /, *, etc. Use parentheses to control operator scope;
   * Create several floats and assign them to variables;
   * Write several arithmetic expressions containing your float variables;
   * Write several expressions using mixed arithmetic (integers and floats);
   * Obtain a float as a result of division of one integer by another; do so by explicitly converting one integer to a float.

2. Type Conversation:
   * Construct an integer from the string "123";
   * Construct a float from the integer 123;
   * Construct an integer from the float 12.345.

3. Digits of a Number:
   * Write a Python-script that detects the last 4 digits of a credit card;
   * Find the sum of the digits of a three-digit number.
</details>

### **Laboratory work 3**

**📅 Date:** 11.10.2021

**📁 Project:** [link](laboratory_work_03.py)

<details>
<summary><b>📋 Specification:</b></summary>

Organize data input and format output of specified data types according to the option number. In the table. for each option there are requirements for the amount, type and format of data. Organize the output of each object using the % operator, the method str.format() and "f" lines.

<table border="1" cellspacing="0" cellpadding="0" width="604">
    <tr>
        <td width="151" colspan="2" valign="top">
            <p align="center"><b>Integers</b></p>
        </td>
        <td width="171" colspan="4" valign="top">
            <p align="center"><b>Real numbers</b></p>
        </td>
        <td width="94" rowspan="3" valign="top">
            <p align="center"><b>The number of characters in a line</b></p>
        </td>
        <td width="122" rowspan="3" valign="top">
            <p align="center"><b>The value of a logical object</b></p>
        </td>
    </tr>
    <tr>
        <td width="63" rowspan="2" valign="top">
            <p align="center"><b>Number of number</b>s</p>
        </td>
        <td width="87" rowspan="2" valign="top">
            <p align="center"><b>The width of the number field</b></p>
        </td>
        <td width="66" rowspan="2" valign="top">
            <p align="center"><b>Number of numbers</b></p>
        </td>
        <td width="38" rowspan="2" valign="top">
            <p align="center"><b>Real floating point number (specified output field width</b>)</p>
        </td>
        <td width="67" colspan="2" valign="top">
            <p align="center"><b>A real number with a fixed point</b></p>
        </td>
    </tr>
    <tr>
        <td width="28">
            <p align="center"><b>Output field width</p>
        </td>
        <td width="38">
            <p align="center"><b>Number of positions after the point</p>
        </td>
    </tr>
    <tr>
        <td width="63" valign="top">
            <p align="center">2</p>
        </td>
        <td width="87" valign="top">
            <p align="center">5</p>
        </td>
        <td width="66" valign="top">
            <p align="center">4</p>
        </td>
        <td width="38" valign="top">
            <p align="center">8</p>
        </td>
        <td width="28">
            <p align="center">7</p>
        </td>
        <td width="38">
            <p align="center">4</p>
        </td>
        <td width="94" valign="top">
            <p align="center">2</p>
        </td>
        <td width="122" valign="top">
            <p align="center">True</p>
        </td>
    </tr>
</table>

Addition. Example of format output:

```python
x = float(input("x = "))
```
<pre>x = 10.01</pre>

```python
print("Special string with \"%\":", "%5.3f" % x)
```
<pre>Special string with "%": 10.010</pre>

```python
print("String format() method:", "{0:5.3f}".format(x))
```
<pre>String format() method: 10.010</pre>

```python
print("f-string:", f"{x:5.3f}")
```
<pre>f-string: 10.010</pre>
</details>

### **Practical work 2**

**📅 Date:** 25.10.2021

**📁 Project:** [link](practical_work_02.py)

<details>
<summary><b>📋 Specification:</b></summary>

1. 
   * Assume that we define x, y, and z to refer to int values. Write an expression that computes whether...
      * ...x is odd;
      * ...x is a multiple of 20 (e.g., 20, 40, 60, ...).

    * Assume that zero is a positive number. Write an expression that computes whether...
      * ...x and y are both positive;
      * ...x and y have the same sign (both are positive or both are negative);
      * ...x and y have different signs (one is positive and one is negative).

   * Write an expression that computes whether...
     * ...all three names (x, y, and z) are bound to equal values;
     * ...all three names (x, y, and z) are bound to different values (none the same);
     * ...two variables store the same value, but the third one is different.

2. 
   * Assume that we specify two points in space by definint the x and y coordinate of each using x1, y1, x2, and y2 all which are float. Write an expression that computes...
     * ...the distance between these points;
     * ...the slope of the line from the first point to the second;
     * ...whether both points lie on the same line from the origin;
     * ...whether the first point is above the second;
     * ...what quadrant the first point lies in (1st, 2nd, 3rd, or 4th);
     * ...whether the two points lie in the same quadrant.
</details>

### **Practice 3**

**📅 Date:** 08.11.2021

**📁 Project:** [link](practice_03.py)

<details>
<summary><b>📋 Specification:</b></summary>

1. Write a Python program using loop structure to print numbers 1.2.3……9.
2. Write a Python program using loop structure to print numbers 9.8.7…..1.
3. Write a Python program to print on the screen odd numbers between 5..13.
4. Write a Python program to add all the numbers entered by a user until user enters 0.
5. Write a Python Program to reverse a number. For example, if user enters 123 as input then 321 is printed as output.
6. Write Python program to find and print factorial of a number.
</details>

### **Lab 4**

**📅 Date:** 08.11.2021

**📁 Project:** [link](lab_04.py)

<details>
<summary><b>📋 Specification:</b></summary>

1. Write a program that changes the values ​​of two integer variables a and b without use of additional variables.

2. Write a program that calculates and displays:
    * arithmetic mean of two integers a and b;
    * geometric mean of two integers a and b.

3. Write a program that rearranges the digits of the three-digit number that is specified user in reverse order and displays a new number on the screen.

4. Write a program that determines the total number of hours of the day (variable hour) and the total number of minutes of the day (variable minute) that have passed before the current seconds of the day (variable second). For example, if second = 11111 (second = 3 * 3600 + 5 * 60 + 11), then hour = 3 and minute = 5.

5. Write a program that determines the value of the angle in degrees (variable corner) between clockwise at the beginning of the day and its state in hour hours, minutes minutes and second seconds (0 ≤ hour ≤ 11; 0 ≤ minute; second ≤ 59).

6. Write a program that determines whether a natural number entered by the user: 
    * even;
    * ending in the number 5.

7. Write a program that determines the value of an integer variable number - from 1 to 7, c depending on which day of the week (Monday to Sunday) is the day (whole variable day) of a low year, in which January 1 is Monday (1 ≤ day ≤ 365).

8. Given fractional numbers a, b, c (a! = 0). Find out if the equation ax² + bx + c has fractional roots.
</details>

### **Practice 4**

**📅 Date:** 15.11.2021

**📁 Project:** [link](practice_04.py)

<details>
<summary><b>📋 Specification:</b></summary>

1. Write a program that reads 4 numbers from the keyboard and displays most of them.

2. Determine the number of days in the year that the user enters. In a leap year - 366 days, while in a normal 365.

3. A triangle exists only when the sum of any two of its sides is greater than a third. Given: a, b, c are the sides of the assumed triangle. Write a program that will indicate whether such a triangle exists or not.

4. Display all numbers in the range of 1 to 100 multiples of 7.

5. Calculate using a cycle the factorial of the number n

6. Display an "hourglass" whose maximum width is read from the keyboard (odd number). In the example, the width is 5:
<pre>
*****
 ***
  *
 ***
*****
</pre>

7. Use cycles to display all prime numbers from 1 to 100.
</details>

### **Practice 5**

**📅 Date:** 22.11.2021

**📁 Project:** [link](practice_05.py)

<details>
<summary><b>📋 Specification:</b></summary>

1. Write a Python program to generate and print a list, where the values are square of numbers between 1 and 30 (both included).
2. Write a Python program to display the examination schedule (extract the date from exam_st_date).

<pre>exam_st_date = (11, 12, 2014)

Sample Output:
The examination will start from: 11/12/2014</pre>

3. Write a Python program which accepts a sequence of commaseparated numbers from user and generate a list and a tuple with those numbers.

<pre>Sample data: 3, 5, 7, 23

Output:
List: ["3", "5", "7", "23"]
Tuple: ("3", "5", "7", "23")</pre>

4. Write a Python function that takes two lists and returns True if they have at least one common member.
5. Write a Python-script. There is a bus moving in the city, and it takes and drop some people in each bus stop. You are provided with a list (or array) of integer arrays (or tuples). Each integer array has two items which represent number of people get into bus (The first item) and number of people get off the bus (The second item) in a bus stop. Your task is to return number of people who are still in the bus after the last bus station (after the last array). Even though it is the last bus stop, the bus is not empty and some people are still in the bus, and they are probably sleeping there :D

Example:

<pre>
number([[10, 0], [3, 5], [5, 8]]) # Result is 5
number([[3, 0], [9, 1], [4, 10], [12, 2], [6, 1], [7, 10]]) # Result is 17
number([[3, 0], [9, 1], [4, 8], [12, 2], [6, 1], [7, 8]]) # Result is 21
</pre>
</details>

### **Practice 6**

**📅 Date:** 22.11.2021

**📁 Project:** [link](practice_06.py)

<details>
<summary><b>📋 Specification:</b></summary>

1. Write a Python program to calculate the length of a string.
2. Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string. If the string length is less than 2, return instead the empty string.
<pre>Sample Strings:

"w3resource"
Expected Result: "w3ce"

"w3"
Expected Result: "w3w3"

"w"
Expected Result: Empty String</pre>

3. Write a Python program to get a string from a given string where all occurrences of its first char have been changed to "$", except the first char itself.

<pre>Sample String : "restart"
Expected Result : "resta\$t"</pre>

4. Write a Python function to reverses a string if it's length is a multiple of 4.
5. Write a Python program that accepts a comma separated sequence of words as input and prints the unique words in sorted form (alphanumerically).
<pre>Sample Words: red, white, black, red, green, black
Expected Result: black, green, red, white, red</pre>
</details>