"""
CP1404/CP5632 Practical
CSV scores file program - broken one
scores file stores scores for each subject for 10 people.
This code reads the lines into lists, saves the first line as a list of subject codes and
converts the rest of the lines from a list of strings into a list of numbers,
which it then prints with the maximum value for that subject.
Nice. Except, it’s broken! It reads the lists per user not per subject so the results are incorrect.
Use the debugger to follow what it's doing... then fix it.
"""


def main():
    scores_file = open("scores.csv")
    scores_data = scores_file.readlines()
    #print(scores_data)
    subjects = scores_data[0].strip().split(",")
    #print(subjects)
    score_values = []
    for score_line in scores_data[1:]:
        score_strings = score_line.strip().split(",")
        score_numbers = [int(value) for value in score_strings]
        score_values.append(score_numbers)
    scores_file.close()
    for i in range(len(subjects)):
        print(subjects[i], "Scores:")
        total_scores = 0
        count_scores = 0
        min_score = 99999
        for j in range(len(score_values)):
            print(score_values[j][i])
            count_scores += 1
            total_scores += score_values[j][i]
            if min_score > score_values[j][i]:
                min_score = score_values[j][i]
        print("   Minimum Score: {:3d}".format(min_score))
        print("   Average Score: {:6.2f}".format(total_scores/count_scores))

main()