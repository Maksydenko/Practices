# **Practical and laboratory works from KROK University**

 <img src="https://cabinet.krok.edu.ua:8443/img/logo.png">

### [**Practice 1**](https://github.com/Maksydenko/Practices/blob/main/practice_01.py)

<details>
<summary><b><i>📜 Specifications</i></b></summary>

<b>Exercise 1.</b> Write a Python-script that displays the message “Hello world”.<br>
<b>Exercise 2.</b> Rewrite the first script to display three any messages.<br>
<b>Exercise 3.</b> Write a Python-script to reads values for the length and width of a rectangle and returns the area of the rectangle.<br>
<b>Exercise 4.</b> Write a program that requests the user to enter two numbers and prints the sum, product, difference and quotient of the two numbers.<br>
<b>Exercise 5.</b> Write a program that reads in the radius of a circle and prints the circle’s diameter, circumference and area. Use the constant value 3.14159 for π. Do these calculations in output statements.
</details>

### [**Practical work 1**](https://github.com/Maksydenko/Practices/blob/main/practical_work_01.py)

<details>
<summary><b><i>📜 Specifications</i></b></summary>

**Task 1. Construct these numeric values:**

* Integer zero
* Floating point zero
* Integer one hundred and one
* Floating point one thousand
* Floating point one thousand using scientific notation
* Create a positive integer, a negative integer, and zero. Assign them to variables
* Write several arithmetic expressions. Bind the values to variables. Use a variety of operators, e.g. +, -, /, *, etc. Use parentheses to control operator scope
* Create several floats and assign them to variables
* Write several arithmetic expressions containing your float variables
* Write several expressions using mixed arithmetic (integers and floats)
* Obtain a float as a result of division of one integer by another; do so by explicitly converting one integer to a float

**Task 2. Type Conversation:**

* Construct an integer from the string "123"
* Construct a float from the integer 123
* Construct an integer from the float 12.345

**Task 3. Digits of a Number:**

* Write a Python-script that detects the last 4 digits of a credit card
* Find the sum of the digits of a three-digit number
</details>

### [**Laboratory work 3**](https://github.com/Maksydenko/Practices/blob/main/laboratory_work_03.py)

<details>
<summary><b><i>📜 Specifications</i></b></summary>

Organize data input and format output of specified data types according to the option number. In the table. for each option there are requirements for the amount, type and format of data. Organize the output of each object using the % operator, the method str.format () and ‘f’ lines.

<table border="1" cellspacing="0" cellpadding="0" width="604">
    <tr>
        </td>
        <td width="151" colspan="2" valign="top">
        <p align="center">Integers</p>
        </td>
        <td width="171" colspan="4" valign="top">
        <p align="center">Real numbers</p>
        </td>
        <td width="94" rowspan="3" valign="top">
        <p align="center">The number of characters in a line</p>
        </td>
        <td width="122" rowspan="3" valign="top">
        <p align="center">The value of a logical object</p>
        </td>
    </tr>
    <tr>
        <td width="63" rowspan="2" valign="top">
        <p align="center">Number of numbers</p>
        </td>
        <td width="87" rowspan="2" valign="top">
        <p align="center">The width of the number field</p>
        </td>
        <td width="66" rowspan="2" valign="top">
        <p align="center">Number of numbers</span></p>
        </td>
        <td width="38" rowspan="2" valign="top">
        <p align="center">Real floating point number (specified output field width)</p>
        </td>
        <td width="67" colspan="2" valign="top">
        <p align="center">A real number with a fixed point</p>
        </td>
    </tr>
    <tr>
        <td width="28">
        <p align="center">Output field width</p>
        </td>
        <td width="38">
        <p align="center">Number of positions after the point</p>
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

**Addition. Example of format output**

\>>> x = float (input ("x ="))<br>
x = 10.01

\>>> print ("Special string with \"% \ ":", "% 5.3f"% x)<br>
Special string with "%": 10.010

\>>> print ("String format method ():", "{0: 5.3f}". format (x))<br>
String format method (): 10.010

\>>> print ("f-string:", f "{x: 5.3f}")<br>
f-string: 10.010
</details>

### [**Practical work 2**](https://github.com/Maksydenko/Practices/blob/main/practical_work_02.py)

<!-- <details>
<summary><b><i>📜 Specifications</i></b></summary> -->

**Task 1:**

Assume that we define x, y, and z to refer to int values. Write an expression that computes whether...

* ...x is odd
* ...x is a multiple of 20 (e.g., 20, 40, 60, ...)

Assume that zero is a positive number. Write an expression that computes whether...

* ...x and y are both positive
* ...x and y have the same sign (both are positive or both are negative)
* ...x and y have different signs (one is positive and one is negative)

Write an expression that computes whether...

* ...all three names (x, y, and z) are bound to equal values
* ...all three names (x, y, and z) are bound to different values (none the same)
* ...two variables store the same value, but the third one is different

**Task 2:**

Assume that we specify two points in space by definint the x and y coordinate of each using x1, y1, x2, and y2 all which are float. Write an expression that computes...

* ...the distance between these points
* ...the slope of the line from the first point to the second
* ...whether both points lie on the same line from the origin
* ...whether the first point is above the second
* ...what quadrant the first point lies in (1st, 2nd, 3rd, or 4th)
* ...whether the two points lie in the same quadrant
</details>