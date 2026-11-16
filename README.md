Week 3 Assignment on Conditions and Loops

grade_reporter.py: Loops through a list of student scores, assigns letter grades using conditional statements, tracks pass and fail counts, and calculates the rounded class average.
bug_hunt.py: Identifies and fixes syntax, loop control, and type concatenation bugs in a while-loop summation script.

The hardest bug to find in Part B was the silent logic bug in the `while` loop condition (`count < 5`), which caused the loop to terminate early and omit the final number (5) from the summation. I knew something was wrong when the program ran successfully without throwing a syntax or type error, but printed an incorrect final sum instead of the expected 15.
