# Daily Coding Challenge https://www.freecodecamp.org/learn

'''
Passing Exam Count
Given an array of student exam scores and the score needed to pass it, return the number of students that passed the exam.
'''
def passing_count(scores, passing_score):
    i=0
    while(True):
       if i>len(scores)-1:
          break
       elif scores[i]<passing_score:
        scores.remove(scores[i])
       else:
          i+=1
    return len(scores)

print(passing_count([84, 65, 98, 53, 58, 71, 91, 80, 92, 70, 73, 83, 86, 69, 84, 77, 72, 58, 69, 75, 66, 68, 72, 96, 90, 63, 88, 63, 80, 67], 60))

'''
No Consecutive Repeats
Given a string, determine if it has no repeating characters.

A string has no repeats if it does not have the same character two or more times in a row.
'''
def has_no_repeats(s):
    i=0
    formatted_s=s.replace(' ', '')
    while(True):
       if i>=len(formatted_s)-1:
          break
       elif formatted_s[i] is formatted_s[i+1]:
          return False
       else:
          i+=1
          continue
          
    return True   

print(has_no_repeats("hi world"))

'''
Cooldown Time
Given two timestamps, the first representing when a user finished an exam, and the second representing the current time, determine whether the user can take an exam again.

Both timestamps will be given the format: "YYYY-MM-DDTHH:MM:SS", for example "2026-03-25T14:00:00". Note that the time is 24-hour clock.
A user must wait at least 48 hours before retaking an exam.
'''
def can_retake(finish_time, current_time):

    return finish_time

print(can_retake("2026-03-23T08:00:00", "2026-03-25T14:00:00")) # True
print(can_retake("2026-03-24T14:00:00", "2026-03-25T10:00:00")) # False
print(can_retake("2026-03-23T09:25:00", "2026-03-25T09:25:00")) # True
print(can_retake("2026-03-25T11:50:00", "2026-03-23T11:49:59")) # False