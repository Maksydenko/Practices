# **KROK University. Practices and labs**

<img src="https://cabinet.krok.edu.ua:8443/img/logo.png">

### **Practice 0**

**📅 Date:** 17.09.2021

**📁 Project:** [link](practice_0/main.py)

<details>
<summary><b>📋 Specification:</b></summary>

1. Write a Python-script that displays the message “Hello world”.
2. Rewrite the first script to display three any messages.
3. Write a Python-script to reads values for the length and width of a rectangle and returns the area of the rectangle.
4. Write a program that requests the user to enter two numbers and prints the sum, product, difference and quotient of the two numbers.
5. Write a program that reads in the radius of a circle and prints the circle’s diameter, circumference and area. Use the constant value 3.14159 for π. Do these calculations in output statements.
</details>

---

### **Practice 1**

**📅 Date:** 04.04.2021

**📁 Project:** [link](practice_1/main.py)

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

---

### **Lab 3**

**📅 Date:** 11.10.2021

**📁 Project:** [link](lab_3/main.py)

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

### **Practice 2**

**📅 Date:** 25.10.2021

**📁 Project:** [link](practice_2/main.py)

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

### **Practice 3**

**📅 Date:** 08.11.2021

**📁 Project:** [link](practice_3/main.py)

<details>
<summary><b>📋 Specification:</b></summary>

1. Write a Python program using loop structure to print numbers 1.2.3……9.
2. Write a Python program using loop structure to print numbers 9.8.7…..1.
3. Write a Python program to print on the screen odd numbers between 5..13.
4. Write a Python program to add all the numbers entered by a user until user enters 0.
5. Write a Python Program to reverse a number. For example, if user enters 123 as input then 321 is printed as output.
6. Write Python program to find and print factorial of a number.
</details>

---

### **Lab 4**

**📅 Date:** 08.11.2021

**📁 Project:** [link](lab_4/main.py)

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

---

### **Practice 4**

**📅 Date:** 15.11.2021

**📁 Project:** [link](practice_4/main.py)

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

### **Practice 5**

**📅 Date:** 22.11.2021

**📁 Project:** [link](practice_5/main.py)

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

### **Practice 6**

**📅 Date:** 22.11.2021

**📁 Project:** [link](practice_6/main.py)

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

### **Practice 7**

**📅 Date:** 28.11.2021

**📁 Project:** [link](practice_7/main.py)

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

    The word can contain any symbols except whitespaces (`,\n,\tand so on).

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

---

### **Lab 5**

**📅 Date:** 30.11.2021

**📁 Project:** [link](lab_5/main.py)

<details>
<summary><b>📋 Specification:</b></summary>

When performing tasks, use standard methods for working with strings. A sequence of numeric values is treated as a string. The reference to the index to the elements of the lines in the tasks of subparagraph b. is not used.

<ol type="a">
    <li>
    The Fibonacci sequence is formed as follows: the first and second members of the sequence are 1, each subsequent is equal to the sum of the previous two (1, 1, 2, 3, 5, 8, 13, ...). Given a natural number n (n> = 3):
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

Addition. Glossary of laboratory work terms:

A sequence is a way of organizing data (called sequence elements) in which the sequence can be either empty, and then it does not contain any elements, or non-empty. In the latter case, the sequence contains the first element. Moreover, for each element except the last, there is exactly one subsequent element. Thus, for each element of the sequence, except the first, there is exactly one previous element. In Python, the sequence element separator is the "," character. The sequence, unlike the set, may contain repeating elements. Examples: 0, 1, 0, 1, 0 and 1, 1, 1, 0, 1, 1, 1 - two sequences of zeros and ones; "A", "B", "A", "B", "A" - a sequence of letters; 121, 362, 1, 0, 548 - a sequence of integers.

A subsequence of the sequence w is any sequence v for which there are sequences x, y such that w = xvy. The initial segment of the sequence w is any sequence v for which there is a sequence y such that w = vy.

For example, 1, 0, 1; 0, 1, 0; 0; 1 and 1, 0, 1, 0, 0, 1 - (different) subsequences of the sequence 1, 0, 1, 0, 0, 1, and 1, 0, 1; 1 and 1, 0, 1, 0, 0, 1 are the initial segments of this sequence. An empty sequence is a subsequence and the initial segment of any sequence of elements of the corresponding type.

A series is a sequence composed of matching elements. For example, 11111 is a series of units.

Vector - a non-empty sequence of elements numbered by integers, starting from 0. Permutation of length n - a vector composed of pairs of different elements, each of which is an integer from the segment 0..n-1. For example, 3241 is a permutation of length 4.

A matrix is ​​a vector whose elements are vectors.

Text - a non-empty sequence of words separated by the characters "space", "comma" and "dot".

A word is a non-empty sequence of letter-symbols.

A sentence is a sequence of words separated by a space, with a closing dot.

Subword - a non-empty subsequence of words.

Word address - a word derived from the original word by writing its letters in reverse order. For example, 'ABCD' is a reference to the word "DCBA". A word is said to be symmetrical if it coincides with its address.

The occurrence of the word (sequence) v in the word (sequence) w is any part of the word (sequence) w, which is a subword (subsequence) v of the word w. For example, the word 'KOLOKOL' contains two occurrences of the subword "KOL".

A sequence of Fibonacci numbers is a sequence of natural numbers, the first two elements of which are equal to 1, and each subsequent one is the sum of the previous two:

 1, 1, 2, 3, 5, 8, 13, 21.
</details>

---

### **Lab 6**

**📅 Date:** 02.12.2021

**📁 Project:** [link](lab_6/main.py)

<details>
<summary><b>📋 Specification:</b></summary>

The tasks in point b) must be performed using the data types dict and list.

<ol type="a">
    <li>
        Given the symbols - s1, s2, ... It is known that the symbol s1 is different from the space and that among s2, s3, ... there is at least one space. We consider s1, ... , sn - the characters preceding the first space (n is not known in advance). From the sequence s1, ... , sn form a set in which to delete all characters that are not letters or numbers, and replace each uppercase letter with the same lowercase.
    </li>
    <li>
        The task. Determine the average grade point average in all subjects, and display information about students whose average score is more than 75b. Structure fields: Surname, Group, Physics, Algorithmization and programming, Higher Mathematics.
    </li>
</ol>
</details>

---

### **Practice 8**

**📅 Date:** 24.01.2022

**📁 Project:** [link](practice_8/main.py)

<details>
<summary><b>📋 Specification:</b></summary>

1. Enter five integer values ​​from the keyboard into the array. Print them in a single line through a comma. Get the arithmetic mean for the array.
2. Enter five integer elements of the array X from the keyboard. Display the values ​​of the roots and squares of each of the elements of the array.
3. Create an array of five last names and display them in a column, starting with the last.
4. Create an array of five last names and display those that start with a specific letter that is entered from the keyboard.
5. Create an array A [0 ... 7] using a random number generator and display it on the screen. Increase all its elements in 2 times.
</details>

---

### **Practice 9**

**📅 Date:** 07.02.2022

**📁 Project:** [link](practice_9/main.py)

<details>
<summary><b>📋 Specification:</b></summary>
Fill the 10x20 matrix with random numbers from 0 to 15. Display the matrix itself and the line numbers in which the number 5 occurs three or more times.
</details>

---

### **Lab 7**

**📅 Date:** 14.02.2022

**📁 Project:** [link](lab_7/main.py)

<details>
<summary><b>📋 Specification:</b></summary>

1. Write a program to display the elements of a linear array on the screen (elements of the array are set in a short order) in reverse order.
2. Write a program to display a transposed 3x3 matrix on the screen.
3. Write a program that generates two square matrices 3x3 (it is necessary to check the size). Bring the results of multiple elements to a new matrix and display them on the screen.
4. Write a program that changes all input elements to 0 in a 4x4 matrix.
</details>

---

### **Practice 10**

**📅 Date:** 21.02.2022

**📁 Project:** [link](practice_10/main.py)

<details>
<summary><b>📋 Specification:</b></summary>

1. Write the function addRightDigit (d, k), which should add to the positive integer K on the right the number D (D is an integer value in the range 0-9, K is an integer value).
2. Write a function that takes two integers n and k and returns a number containing k of the first digits of the number n.
</details>