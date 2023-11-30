def round_robin(processes, burst_times, quantum):
    n = len(processes)
    wt = [0] * n
    tat = [0] * n
    burst_remaining = burst_times.copy()

    time = 0
    while True:
        done = True
        for i in range(n):
            if burst_remaining[i] > 0:
                done = False
                if burst_remaining[i] > quantum:
                    time += quantum
                    burst_remaining[i] -= quantum
                else:
                    time += burst_remaining[i]
                    wt[i] = time - burst_times[i]
                    burst_remaining[i] = 0

        if done:
            break

    for i in range(n):
        tat[i] = wt[i] + burst_times[i]

    avg_waiting_time = sum(wt) / n
    avg_tat = sum(tat)/n
    print("Round Robin Scheduling:")
    print("Average Waiting Time:", avg_waiting_time)
    print("Average Turn Around Time:", avg_tat)


# Example usage:
if __name__ == "__main__":
    burst_time=[]
    process = []
    print("RR algo")
    process_no= int(input("Enter No of process:"))
    for i in range(process_no):
        process.append(input(f"Enter process {i + 1}: "))
        burst_time.append(int(input("Enter process burst time")))
    quantum = int(input("Enter Time Quantum:"))

    round_robin(process,burst_time,quantum)