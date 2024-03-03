codon_table = {
    "UUU": "F", "UUC": "F", "UUA": "L", "UUG": "L",
    "UCU": "S", "UCC": "S", "UCA": "S", "UCG": "S",
    "UAU": "Y", "UAC": "Y", "UAA": "Stop", "UAG": "Stop",
    "UGU": "C", "UGC": "C", "UGA": "Stop", "UGG": "W",
    "CUU": "L", "CUC": "L", "CUA": "L", "CUG": "L",
    "CCU": "P", "CCC": "P", "CCA": "P", "CCG": "P",
    "CAU": "H", "CAC": "H", "CAA": "Q", "CAG": "Q",
    "CGU": "R", "CGC": "R", "CGA": "R", "CGG": "R",
    "AUU": "I", "AUC": "I", "AUA": "I", "AUG": "M",
    "ACU": "T", "ACC": "T", "ACA": "T", "ACG": "T",
    "AAU": "N", "AAC": "N", "AAA": "K", "AAG": "K",
    "AGU": "S", "AGC": "S", "AGA": "R", "AGG": "R",
    "GUU": "V", "GUC": "V", "GUA": "V", "GUG": "V",
    "GCU": "A", "GCC": "A", "GCA": "A", "GCG": "A",
    "GAU": "D", "GAC": "D", "GAA": "E", "GAG": "E",
    "GGU": "G", "GGC": "G", "GGA": "G", "GGG": "G",
}

monoisotopic_mass_table = {
    "A": 71.03711, "C": 103.00919, "D": 115.02694, "E": 129.04259,
    "F": 147.06841, "G": 57.02146, "H": 137.05891, "I": 113.08406,
    "K": 128.09496, "L": 113.08406, "M": 131.04049, "N": 114.04293,
    "P": 97.05276, "Q": 128.05858, "R": 156.10111, "S": 87.03203,
    "T": 101.04768, "V": 99.06841, "W": 186.07931, "Y": 163.06333
}


def count_nucleotides(strand):  # returns dict of counts of nucleotides
    count = {"A": 0, "C": 0, "G": 0, "T": 0}
    for nucleotide in strand:
        if nucleotide not in count.keys():
            continue
        else:
            count[nucleotide] += 1
    return count


def transcribe_to_rna(dna_strand):  # replaces T in DNA with U and returns result
    nstrand = ""
    for nucleotide in dna_strand:
        if nucleotide == "T":
            nstrand += "U"
        else:
            nstrand += nucleotide
    return nstrand


def complement(strand):  # replaces every item with complement
    nstrand = ""
    for i in strand:
        if i == "A":
            nstrand += "T"
        elif i == "T" or i == "U":
            nstrand += "A"
        elif i == "C":
            nstrand += "G"
        else:
            nstrand += "C"
    return nstrand


def aminoacid_chain(rna_strand):  # creates protein chain using codon table
    codon_list = []
    for i in range(0, len(rna_strand), 3):
        codon_list.append(rna_strand[i:i + 3])

    amino_acid_chain = ""
    for i in codon_list:
        if codon_table[i] == "Stop":
            break
        amino_acid_chain += codon_table[i]

    return amino_acid_chain


def protein_mass(protein_string):
    protein_mass = 0
    for i in protein_string:
        protein_mass += monoisotopic_mass_table[i]
    return round(protein_mass, 3)


def hamming_distance(strand1, strand2):  # returns number of point mutations between two sequences
    count = 0
    for i in range(len(strand1)):
        if strand1[i] != strand2[i]:
            count += 1
    return count


def gc_content(strand):
    g = count_nucleotides(strand)["G"]
    c = count_nucleotides(strand)["C"]
    return (g + c) * 100 / (len(strand))






