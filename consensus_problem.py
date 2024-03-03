from algorithms import *

def consensus(profile):
    np = transpose(profile)
    string = ""
    for row in np:
        i = row.index(max(row))
        if i == 0:
            string += "A"
        elif i == 1:
            string += "C"
        elif i == 2:
            string += "G"
        else:
            string += "T"
    return string


dataset = read_fasta_file("test.txt")

dna_strings = []

for i in list(dataset.values()):
    dna_strings.append(list(i))

x = transpose(dna_strings)

profile = []  # A, C, G, T (in that order)
for row in x:
    count = {"A": 0, "C": 0, "G": 0, "T": 0}
    for element in row:
        count[element] += 1
    profile.append(list(count.values()))
profile = transpose(profile)
a = "A: "
for i in profile[0]:
    a += str(i) + " "

c = "C: "
for i in profile[1]:
    c += str(i) + " "

g = "G: "
for i in profile[2]:
    g += str(i) + " "

t = "T: "
for i in profile[3]:
    t += str(i) + " "


print(consensus(profile))
print(a)
print(c)
print(g)
print(t)