
# <!----------------BEGIN-HEADER------------------------------------>
# ## ConfigMaker
# A Python package for generating configurations of atoms.
# Code structure inspired by the FitSNAP package.
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

# ASE import
from ase.visualize import view
from ase import Atoms
from ase.io import write

class Configurations:

    def __init__(self):
        print("__init__ Configurations")
        
        # Parse configuration types which define how the configs relate to the given config.
        self.parse_configtypes()
        self.nconfigs = len(self.configtypes)
        print(f"{self.nconfigs} configs.")
        # Parse the given config.
        self.parse_config()
        
        # Initialize list of Atoms object
        self.atoms_list = []
        
        
    def parse_configtypes(self):
        f = open("CONFIGTYPES", 'r')
        self.configtypes=[]
        for line in f:
            strip_lines=line.strip()
            listli=strip_lines.split()
            #print(listli)
            m=self.configtypes.append(listli)
        print(self.configtypes)
        f.close()
        
    def parse_config(self):
    
        # Lattice vector
        f = open("LATVEC", 'r')
        test = np.empty((self.nconfigs,3,3))
        test.fill(np.nan)
        print(test)
        latvec_list = []
        for line in f:
            strip_lines=line.strip()
            listli=strip_lines.split()
            listli = [float(x) for x in listli]
            #print(listli)
            m=latvec_list.append(listli)
        self.latscale = latvec_list[0][0]
        print(self.latscale)
        #print(np.array(latvec_list[1:]))
        self.latvec = np.array(latvec_list[1:])
        print(self.latvec)
        f.close()
        
        # Basis
        f = open("BASIS", 'r')
        self.basis = []
        for line in f:
            strip_lines=line.strip()
            listli=strip_lines.split()
            #print(listli)
            m=self.basis.append(listli)
        print(self.basis)
        self.basis=np.array(self.basis)
        self.basistypes = self.basis[:,0]
        self.basis = self.basis[:,1:]
        f.close()
        
        # Box
        f = open("BOX", 'r')
        box_list = []
        for line in f:
            strip_lines=line.strip()
            listli=strip_lines.split()
            listli = [float(x) for x in listli]
            #print(listli)
            m=box_list.append(listli)
        self.boxscale = float(box_list[0][0])
        #print(self.boxscale)
        #print(box_list[1:])
        self.box = np.array(box_list[1:])
        self.box = self.boxscale*self.box
        print(self.box)
        f.close()
        
        # Type map
        f = open("TYPEMAP", 'r')
        self.map_list = []
        for line in f:
            strip_lines=line.strip()
            #listli=strip_lines.split()
            #listli = [float(x) for x in listli]
            #print(listli)
            m=self.map_list.append(strip_lines)
        print(self.map_list)
        f.close()
        
    # Allocate arrays like positions, types, boxes, etc.
    def allocate(self):
        pass
        
    # Add a config (ASE Atoms object) to the list of configs)
    def add(self,symbols,x,box):
        atoms = Atoms(#numbers=types,
                     symbols=symbols,
                     positions=x,
                     cell=box,
                     pbc=[True, True, True])
        print("numbers:-------")
        print(atoms.numbers)
        self.atoms_list.append(atoms)
        
        
        
