def fcfs(process, burst_time):
    n = len(process)
    wt = [0] * n
    tat = [0] * n

    for i in range(1, n):
        wt[i] = wt[i - 1] + burst_time[i - 1]

    for i in range(n):
        tat[i] = wt[i] + burst_time[i]

    avg_wt = sum(wt) / n
    avg_tat = sum(tat) / n
    print("Average Waiting time:", avg_wt)
    print("Average Turnaround time:", avg_tat)

if __name__ == "__main__":
    burst_time = []
    process = []
    print("FCFS algo")
    process_no = int(input("Enter No of processes:"))
    for i in range(process_no):
        process.append(i + 1)
        burst_time.append(int(input(f"Enter burst time for process {i + 1}: ")))

    fcfs(process, burst_time)
