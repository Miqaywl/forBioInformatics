class Amino:
    def __init__(self, amino_sequence):
        self.amino_seqience = amino_sequence

    def find_amino_consitention(self, amino):
        amino_len = len(self.amino_seqience)
        amino_quantity = self.amino_seqience.count(amino)
        result = (amino_quantity / amino_len) * 100
        print(f'{result}%')
        print(amino_len)
        return f'{result}%'