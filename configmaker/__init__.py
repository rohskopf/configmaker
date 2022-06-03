
# <!----------------BEGIN-HEADER------------------------------------>
# ## ConfigMaker
# A Python package for generating configurations of atoms.
#
# <!-----------------END-HEADER------------------------------------->

#pt.single_print("-------------------------------------")
#pt.single_print("----------- ConfigMaker -------------")
#pt.single_print("-------------------------------------")


try:
    import lammps
    lmp = lammps.lammps()
#     print("LAMMPS version: ",lammps.version())
except Exception as e:
    print("Trouble importing LAMMPS library, exiting...")
    raise e
