import matplotlib
from Bio import AlignIO, Phylo
from Bio.Phylo.TreeConstruction import DistanceCalculator, DistanceTreeConstructor
import matplotlib.pyplot as plt
import Bio as Bio
from Bio import SeqIO






def phylogenetics(file: str):

    alignment = AlignIO.read(file, "clustal")


    calculator = DistanceCalculator('johnson')
    constructor = DistanceTreeConstructor(calculator)
    tree = constructor.build_tree(alignment)
    tree.ladderize()

    fig = plt.figure(figsize=(20, 5), dpi=100)
    matplotlib.rc('font', size=10)
    matplotlib.rc('xtick', labelsize=10)
    matplotlib.rc('ytick', labelsize=10)
    tree.ladderize()
    Phylo.draw(tree, branch_labels=lambda c: round(c.branch_length, 3))
    fig.savefig("sharks_cladogram")





phylogenetics('../src/Phylogenetics/alignment.aln')