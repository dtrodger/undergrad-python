#David Rodgers
#INFO - I 210
#Extra Credit Homework 6

#Chapter 6 Project 2


# Define a function, rate_score, which receives one parameter, score. If score
# is given no value assign it = 0. Return a string about the value of the score.

def rate_score(score = 0):
    if score < 1000:
        return "Nothing to be proud of."
    elif score >= 1000 and score < 10000:
        return "Not bad."
    elif score >= 10000:
        return "Nice!"

# Call rate_score with various parameters.

print rate_score(50)
print rate_score(5000)
print rate_score(50000)
print rate_score()