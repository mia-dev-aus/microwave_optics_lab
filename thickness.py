OPTICAL_PATH = 1.4276
N = 1.5
# calculate thickness of the glass block required to introduce a phase difference
def calculate_t (n, path_diff):
    t = path_diff / (n - 1)
    return t

print("The thickness required by n =",N," is t =", calculate_t(N, OPTICAL_PATH))
