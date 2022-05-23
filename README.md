# **Algorithmization and programming**

<img src="images/python.gif&ct=s" height="150" alt="Python">

### **Short annotation to the course:**

The aim of the course is to form the student's knowledge of the whole process of developing a computer program using Python programming language in an integrated PyCharm development environment.<br>The course considers the principles of imperative programming and basic techniques that allow you to create simple and sophisticated solutions of typical mathematical and informational tasks; the basics of the Python programming language and the possibilities of a modern integrated PyCharm development environment are studied; construction of basic algorithms of data processing is carried out; knowledge, skills and abilities of effective use of programming tools in the future professional activity are formed, and also bases of information culture and style of programming are laid.

---

### **Practice 0**

**📅 Date:** 17.09.2021

**📁 Project:** [link](practice_00/main.py)

<details>
<summary><b>📋 Specification:</b></summary>

1. Write a Python-script that displays the message “Hello world”.
2. Rewrite the first script to display three any messages.
3. Write a Python-script to reads values for the length and width of a rectangle and returns the area of the rectangle.
4. Write a program that requests the user to enter two numbers and prints the sum, product, difference and quotient of the two numbers.
5. Write a program that reads in the radius of a circle and prints the circle’s diameter, circumference and area. Use the constant value 3.14159 for π. Do these calculations in output statements.
</details>

---

## **Python data model**

### **Practice 1**

**📅 Date:** 04.10.2021

**📁 Project:** [link](practice_01/main.py)

<details>
<summary><b>📋 Specification:</b></summary>

1. Construct these numeric values:

   * integer zero;
   * floating point zero;
   * integer one hundred and one;
   * floating point one thousand;
   * floating point one thousand using scientific notation;
   * create a positive integer, a negative integer, and zero. Assign them to variables;
   * write several arithmetic expressions. Bind the values to variables. Use a variety of operators, e.g. +, -, /, *, etc. Use parentheses to control operator scope;
   * create several floats and assign them to variables;
   * write several arithmetic expressions containing your float variables;
   * write several expressions using mixed arithmetic (integers and floats);
   * obtain a float as a result of division of one integer by another; do so by explicitly converting one integer to a float.

2. Type Conversation:

   * construct an integer from the string "123";
   * construct a float from the integer 123;
   * construct an integer from the float 12.345.

3. Digits of a Number:

   * write a Python-script that detects the last 4 digits of a credit card;
   * find the sum of the digits of a three-digit number.
</details>

### **Lab 3**

**📅 Date:** 11.10.2021

**📁 Project:** [link](lab_03/main.py)

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

    x = 10.01

```python
print("Special string with \"%\":", "%5.3f" % x)
```

    Special string with "%": 10.010

```python
print("String format() method:", "{0:5.3f}".format(x))
```

    String format() method: 10.010

```python
print("f-string:", f"{x:5.3f}")
```

    f-string: 10.010
</details>

---

## **Expressions in Python**

### **Practice 2**

**📅 Date:** 25.10.2021

**📁 Project:** [link](practice_02/main.py)

<details>
<summary><b>📋 Specification:</b></summary>

1. Assume that we define x, y, and z to refer to int values. Write an expression that computes whether:

      * x is odd;
      * x is a multiple of 20 (e.g., 20, 40, 60, ...).

    Assume that zero is a positive number. Write an expression that computes whether:

      * x and y are both positive;
      * x and y have the same sign (both are positive or both are negative);
      * x and y have different signs (one is positive and one is negative).

    Write an expression that computes whether:

     * all three names (x, y, and z) are bound to equal values;
     * all three names (x, y, and z) are bound to different values (none the same);
     * two variables store the same value, but the third one is different.

2. Assume that we specify two points in space by definint the x and y coordinate of each using x1, y1, x2, and y2 all which are float. Write an expression that computes:

     * the distance between these points;
     * the slope of the line from the first point to the second;
     * whether both points lie on the same line from the origin;
     * whether the first point is above the second;
     * what quadrant the first point lies in (1st, 2nd, 3rd, or 4th);
     * whether the two points lie in the same quadrant.
</details>

---

## **Instructions in Python**

### **Lab 4**

**📅 Date:** 08.11.2021

**📁 Project:** [link](lab_04/main.py)

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

8. Given fractional numbers a, b, c (a != 0). Find out if the equation ax² + bx + c has fractional roots.
</details>

---

## **Execution Flow Management in Python - I**

### **Practice 3**

**📅 Date:** 08.11.2021

**📁 Project:** [link](practice_03/main.py)

<details>
<summary><b>📋 Specification:</b></summary>

1. Write a Python program using loop structure to print numbers 1, 2, 3, ..., 9.
2. Write a Python program using loop structure to print numbers 9, 8, 7, ..., 1.
3. Write a Python program to print on the screen odd numbers between 5 ... 13.
4. Write a Python program to add all the numbers entered by a user until user enters 0.
5. Write a Python Program to reverse a number. For example, if user enters 123 as input then 321 is printed as output.
6. Write Python program to find and print factorial of a number.
</details>

---

## **Execution Flow Management in Python - II**

### **Practice 4**

**📅 Date:** 15.11.2021

**📁 Project:** [link](practice_04/main.py)

<details>
<summary><b>📋 Specification:</b></summary>

1. Write a program that reads 4 numbers from the keyboard and displays most of them.

2. Determine the number of days in the year that the user enters. In a leap year - 366 days, while in a normal 365.

3. A triangle exists only when the sum of any two of its sides is greater than a third. Given: a, b, c are the sides of the assumed triangle. Write a program that will indicate whether such a triangle exists or not.

4. Display all numbers in the range of 1 to 100 multiples of 7.

5. Calculate using a cycle the factorial of the number n

6. Display an "hourglass" whose maximum width is read from the keyboard (odd number). In the example, the width is 5:

        *****
         ***
          *
         ***
        *****

7. Use cycles to display all prime numbers from 1 to 100.
</details>

---

## **Basic sequences in Python - list, tuple, range**

### **Practice 5**

**📅 Date:** 22.11.2021

**📁 Project:** [link](practice_05/main.py)

<details>
<summary><b>📋 Specification:</b></summary>

1. Write a Python program to generate and print a list, where the values are square of numbers between 1 and 30 (both included).

2. Write a Python program to display the examination schedule (extract the date from exam_st_date).

        exam_st_date = (11, 12, 2014)

        Sample Output:
        The examination will start from: 11/12/2014

3. Write a Python program which accepts a sequence of commaseparated numbers from user and generate a list and a tuple with those numbers.

        Sample data: 3, 5, 7, 23

        Output:
        List: ["3", "5", "7", "23"]
        Tuple: ("3", "5", "7", "23")

4. Write a Python function that takes two lists and returns True if they have at least one common member.

5. Write a Python-script. There is a bus moving in the city, and it takes and drop some people in each bus stop. You are provided with a list (or array) of integer arrays (or tuples). Each integer array has two items which represent number of people get into bus (The first item) and number of people get off the bus (The second item) in a bus stop. Your task is to return number of people who are still in the bus after the last bus station (after the last array). Even though it is the last bus stop, the bus is not empty and some people are still in the bus, and they are probably sleeping there :D
    
    Example:

        number([[10, 0], [3, 5], [5, 8]]) # Result is 5
        number([[3, 0], [9, 1], [4, 10], [12, 2], [6, 1], [7, 10]]) # Result is 17
        number([[3, 0], [9, 1], [4, 8], [12, 2], [6, 1], [7, 8]]) # Result is 21
</details>

---

## **Strings in Python - I**

### **Practice 6**

**📅 Date:** 22.11.2021

**📁 Project:** [link](practice_06/main.py)

<details>
<summary><b>📋 Specification:</b></summary>

1. Write a Python program to calculate the length of a string.

2. Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string. If the string length is less than 2, return instead the empty string.

        Sample Strings:

        "w3resource"
        Expected Result: "w3ce"

        "w3"
        Expected Result: "w3w3"

        "w"
        Expected Result: Empty String

3. Write a Python program to get a string from a given string where all occurrences of its first char have been changed to "$", except the first char itself.

        Sample String : "restart"
        Expected Result : "resta$t"

4. Write a Python function to reverses a string if it's length is a multiple of 4.

5. Write a Python program that accepts a comma separated sequence of words as input and prints the unique words in sorted form (alphanumerically).

        Sample Words: red, white, black, red, green, black
        Expected Result: black, green, red, white, red
</details>

---

## **Strings in Python - II**

### **Practice 7**

**📅 Date:** 28.11.2021

**📁 Project:** [link](practice_07/main.py)

<details>
<summary><b>📋 Specification:</b></summary>

1. Implement a script which receives a string and replaces all " symbols with ' and vise versa. The script should return modified string.

2. Write a script that checks whether a string is a palindrome or not.
    
    Returns "True" if it is palindrome, else "False".

    To check your implementation you can use strings from [here](https://en.wikipedia.org/wiki/Palindrome#Famous_palindromes).

    The script has to ignore special characters, whitespaces and different cases.

3. Implement a script which works the same as str.split.

    Note:
    
    Usage of str.split method is prohibited.

4. Implement a script which returns the longest word in the given string.

    The word can contain any symbols except whitespaces (`, \n, \t and so on).

    If there are multiple longest words in the string with a same length return the word that occurs first.

5. For a positive integer n calculate the result value, which is equal to the sum of the odd numbers of n.

    Example:

        n = 1234
        result = 4

        n = 246
        result = 0

6. Create a script that for a positive integer n calculates the result value, which is equal to the sum of the “1” in the binary representation of n otherwise, returns None.

    Example:

        n = 14 = 1110
        result = 3

        n = 128 = 10000000
        result = 1

7. Once upon a time, on a way through the old wild mountainous west, a man was given directions to go from one point to another. The directions were "NORTH", "SOUTH", "WEST", "EAST". Clearly "NORTH" and "SOUTH" are opposite, "WEST" and "EAST" too.

    Going to one direction and coming back the opposite direction right away is a needless effort. Since this is the wild west, with dreadfull weather and not much water, it's important to save yourself some energy, otherwise you might die of thirst!

    How I crossed a mountainous desert the smart way.

    The directions given to the man are, for example, the following (depending on the language):

        ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]

    or

        {"NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"}

    or

        [North, South, South, East, West, North, West]

    You can immediatly see that going "NORTH" and immediately "SOUTH" is not reasonable, better stay to the same place! So the task is to give to the man a simplified version of the plan. A better plan in this case is simply:

        ["WEST"]

    or

        {"WEST"}

    or

        [West]

    Other examples:

    * in ["NORTH", "SOUTH", "EAST", "WEST"], the direction "NORTH" + "SOUTH" is going north and coming back right away;

    * the path becomes ["EAST", "WEST"], now "EAST" and "WEST" annihilate each other, therefore, the final result is [] (nil in Clojure);

    * in ["NORTH", "EAST", "WEST", "SOUTH", "WEST", "WEST"], "NORTH" and "SOUTH" are not directly opposite but they become directly opposite after the reduction of "EAST" and "WEST" so the whole path is reducible to ["WEST", "WEST"].

    Task:

    Write a script which will take an array of strings and returns an array of strings with the needless directions removed (W<->E or S<->N side by side).

8. Background:

    In Japan, a game called Shiritori is played. The rules are simple, a group of people take turns calling out a word whose beginning syllable is the same as the previous player's ending syllable. For example, the first person would say the word ねこ, and the second player must make a word that starts with こ, like　こむぎ. This repeats until a player can not think of a word fast enough or makes a word that ends in ん, because there are no words that begin with ん　in the Japanese language.

    English Shiritori has the same principle, with the first and last letters of words. That being said the lose condition is saying a word that doesn't start with the previous word's last letter or not saying a word quick enough.

    For example:
    
    apple -> eggs -> salmon -> nut -> turkey ...

    Your Task:

    You will be given a list of strings, a transcript of an English Shiritori match. Your task is to find out if the game ended early, and return a list that contains every valid string until the mistake. If a list is empty return an empty list. If one of the elements is an empty string, that is invalid and should be handled.

    Examples:

        All elements valid:
        The array {"dog", "goose", "elephant", "tiger", "rhino", "orc", "cat"}
        Should return {"dog", "goose", "elephant", "tiger", "rhino", "orc", "cat"}

        An invalid element at index 2:
        The array {"dog", "goose", "tiger", "cat", "elephant", "rhino", "orc"}
        Should return ("dog", "goose") since goose ends in "e" and tiger starts with "t"

        An invalid empty string at index 2:
        The array {"ab", "bc", "", "cd"}
        Should return ("ab", "bc")

        All invalid empty string at index 0:
        The array {"", "bc", "", "cd"}
        Should return An Empty List
</details>

### **Lab 5**

**📅 Date:** 30.11.2021

**📁 Project:** [link](lab_05/main.py)

<details>
<summary><b>📋 Specification:</b></summary>

When performing tasks, use standard methods for working with strings. A sequence of numeric values is treated as a string. The reference to the index to the elements of the lines in the tasks of subparagraph b. is not used.

<ol type="a">
    <li>
        The Fibonacci sequence is formed as follows: the first and second members of the sequence are 1, each subsequent is equal to the sum of the previous two (1, 1, 2, 3, 5, 8, 13, ...). Given a natural number n (n >= 3):
        <ul>
            <li>find the k-th member of the Fibonacci sequence;</li>
            <li>get ​​the first n members of the Fibonacci sequence.</li>
        </ul>
    </li>
    <li>
        Program. This sequence contains from 2 to 20 words, each of which from 2 to 10 Latin letters; between adjacent words - at least one space, after the last word - a period. Display all words other than the last word, pre-arranging the words of the text in alphabetical order.
    </li>
    <li>
        Two words are given. Display those letters of words that are only in one of them (including those that are repeated). For example, if the given words are processor and information, then the answer should be: r o.
    </li>
</ol>
</details>

---

## **Sets in Python**

### **Lab 6**

**📅 Date:** 02.12.2021

**📁 Project:** [link](lab_06/main.py)

<details>
<summary><b>📋 Specification:</b></summary>

The tasks in point b) must be performed using the data types dict and list.

<ol type="a">
    <li>
        Given the symbols - s1, s2, ... It is known that the symbol s1 is different from the space and that among s2, s3, ... there is at least one space. We consider s1, ..., sn - the characters preceding the first space (n is not known in advance). From the sequence s1, ..., sn form a set in which to delete all characters that are not letters or numbers, and replace each uppercase letter with the same lowercase.
    </li>
    <li>
        The task. Determine the average grade point average in all subjects, and display information about students whose average score is more than 75b. Structure fields: Surname, Group, Physics, Algorithmization and programming, Higher Mathematics.
    </li>
</ol>
</details>

---

## **Exam (autumn semester)**

**📅 Date:** 06.12.2021

**📁 Project:** [link](exam_autumn/main.py)

<details>
<summary><b>📋 Specification:</b></summary>

1. Write a program in Python that calculates the value of the function y = (5x2-3x) / sin (x) for x values ranging from 1 to 30, in steps of 0.5.
2. Write a program in Python that outputs the number of odd numbers in a given list into a standard output stream.
3. Write a program in Python, which in a non-empty sequence of non-empty words from Latin letters determines the number of words that begin and end with the same letter. Display the result.
4. Write a program in Python that outputs all prime numbers from 1 to 1000 to the standard output stream.

    Note: A prime number is a number that is divisible without remainder only by one or by itself.
</details>

---

## **Multidimensional arrays in Python**

### **Practice 8**

**📅 Date:** 24.01.2022

**📁 Project:** [link](practice_08/main.py)

<details>
<summary><b>📋 Specification:</b></summary>

1. Enter five integer values ​​from the keyboard into the array. Print them in a single line through a comma. Get the arithmetic mean for the array.
2. Enter five integer elements of the array X from the keyboard. Display the values ​​of the roots and squares of each of the elements of the array.
3. Create an array of five last names and display them in a column, starting with the last.
4. Create an array of five last names and display those that start with a specific letter that is entered from the keyboard.
5. Create an array A[0 ... 7] using a random number generator and display it on the screen. Increase all its elements in 2 times.
</details>

### **Lab 7**

**📅 Date:** 14.02.2022

**📁 Project:** [link](lab_07/main.py)

<details>
<summary><b>📋 Specification:</b></summary>

1. Write a program to display the elements of a linear array on the screen (elements of the array are set in a short order) in reverse order.
2. Write a program to display a transposed 3x3 matrix on the screen.
3. Write a program that generates two square matrices 3x3 (it is necessary to check the size). Bring the results of multiple elements to a new matrix and display them on the screen.
4. Write a program that changes all input elements to 0 in a 4x4 matrix.
</details>

---

## **Data search**

### **Practice 9**

**📅 Date:** 07.02.2022

**📁 Project:** [link](practice_09/main.py)

<details>
<summary><b>📋 Specification:</b></summary>
Fill the 10x20 matrix with random numbers from 0 to 15. Display the matrix itself and the line numbers in which the number 5 occurs three or more times.
</details>

### **Lab 8**

**📅 Date:** 22.02.2022

**📁 Project:** [link](lab_08/main.py)

<details>
<summary><b>📋 Specification:</b></summary>

The task is to study and implement search algorithms for data prepared using the function of modeling random numbers and texts prepared independently.

For the skin algorithm, it is necessary to prepare tests that confirm the application of the program. For all the search algorithms, the listings of the search programs and the listings of the results are given (position numbers in the output array, depending on how the element is sorted or the fragment of the search; the number of ordering according to the skin algorithm of the search).

The simplest algorithms for a joke:

1. Line search.
2. Binary search.
3. Direct poshuk pіryadka.
</details>

---

## **Data sorting**

### **Practice 10**

**📅 Date:** 10.04.2022

**📁 Project:** [link](practice_10_01/main.py)

<details>
<summary><b>📋 Specification:</b></summary>

1. Given an array of integers. The number of items to invite from the keyboard. Find:

   * the maximum element of the array and its number;
   * the minimum element of the array.

2. Given an array of 10 elements. Sort the first 4 in ascending order, the last 4 in descending order.

3. Given an array of 20 integers on the segment [-2; 5]. Arrange the array by deleting the zeros with an offset to the left.
</details>

### **Lab 9**

**📅 Date:** 13.05.2022

**📁 Project:** [link](lab_09_01/main.py)

<details>
<summary><b>📋 Specification:</b></summary>

Implement a program in which each of the sorting algorithms is designed as a separate function. Illustrate the mechanism of using different types of parameters. Provide a calculation of the number of required comparisons, the number of exchanges and the operating time of each function, forming the functions of evaluating the effectiveness of sorting methods. Prepare a single test source for all algorithms:

* generated a sequence of pseudo-random numbers sufficient to estimate the speed of the sorting algorithm (about 100,000 integers);
* the original sequence of pseudo-random numbers, sorted by any method in ascending order;
* the original sequence of pseudo-random numbers, sorted by any method in descending order;
* provide software selection of input data from the keyboard up to 30 output numbers.

For the program, list the results of the work:

* output array (display on the screen for the case of input from the keyboard);
* sorted array (for the case of input from the keyboard, one instance of the sorted array to display);
* indicators of the function of evaluating the effectiveness of sorting methods (display).

Sort the array of integers A in ascending / descending order. The simplest sorting algorithms:

* bubble sort;
* selection sort;
* insertion sort.
</details>

---

## **Functions in Python**

### **Practice 10**

**📅 Date:** 21.02.2022

**📁 Project:** [link](practice_10/main.py)

<details>
<summary><b>📋 Specification:</b></summary>

1. Write the function addRightDigit (d, k), which should add to the positive integer k on the right the number d (d is an integer value in the range 0-9, k is an integer value).
2. Write a function that takes two integers n and k and returns a number containing k of the first digits of the number n.
</details>

### **Lab 9**

**📅 Date:** 09.05.2022

**📁 Project:** [link](lab_09/main.py)

<details>
<summary><b>📋 Specification:</b></summary>

1. Write a function that returns the maximum value from the list of numbers.
2. Implement a function whose parameters are two numbers and a string. It returns the concatenation of the string with the sum of the numbers.
3. Implement a function that displays a rectangle of asterisks "*". Its parameters will be integers that describe the length and width of such a rectangle.
4. Write a function that implements a linear search for an element in a list of integers. If such an item is in the list, return its index, if not, return the number "-1".
5. Write a function that returns the number of words in a line of text.
</details>

---

## **Recursion**

### **Practice 11**

**📅 Date:** 17.04.2022

**📁 Project:** [link](practice_11/main.py)

<details>
<summary><b>📋 Specification:</b></summary>

Realize Python's program in the list below. For each of the tasks, the algorithm is implemented using recursion and iteration. To argue the feasibility of choosing in each case of recursion or iteration (to use as criteria - the time of development and execution of programs, the amount of memory occupied, the readability of the program).

1. To form a function that will compute the factorial specified by the natural number user n.

2. To form a function to calculate the digital root of a natural number. The digital root is obtained as follows: It is necessary to compile all figures of a given number, then make up all figures of the amount found and repeat the process until the amount will be equal to the unambiguous number, which will be a digital root of a given number.

3. Form a function to calculate the index of the maximum array of n * n, where 1 <= n <= 5.
</details>

### **Lab 10**

**📅 Date:** 15.05.2022

**📁 Project:** [link](lab_10/main.py)

<details>
<summary><b>📋 Specification:</b></summary>

Implement the Python program tasks from the list below. For each of the tasks the algorithm is implemented using recursion and iteration. Argue in writing the appropriateness of the choice in each case of recursion or iteration (use as criteria - the time of development and execution of programs, the amount of memory occupied, the readability of the program).

1. Create a function for entering a sequence of numbers from the keyboard and display it in reverse order (the final character of the sequence - a dot)

2. Form a function that will determine whether a given natural number is prime. A prime number is one that is greater than 1 and has no divisors other than 1 and itself).

3. Form a function for converting a natural number from a decimal number system to a hexadecimal one.
</details>

---

## **Exam (spring semester)**

**📅 Date:** 16.05.2022

**📁 Project:** [link](exam_spring/main.py)

<details>
<summary><b>📋 Specification:</b></summary>

1. Polycarpus works as a DJ in the best Berland nightclub, and he often uses dubstep music in his performance. Recently, he has decided to take a couple of old songs and make dubstep remixes from them.

    Let's assume that a song consists of some number of words (that don't contain WUB). To make the dubstep remix of this song, Polycarpus inserts a certain number of words "WUB" before the first word of the song (the number may be zero), after the last word (the number may be zero), and between words (at least one between any pair of neighbouring words), and then the boy glues together all the words, including "WUB", in one string and plays the song at the club.

    For example, a song with words "I AM X" can transform into a dubstep remix as "WUBWUBIWUBAMWUBWUBX" and cannot transform into "WUBWUBIAMWUBX".
    
    Recently, Jonny has heard Polycarpus's new dubstep track, but since he isn't into modern music, he decided to find out what was the initial song that Polycarpus remixed. Help Jonny restore the original song.

    Input:
    
    The input consists of a single non-empty string, consisting only of uppercase English letters, the string's length doesn't exceed 200 characters

    Output: 
    
    Return the words of the initial song that Polycarpus used to make a dubsteb remix. Separate the words with a space.

    Examples:

        song_decoder("WUBWEWUBAREWUBWUBTHEWUBCHAMPIONSWUBMYWUBFRIENDWUB")
        WE ARE THE CHAMPIONS MY FRIEND


2. Numbers in the Morse code have the following pattern:

* all digits consist of 5 characters;
* the number of dots at the beginning indicates the numbers from 1 to 5, the remaining characters are dashes;
* starting with the number 6, each dot is replaced by a dash and vise versa.
Write the function morse_number() for encryption of a number in a three-digit format in Morse code.


3. Write a function using recursion to check if a number n is prime (you have to check whether n is divisible by any number below n).


4. Bob is preparing to pass IQ test. The most frequent task in this test is to find out which one of the given numbers differs from the others. Bob observed that one number usually differs from the others in evenness. Help Bob — to check his answers, he needs a program that among the given numbers finds one that is different in evenness, and return a position of this number.

    ! Keep in mind that your task is to help Bob solve a real IQ test, which means indexes of the elements start from 1 (not 0)

    Examples:

        iq_test("2 4 7 8 10")
        3 # Third number is odd, while the rest of the numbers are even

        iq_test("1 2 1 1")
        2 # Second number is even, while the rest of the numbers are odd


5. Your task is to sort a given string. Each word in the string will contain a single number. This number is the position the word should have in the result.

    Note: Numbers can be from 1 to 9. So 1 will be the first word (not 0).
If the input string is empty, return an empty string. The words in the input String will only contain valid consecutive numbers.

    Examples:

        "is2 Thi1s T4est 3a"  -->  "Thi1s is2 3a T4est"
        "4of Fo1r pe6ople g3ood th5e the2"  -->  "Fo1r the2 g3ood 4of th5e pe6ople"
</details>

---

## **Python files**

### **Practice 12**

**📅 Date:** 21.05.2022

**📁 Project:** [link](practice_12)

<details>
<summary><b>📋 Specification:</b></summary>

The text file contains entries for phone numbers. Each line contains information: phone number, name, address.

Write a program that sorts the entries in the file in ascending order of the phone number.
</details>

### **Lab 11**

**📅 Date:** 22.05.2022

**📁 Project:** [link](lab_11/)

<details>
<summary><b>📋 Specification:</b></summary>

Write programs under given conditions. Display the results of the programs. Output data for tasks is generated programmatically.

<ol type="a">
    <li>
        Given binary files f and g, the components of which are integers. Get in the file h new components formed by subtracting the two components of the files f and g, which are in the appropriate positions.
    </li>
    <li>
        Given a text file f, the elements of which are symbols. Write in the file g those components of the file f that are numbers, and in the file h - letters.
    </li>
</ol>
</details>