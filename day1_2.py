from day1_1 import fuel

def fuel_complete(mass):
    def fuel_recursive(mass, acc):
        if mass < 0:
            return acc
        else:
            return fuel_recursive(fuel(mass), acc+mass)
    return fuel_recursive(mass, -mass)


if __name__ == "__main__":
    masses = sum([fuel_complete(int(x.strip())) for x in open("day1.2.txt", "r").readlines() if len(x.strip()) > 0])
    print(masses)