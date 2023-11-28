# SimLibrary.py python file

def read_config_file(region):
    try:
        filename = input("Enter the name of the file containing initial simulation information: ")
        while True:
            try:
                with open('input1.txt', 'r') as file:
                    threshold = int(file.readline().strip())
                    infectious_period = int(file.readline().strip())
                    data = file.readlines()
                    for line in data:
                        line = line.strip()
                        if not line:
                            continue
                        region.append(list(line))
                    return threshold, infectious_period
            except FileNotFoundError:
                filename = input("File not found. Please enter a valid filename: ")
    except Exception as e:
        print(f"Error: {e}")
        exit(-2)

def output_initial_state(region):
    print("Day 0:")
    for row in region:
        print("".join(row))
        

def simulate_outbreak(region, threshold, infectious_period, susceptible_counts, infectious_counts, recovered_counts):
    day = 1
    while 'i' in ''.join([''.join(row) for row in region]):
        for i in range(len(region)):
            for j in range(len(region[i])):
                if region[i][j] == 's':
                    if count_infectious(region, i, j) >= threshold:
                        region[i][j] = 'i'
                elif region[i][j] == 'i':
                    if count_infectious_period(region, i, j) >= infectious_period:
                        region[i][j] = 'r'
        output_state(region, day)
        count_people(region, susceptible_counts, infectious_counts, recovered_counts)
        day += 1
    return day - 1
    
    

def count_infectious(region, i, j):
    count = 0
    for x in range(i - 1, i + 2):
        for y in range(j - 1, j + 2):
            if 0 <= x < len(region) and 0 <= y < len(region[i]):
                if region[x][y] == 'i':
                    count += 1
    return count

def count_infectious_period(region, i, j):
    count = 0
    for x in range(i - 1, i + 2):
        for y in range(j - 1, j + 2):
            if 0 <= x < len(region) and 0 <= y < len(region[i]):
                if region[x][y] == 'i':
                    count += 1
    return count




def output_state(region, day):
    print(f"Day {day}:")
    for row in region:
        print("".join(row))




def count_people(region, susceptible_counts, infectious_counts, recovered_counts):
    susceptible_counts.append(sum(row.count('s') for row in region))
    infectious_counts.append(sum(row.count('i') for row in region))
    recovered_counts.append(sum(row.count('r') for row in region))
    
    

def plot_results(susceptible_counts, infectious_counts, recovered_counts, outbreak_duration):
    import matplotlib.pyplot as plt

    days = list(range(outbreak_duration + 1))

    plt.plot(days, susceptible_counts, label="Susceptible")
    plt.plot(days, infectious_counts, label="Infectious")
    plt.plot(days, recovered_counts, label="Recovered")

    plt.title("Outbreak Simulation")
    plt.xlabel("Days")
    plt.ylabel("Number of People")
    plt.legend()
    plt.show()
