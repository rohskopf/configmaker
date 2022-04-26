from ase import Atoms
from ase.io import read, write, extxyz, vasp

# Count number of configurations in file
fh = open("Si2.xyz", "r")
data = fh.read()
nconfigs = data.count("Lattice=")
print(f"nconfigs: {nconfigs}")


atoms = read('Si2.xyz', index=':') # Read all
#atoms = read('Si2.xyz', index='0:2') # Read a specific slice

#atoms = extxyz.read_extxyz("Si2.xyz")

#print(atoms[0])

# Loop through all atoms and make a POSCAR.
for m in range(0,nconfigs):
    fname = f'POSCAR{m}'
    vasp.write_vasp(fname,atoms[m])
