import itertools

def calculate_combinations(elements):
    combinations = []
    for i in range(1, len(elements) + 1):
        sub_combinations = itertools.combinations(elements, i)
        combinations.extend(sub_combinations)
    return combinations

def main():
    input_data = [1, 2, 3]
    combinations = calculate_combinations(input_data)
    print("Intermediate combinations:", combinations)

if __name__ == "__main__":
    main()

def calculate_combinations(elements):
    combinations = []
    for i in range(1, len(elements) + 1):
        sub_combinations = itertools.combinations(elements, i)
        combinations.extend(sub_combinations)
    return combinations

def main():
    input_data = [1, 2, 3]
    combinations = calculate_combinations(input_data)
    print(combinations)

if __name__ == "__main__":
    main()
