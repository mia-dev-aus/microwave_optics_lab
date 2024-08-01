import math
OPTICAL_PATH = 1.4276
n = 1.5

def calculate_t (n, path_diff):
    t = path_diff / (n - 1);
    return t

print("The thickness required by n =",n," is t =", calculate_t(n, OPTICAL_PATH))
