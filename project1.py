print ("Programmed by: Daniel Rojas") 
print ("Project 1: Machine Scheduling with Deadlines to Minimize the Sum of Lateness")
print ("Reading jobs.txt")
wordList = open('jobs.txt', "r")
words = wordList.read().split()
totalJobs = len(words) // 2

jobsHash = {}
sortedDeadlines = []

class job:
	processTime = 0
	jobNumber = 0

jobs = [job() for i in range(totalJobs)]

#add data from text file to "jobs" hashMap 
#also create a list that only contains deadline data
i = 0
for x in range(0,len(words)):
	if(x % 2 == 0):
		jobs[i].processTime = int(words[x])
	else:
		deadline = int(words[x])
		jobsHash.update({deadline:jobs[i]})
		jobsHash[deadline].jobNumber = i
		sortedDeadlines.append(deadline)
		i += 1

sortedDeadlines.sort()

print ("The best order to schedule the jobs is:")

#match sorted deadline keys with "jobs"
totalLateness = 0
time = 0
for x in range(0,totalJobs):
	deadline = sortedDeadlines[x]
	currentJob = jobsHash[deadline]
	time += currentJob.processTime
	if (time - deadline > 0):
			totalLateness += time - deadline
	print (jobsHash[sortedDeadlines[x]].jobNumber),

print ("\nIt has a total lateness of %d." % (totalLateness))
