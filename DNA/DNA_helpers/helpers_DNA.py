from collections import Counter


def read_code_from_file(file_name: str):
    with open(file_name, 'r') as code:
        lines = code.readlines()
        return ''.join(lines[1:])


class DNA_helpers:
    def __init__(self, DNA_code):
        self.DNA_code = DNA_code.upper()

    def composition(self):
        nucleotides = ['A', 'C', 'T', 'G']
        nuc_comp = {}
        for i in nucleotides:
            nuc_comp[i] = (self.DNA_code.count(i))

        return nuc_comp

    def composition_faster(self):
        counts = Counter(self.DNA_code)
        return {nuc: counts.get(nuc, 0) for nuc in "ACTG"}

    def validate_DNA(self):
        code_len = len(self.DNA_code)
        nuc_count = self.DNA_code.count('A') + self.DNA_code.count('C') + self.DNA_code.count('T') + self.DNA_code.count('G')
        if code_len == nuc_count:
            return True
        else:
            return False

    def dna2rna(self):
        return self.DNA_code.replace('T', 'U')

    def DNAstrand(self):
        strand = ""
        for i in self.DNA_code[::-1]:
            if i == "A":
                strand += "T"
            if i == "T":
                strand += "A"
            if i == "C":
                strand += "G"
            if i == "G":
                strand += "C"
        return strand

    def counting_mutations_rosalind(self,string1, string2):
        distance = 0
        assert len(string1) == len(string2)
        for i in range(len(string1)):
            if string1[i] != string2[i]:
                distance += 1
        return distance

    def subs_rosalind(self, string1, string2):
        loc = []
        for i in range(len(string1)):
            if string2 == string1[i: i + len(string2)]:
                loc.append(i + 1)
        return loc