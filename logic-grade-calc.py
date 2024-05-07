import sys

if (len(sys.argv) != 6):
    print("Usage: {} <number of weeks> <accumulative points> <number of presentations>"
          " <accumulative points> <bonus points>".format(sys.argv[0]))
    exit()
    
num_weeks = int(sys.argv[1])
points_weeks = float(sys.argv[2])
num_presentations = int(sys.argv[3])
points_presentations = float(sys.argv[4])
bonus_points = float(sys.argv[5])

score_with_presentations = ((points_weeks + points_presentations) / (10 * 12 + 14)) * 100
score_total = score_with_presentations + bonus_points

score_conjectorial = ((points_weeks + points_presentations) / (10 * num_weeks + 7 * num_presentations)) * 100
score_conjectorial_pure = points_weeks / (10 * num_weeks) * 100

def score_to_grade(score):
    if score < 50:
        return 5
    elif score < 63:
        return 4
    elif score < 75:
        return 3
    elif score < 88:
        return 2
    else:
        return 1

print("----------------------------------------")
print("Score: {:.2f}\nGrade: {:.2f}".format(score_total, score_to_grade(score_total)))
print("----------------------------------------")
print("Score without bonus points: {:.2f}\nGrade with bonus points {:.2f}".format(score_with_presentations, score_to_grade(score_with_presentations)))
print("----------------------------------------")
print("Conjectorial score without considering bonus points: {:.2f}".format(score_conjectorial))
print("Conjectorial score without consudierung presentation and bonus points: {:.2f}".format(score_conjectorial_pure))
print("----------------------------------------")
print("To attain the highest grade with your current total score {:.2f} (after {} weeks), you would need {:.2f} additional points in total.\n"
      "Relying solely on the following {} weeks' assignments, you would need {:.2f} points for each assignment on average."
    .format(score_total, num_weeks, 88 - score_total, 12 - num_weeks, (88 - score_total) / (12 - num_weeks)))
print("----------------------------------------")
