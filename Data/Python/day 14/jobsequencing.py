class Job:
    def __init__(self, job_id, deadline, profit):
        self.job_id = job_id
        self.deadline = deadline
        self.profit = profit

def job_sequencing(jobs):
    # Step 1: Sort jobs by profit in descending order
    jobs.sort(key=lambda x: x.profit, reverse=True)

    n = max(job.deadline for job in jobs)
    slots = [False] * n        # Track filled time slots
    result = [None] * n        # Store job IDs in slots

    total_profit = 0

    for job in jobs:
        # Find a free slot for this job (latest before deadline)
        for i in range(min(n, job.deadline) - 1, -1, -1):
            if not slots[i]:
                slots[i] = True
                result[i] = job.job_id
                total_profit += job.profit
                break

    print("Scheduled Jobs:", ' → '.join([job for job in result if job]))
    print("Total Profit:", total_profit)

# Sample Jobs
jobs = [
    Job('J1', 3, 100),
    Job('J2', 1, 19),
    Job('J3', 2, 27),
    Job('J4', 1, 25),
    Job('J5', 3, 15)
]

job_sequencing(jobs)