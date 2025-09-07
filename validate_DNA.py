from helpers import DNA_helpers, read_code_from_file


code = read_code_from_file('DNA_code.txt')
test_DNA = DNA_helpers(code)
print(test_DNA.composition())
print(test_DNA.validate_DNA())

