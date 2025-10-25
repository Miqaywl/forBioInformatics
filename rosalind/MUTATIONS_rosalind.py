with open("rosalind_hamm.txt", "r") as f:
    string1 = f.readline().strip()
    string2 = f.readline().strip()


def hamm(string1, string2):
    distance = 0
    assert len(string1) == len(string2)
    for i in range(len(string1)):
        if string1[i] != string2[i]:
            distance += 1
    return distance


print(hamm(string1, string2))

