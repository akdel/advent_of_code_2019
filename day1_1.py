
def fuel(mass):
    return int(mass/3) - 2


if __name__ == "__main__":
    masses = sum([fuel(int(x.strip())) for x in open("day1.txt", "r").readlines() if len(x.strip()) > 0])
    print(masses)
