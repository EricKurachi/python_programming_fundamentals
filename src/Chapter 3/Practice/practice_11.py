"""
Given what you now know about references, what would print
if the question variable were printed after executing the code
"""

question = ['are', 'you', 'awake', 'for', 'this']
answer = question
answer[0] = answer[3]
answer[1] = answer[4]
answer[4] = answer[2]
answer[2] = 'I'
answer[3] = 'am'
print(answer)
print(question)

'''The most common answer would be that the question prints the initial list, but what you pass to the answer is a
reference, so they change together'''