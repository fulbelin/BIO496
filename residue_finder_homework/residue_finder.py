class Atom():
    def __init__(self, boluk):
        self.atomName = boluk[2]
        self.atomNumber = boluk[1]
        self.coordinates = [boluk[6],boluk[7],boluk[8]]

class Protein():
    def __init__(self, name, boluk):
        self.proteinName = name
        self.residueList = boluk

class Residue():
    def __init__(self, name, boluk):
        self.residueName = name
        self.atomList = boluk

filepath = 'C:\\Users\\HP\\PycharmProjects\\Hw7\\1ubq.pdb'
def pdbread(filepath):
    coordinates = []
    blank = []
    residueList={}
    proteinName = []
    with open(filepath) as pdbfile:
        for line in pdbfile:
            if line.startswith('ATOM'):
                boluk = line.split()
                atomName = boluk[2]
                atomNumber = boluk[1]
                atomList = boluk
                coordinates.append([boluk[6],boluk[7],boluk[8]])
                residueName = boluk[3]
                if line.split()[3] not in residueList:
                    residueList[line.split()[3]] = []
                    residueList[line.split()[3]].append(Atom(line.split()))
                else:
                    residueList[line.split()[3]].append(Atom(line.split()))
    for residue in residueList:
        blank.append(Residue(residue, residueList[residue]))

    with open(filepath) as pdbfile2:
        for i, line in enumerate(pdbfile2):
            if i == 3:
                separated = line.split()
                proteinName_x = separated[3].strip(';')
                proteinName.append(proteinName_x)

    return proteinName, blank



ubq = Protein(pdbread(filepath)[0], pdbread(filepath)[1])

print(ubq.proteinName)
print(ubq.residueList[4].residueName)
print(ubq.residueList[4].atomList[3].atomName)
print(ubq.residueList[4].atomList[3].coordinates)
