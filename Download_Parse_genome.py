# Following line downloads FASTA file containing the lambda phage reference genome
#!wget http://d28rh4a8wq0iu5.cloudfront.net/ads1/data/lambda_virus.fa

def readGenome(filename):
    genome = ''
    with open(filename, 'r') as f:
        for line in f:
            # ignore header line with genome information
            if not line[0] == '>':
                genome += line.rstrip()
    return genome
genome = readGenome('lambda_virus.fa')
genome[:100]


# Count the number of occurences of each base
counts = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
for base in genome:
    counts[base] += 1
print(counts)



import collections
collections.Counter(genome)

