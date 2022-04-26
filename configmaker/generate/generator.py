# <!----------------BEGIN-HEADER------------------------------------>
# ## FitSNAP3
# A Python Package For Training SNAP Interatomic Potentials for use in the LAMMPS molecular dynamics package
#
# _Copyright (2016) Sandia Corporation.
# Under the terms of Contract DE-AC04-94AL85000 with Sandia Corporation,
# the U.S. Government retains certain rights in this software.
# This software is distributed under the GNU General Public License_
# ##
#
# #### Original author:
#     Aidan P. Thompson, athomps (at) sandia (dot) gov (Sandia National Labs)
#     http://www.cs.sandia.gov/~athomps
#
# #### Key contributors (alphabetical):
#     Mary Alice Cusentino (Sandia National Labs)
#     Nicholas Lubbers (Los Alamos National Lab)
#     Maybe me ¯\_(ツ)_/¯
#     Adam Stephens (Sandia National Labs)
#     Mitchell Wood (Sandia National Labs)
#
# #### Additional authors (alphabetical):
#     Elizabeth Decolvenaere (D. E. Shaw Research)
#     Stan Moore (Sandia National Labs)
#     Steve Plimpton (Sandia National Labs)
#     Gary Saavedra (Sandia National Labs)
#     Peter Schultz (Sandia National Labs)
#     Laura Swiler (Sandia National Labs)
#
# <!-----------------END-HEADER------------------------------------->

#from ..io.input import config
#from os import path, listdir, stat
import numpy as np
#from random import shuffle
#from ..parallel_tools import pt
#from ..io.output import output
#from ..units.units import convert
#from copy import copy
# from natsort import natsorted
from ..parallel_tools import pt

# ASE import
from ase.visualize import view
from ase import Atoms
from ase.io import write

# Others
import ctypes



class Generator:

    def __init__(self, configurations):
        print("__init__ Generator")
        #print(configurations.basis)
        #configurations.basis = 0
        #self.lmp.one("units metal")
        self._initialize_lammps(configurations)
        
        self.generate(configurations)
        
        # Close lammps
        self._lmp = pt.close_lammps()
        
        # Write configs
        self.write(configurations)
        
    def _initialize_lammps(self,configurations):
        print("Initializing LAMMPS")
        self._lmp = pt.initialize_lammps(0,0)
        self._lmp.command(f"neighbor 1.0 multi")
        self._lmp.command(f"units metal")
        self._lmp.command(f"atom_style atomic")
        self._lmp.command(f"atom_modify map array")
        
        #self._lmp.command(f"lattice diamond 5.46")
                                                                     
        lattice_custom_str = f"lattice custom {configurations.latscale} a1 {configurations.latvec[0][0]} {configurations.latvec[0][1]} {configurations.latvec[0][2]} \
                                                                        a2 {configurations.latvec[1][0]} {configurations.latvec[1][1]} {configurations.latvec[1][2]} \
                                                                        a3 {configurations.latvec[2][0]} {configurations.latvec[2][1]} {configurations.latvec[2][2]} "
                                                                        
        nbasis = np.shape(configurations.basis)[0]
        for b in range(0,nbasis):
            lattice_custom_str = lattice_custom_str + f"basis {configurations.basis[b][0]} {configurations.basis[b][1]} {configurations.basis[b][2]} "
            
        #print(lattice_custom_str)
        self._lmp.command(lattice_custom_str)
        #self._lmp.command(f"region box prism 0 1 0 1 0 1 0 0 0 units lattice")
        region_str = f"region box prism 0 {configurations.box[0][0]} 0 {configurations.box[1][1]} 0 {configurations.box[2][2]} {configurations.box[0][1]} {configurations.box[0][2]} {configurations.box[1][2]} units box"
        self._lmp.command(region_str)
        #self._lmp.command(f"region box prism 0 5.46 0 5.46 0 5.46 0 0 0 units box")
        
        
        self._lmp.command(f"create_box 1 box") # change 1 to number of atom types.
        ### Create atom type 1 in the box
        #self._lmp.command(f"create_atoms 1 random 17 1919191 NULL") # Positions don't matter... just declare the memory
        self._lmp.command(f"create_atoms 1 region box basis 1 1 basis 2 1") # See create_atoms command to see how we will change the atom types.
        
        natoms = self._lmp.get_natoms()
        print(f"{natoms} atoms.")
        #x = self._lmp.numpy.gather_atoms("x",1,3)
        
        # Get positions, types, and box.
        self.x = self._lmp.numpy.extract_atom_darray(name="x", nelem=natoms, dim=3)
        print("Given positions:")
        print(self.x)

        self.type = self._lmp.numpy.extract_atom_iarray(name="type", nelem=natoms)
        print("Given types:")
        print(self.type)
        # Create list of symbols from types
        self.symbols = []
        for i in range(0,natoms):
            self.symbols.append(configurations.map_list[self.type[i]-1])
        print(self.symbols)
        
        boxlo,boxhi,xy,yz,xz,periodicity,box_change = self._lmp.extract_box()
        self.box = np.array([[boxhi[0], xy, xz],
                             [xy, boxhi[1], yz],
                             [xz, yz, boxhi[2]]])
        print("Given box:")
        print(self.box)
        
    def generate(self,configs):
    
        for m in range(0,configs.nconfigs):
            print(f"Making config {m}.")
            configtype = configs.configtypes[m][0][0]
            if (configtype=='0'):
                configs.add(self.symbols, self.x, self.box)
                print("Zero!")
            elif (configtype=='1'):
                print("One!")
            else:
                print("Unrecognized config type.")
                
    def write(self, configs):
    
        # VASP
        write("POSCAR", configs.atoms_list, "vasp", parallel=False, append=False)
    
        # ASE exyz
        """
        print(configs.atoms_list)
        write("output.exyz", configs.atoms_list, "extxyz", parallel=False, append=False)
        """
