def naive(p, t):
	#numMatched = 0
	occurrences = []
	for i in range(len(t) - len(p) + 1):  # loop over alignments
		match = True
		for j in range(len(p)):  # loop over characters
			if t[i+j] != p[j]:  # compare characters
				match = False
				break
			if match:
				occurrences.append(i)  # all chars matched; record
				#numMatched = numMatched +1
				#k = occurrences[numMatched-1]
	#print(numMatched)
	return occurrences
	
	
def reverseComplement(s):
    complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A', 'N': 'N'}
    t = ''
    for base in s:
        t = complement[base] + t
    return t
#we saw a function that parses a DNA reference genome from a file in the FASTA format.	
def readGenome(filename):
    genome = ''
    with open(filename, 'r') as f:
        for line in f:
            # ignore header line with genome information
            if not line[0] == '>':
                genome += line.rstrip()
    return genome
	
	
t = readGenome('lambda_virus(1).fa')
p = 'AGGT'
p1 = naive(p, t)
#print(len(p1))

#print((p4))
#print(p4[0])
p2 = reverseComplement('AGGT')
p3 =len(p2) + len(p1)
print((p3))
#p3 = naive(p2, t)
#print(p3[0])
#print(p3)
#p4=len(naive(p2, t))
#print (p3 + p4)


'''
#second problem
p4= 'TTAA'
p5 = naive(p4, t)
print(p5)
'''

# 2. naive_2mm allows up to 2 mismatches per occurrence. 
# As per the question problem we do not consider the reverse complement here
# because We're looking for approximate matches for P itself, not its reverse complement. 
#https://github.com/filipdanic/coursera_ads/blob/7c345813a00fd578ff719f5d8d331e6b8513f7de/homework1/homework1.py
def naive_2mm(p, t):
    occurrences = []
    for i in range(len(t) - len(p) + 1):  # loop over alignments
        mismatches = 0 # counter
        for j in range(len(p)):  # loop over characters
            if t[i+j] != p[j]:  # compare characters
                mismatches += 1
                if mismatches > 2:
                    break
        if mismatches <= 2:
            occurrences.append(i)  # all chars matched; record
    return occurrences
print(len(naive_2mm('TTCAAGCC', t)))
m = (naive_2mm('TTCAAGCC', t))
print(m[0])

'''


Finally, download and parse the provided FASTQ file containing real DNA sequencing reads derived from a human:

https://d28rh4a8wq0iu5.cloudfront.net/ads1/data/ERR037900_1.first1000.fastq

Note that the file has many reads in it and you should examine all of them together when answering this question. The reads are taken from this study:

Ajay, S. S., Parker, S. C., Abaan, H. O., Fajardo, K. V. F., & Margulies, E. H. (2011). Accurate and comprehensive sequencing of personal genomes. Genome research, 21(9), 1498-1505.

This dataset has something wrong with it; one of the sequencing cycles is poor quality.

Report which sequencing cycle has the problem. Remember that a sequencing cycle corresponds to a particular offset in all the reads. For example, if the leftmost read position seems to have a problem consistently across reads, report 0. If the fourth position from the left has the problem, report 3. Do whatever analysis you think is needed to identify the bad cycle. It might help to review the "Analyzing reads by position" video.
'''

def readFastq(filename):
    sequences = []
    qualities = []
    with open(filename) as fh:
        while True:
            fh.readline()  # skip name line
            seq = fh.readline().rstrip()  # read base sequence
            fh.readline()  # skip placeholder line
            qual = fh.readline().rstrip() # base quality line
            if len(seq) == 0:
                break
            sequences.append(seq)
            qualities.append(qual)
    return sequences, qualities
	
_, w = readFastq('ERR037900_1.first1000.fastq')

def lowest_quality_base(qualities):
    total = [0] * len(qualities[0])
    for q in qualities:
        for i, phred in enumerate(q):
            total[i] += phred33ToQ(phred)
    return total.index(min(total))


def phred33ToQ(quality):
    return ord(quality) - 33
	
print(lowest_quality_base(w))



def naive_with_rc(p, t):
    occurrences = []
    for i in range(len(t) - len(p) + 1):  # loop over alignments
        for double_seq in (p, reverseComplement(p)): # check the original and complement
            match = True
            for j in range(len(double_seq)):  # loop over characters
                if t[i+j] != double_seq[j]:  # compare characters
                    match = False
                    break
            if match:
                occurrences.append(i)  # all chars matched; record and 
                break # break, no need to check the complement
    return occurrences
print("problem 1")
# problem 1:
print(len(naive_with_rc('AGGT', t)))
# problem 2:
print(len(naive_with_rc('TTAA', t)))
print(naive_with_rc('ACTAAGT', t)[0])
# problem 4:
print(naive_with_rc('AGTCGA', t)[0])
# problem 5:
print(len(naive_2mm('TTCAAGCC', t)))
# problem 6:
print(naive_2mm('AGGAGGTT', t)[0])

print(lowest_quality_base(w))