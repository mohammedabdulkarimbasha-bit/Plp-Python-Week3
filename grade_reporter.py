
scores = [72, 45, 90, 61, 38]

pass_count = 0
fail_count = 0
total_score = 0

for score in scores:
 
    if score >= 80:
        grade = "A"
    elif score >= 70:
        grade = "B"
    elif score >= 50:
        grade = "C"
    else:
        grade = "F"
    
    
    print(f"Score: {score} - Grade: {grade}")
    
    
    if score >= 50:
        pass_count += 1
    else:
        fail_count += 1
        
    total_score += score

average_score = round(total_score / len(scores), 1)


print(f"\nNumber of learners passed: {pass_count}")
print(f"Number of learners failed: {fail_count}")
print(f"Class average score: {average_score}")