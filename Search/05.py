def solution(idx, jobs, workers, best_time=float('inf')):
	if idx == len(jobs):
		return max(workers)

	for i in range(len(workers)):
		if workers[i] in workers[:i]:
			continue

		if workers[i] + jobs[idx] >= best_time:
			continue

		workers[i] += jobs[idx]
		time = solution(idx + 1, jobs, workers, best_time)
		best_time = min(best_time, time)
		workers[i] -= jobs[idx]

	return best_time


def main():
	jobs, k = input('Enter jobs and number of workers : ').split('/')
	jobs = [int(job) for job in jobs.strip().split(' ')]
	jobs.sort(reverse=True)  # Sort biggest jobs first so we hit best_time faster
	k = int(k)
	workers = [0] * k
	print(f'Minimum time to complete jobs with {k} workers is {solution(0, jobs, workers)}')


if __name__ == '__main__':
	main()