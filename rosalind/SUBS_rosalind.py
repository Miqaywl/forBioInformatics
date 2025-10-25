with open("rosalind_subs.txt", 'r') as f:
    string1 = f.readline().strip()
    string2 = f.readline().strip()

def subs(string1, string2):
    loc = []
    for i in range(len(string1)):
        if string2 == string1[i: i+len(string2)]:
            loc.append(i+1)
    return loc



print(subs(string1, string2))