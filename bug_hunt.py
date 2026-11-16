count = 1
total = 0

# BUG: Added missing colon (:) at the end of the while statement to fix the SyntaxError.
while count <= 5:
    total = total + count
    # BUG: Changed count increment condition from count < 5 (which caused an infinite loop because count started at 1 and never incremented past 4 correctly) to count <= 5, and fixed the loop condition check.
    count = count + 1

# BUG: Fixed TypeError by converting the integer variable 'total' to a string using str() before concatenating it with another string.
print("Sum of 1 to 5 is: " + str(total))