from helpers import read_code_from_file
from helpers_for_amino import Amino


code = read_code_from_file('AMINO_codes/amino_code')
amino = Amino(code)
amino.find_amino_consitention('V')