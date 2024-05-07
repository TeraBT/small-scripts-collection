import math
import sys

def decay_function(n_0, half_life, h):
    decay_constant = math.log(2) / half_life
    return n_0 * math.pow(math.e, - decay_constant * h)

def medication_level_calc(dose, times_per_day, half_life, duration):
    med_level = 0
    intermission_hours = 24 // times_per_day
    cumulative_hours = duration * 24
    for i in range(0, cumulative_hours):
        med_level = decay_function(med_level, half_life, 1)
        if i % intermission_hours == 0:
            med_level += dose
        print("%dd %dh: %.2f" % (i // 24, i % 24, med_level))

def decay_visualization(n_0, half_life):
    n = n_0
    hours = 0
    while (n / n_0 * 100) >= 2.5:
        n = decay_function(n_0, half_life, hours)
        print("%dd: %.2f%% %.2f" % (hours // 24, n / n_0 * 100, n ))
        hours += 24



num_sys_args = len(sys.argv)
if sys.argv[1] == "-df" and num_sys_args == 5:
    n_0 = int(sys.argv[2])
    half_life = int(sys.argv[3])
    h = int(sys.argv[4])
    print("%.2f" % decay_function(n_0, half_life, h))
elif sys.argv[1] == "-mlc" and num_sys_args == 6:
    dose = int(sys.argv[2])
    times_per_day = int(sys.argv[3])
    half_life = int(sys.argv[4])
    duration = int(sys.argv[5])
    medication_level_calc(dose, times_per_day, half_life, duration)
elif sys.argv[1] == "-dv" and num_sys_args == 4:
    n_0 = int(sys.argv[2])
    half_life = int(sys.argv[3])
    decay_visualization(n_0, half_life)
else:
    print("""USAGE: %s -df n_0 half_life h
        OR: %s -mlc dose times_per_day half_life duration
        OR: %s -dv dn_0 half_life""" % (sys.argv[0], sys.argv[0], sys.argv[0]))
    