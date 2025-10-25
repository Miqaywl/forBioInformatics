from Bio import SeqIO
seq_name, seq_string = [], []
with open ("rosalind_gc.txt", 'r') as fa:
      for seq_record  in SeqIO.parse(fa,'fasta'):
          seq_name.append(str(seq_record.name))
          seq_string.append(str(seq_record.seq))

strings = {seq_name[i]:seq_string[i] for i in range(len(seq_name))}


def gc(strings):
    gc_contents = {}
    for k, v in strings.items():
        gc_content = 100 * (v.count("G") + v.count("C")) / len(v)
        gc_contents[k] = gc_content

    return gc_contents

print(gc(strings))