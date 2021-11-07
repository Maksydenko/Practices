int_1 = int(input("Write the first integer: "))
print("Special string with \"%\":", "%5d" % int_1,
      "\nThe string format() method:", "{0:5d}".format(int_1),
      "\nf-string:", f"{int_1:5d}")
int_2 = int(input("Write the second integer: "))
print("Special string with '%':", "%5d" % int_2,
      "\nThe string format() method:", "{0:5d}".format(int_2),
      "\nf-string:", f"{int_2:5d}")

float_1 = float(input("Write the first real number: "))
print("Special string with \"%\":", "%8f" % float_1,
      "\nThe string format() method:", "{0:8f}".format(float_1),
      "\nf-string:", f"{float_1:8f}")
float_2 = float(input("Write the second real number: "))
print("Special string with \"%\":", "%8f" % float_2,
      "\nThe string format() method:", "{0:8f}".format(float_2),
      "\nf-string:", f"{float_2:8f}")
float_3 = float(input("Write the third real number: "))
print("Special string with \"%\":", "%7.4f" % float_3,
      "\nThe string format() method:", "{0:7.4f}".format(float_3),
      "\nf-string:", f"{float_3:7.4f}")
float_4 = float(input("Write the fourth real number:"))
print("Special string with \"%\":", "%7.4f" % float_4,
      "\nThe string format() method:", "{0:7.4f}".format(float_4),
      "\nf-string:", f"{float_4:7.4f}")

str_1 = input("Write the text: ")
print("Special string with \"%\":", "%0.2s" % str_1,
      "\nThe string format() method:", "{0:0.2s}".format(str_1),
      "\nf-string:", f"{str_1:0.2s}")

print("Special string with \"%\":", "%s" % (True),
      "\nThe string format() method:", "{}".format(True),
      "\nf-string:", f"{True}")