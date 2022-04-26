
# <!----------------BEGIN-HEADER------------------------------------>
# ## ConfigMaker
# A Python package for generating configurations of atoms.
# Code structure inspired by the FitSNAP package.
#
# <!-----------------END-HEADER------------------------------------->


try:
    import mpi4py as mpi4py
    from .parallel_tools import pt

except ModuleNotFoundError:
    from .parallel_tools import pt

except Exception as e:
    print("Trouble importing mpi4py package, exiting...")
    raise e

pt.single_print("-------------------------------------")
pt.single_print("----------- ConfigMaker -------------")
pt.single_print("-------------------------------------")

try:
    pt.single_print("Reading input...")
    pt.all_barrier()
    #from .io.input import config
    pt.single_print("Finished reading input")
    pt.single_print("------------------")

    #from .io.output import output
except Exception as e:
    pt.single_print("Trouble reading input, exiting...")
    pt.exception(e)

try:
    pass
    #output.screen("mpi4py version: ", mpi4py.__version__)

except NameError:
    print("No mpi4py detected, using fitsnap stubs...")

try:
    import numpy as np
    #output.screen("numpy version: ", np.__version__)
except Exception as e:
    pass
    #output.screen("Trouble importing numpy package, exiting...")
    #output.exception(e)

try:
    import scipy as sp
    #output.screen("scipy version: ", sp.__version__)
except Exception as e:
    pass
    #output.screen("Trouble importing scipy package, exiting...")
    #output.exception(e)

try:
    import pandas as pd
    #output.screen("pandas version: ", pd.__version__)
except Exception as e:
    pass
    #output.screen("Trouble importing pandas package, exiting...")
    #output.exception(e)

"""
try:
    import lammps
    lmp = lammps.lammps()
#     print("LAMMPS version: ",lammps.version())
except Exception as e:
    print("Trouble importing LAMMPS library, exiting...")
    raise e
"""
#output.screen("-----------")
