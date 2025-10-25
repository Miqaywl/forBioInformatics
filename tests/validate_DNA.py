from DNA.DNA_helpers.helpers_DNA import DNA_helpers, read_code_from_file


code = read_code_from_file('../src/DNA/gene.fna')
test_DNA = DNA_helpers(code)
# print(test_DNA.composition())
# print(test_DNA.validate_DNA())
# print(test_DNA.DNAstrand())
print(code)