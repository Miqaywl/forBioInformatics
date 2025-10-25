from AMINO.amino_helpers.helpers_for_amino import Amino
from DNA.DNA_helpers.helpers_DNA import read_code_from_file

code = read_code_from_file('AMINO/amino_code')
# code = '''MGLSDGEWQLVLNVWGKVEADIPGHGQEVLIRLFKGHPETLEKFDKFKHLKSEDEMKASEDLKKHGATVLTALGGILKKKGHHEAEIKPLAQSHATKHKIPVKYLEFISECIIQVLQSKHPGDFGADAQGAMNKALELFRKDMASNYKELGFQG'''
amino = Amino(code)
amino.find_amino_consitention('V')
print(code)