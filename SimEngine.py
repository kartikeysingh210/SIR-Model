# SimEngine.py
import SimLibrary

def main():
    region = []
    susceptible_counts = []
    infectious_counts = []
    recovered_counts = []

    threshold, infectious_period = SimLibrary.read_config_file(region)
    SimLibrary.output_initial_state(region)
    outbreak_duration = SimLibrary.simulate_outbreak(region, threshold, infectious_period, susceptible_counts, infectious_counts, recovered_counts)

    print("Final state of the region:")
    SimLibrary.output_state(region, outbreak_duration)
    print(f"Outbreak lasted for {outbreak_duration} days")
    max_infectious_count = max(infectious_counts)
    day_max_infectious = infectious_counts.index(max_infectious_count)
    print(f"Highest count of infectious individuals ({max_infectious_count}) occurred on Day {day_max_infectious}")

    SimLibrary.plot_results(susceptible_counts, infectious_counts, recovered_counts, outbreak_duration)

if __name__ == "__main__":
    main()
