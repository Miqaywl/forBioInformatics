class Amino:
    def __init__(self, amino_sequence):
        self.amino_seqience = amino_sequence

    def find_amino_consitention(self, amino):
        amino_len = len(self.amino_seqience)
        amino_quantity = self.amino_seqience.count(amino)
        result = amino_len * (amino_quantity / 100)
        print(f'{result}%')
        return f'{result}%'