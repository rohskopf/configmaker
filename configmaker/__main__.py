
# <!----------------BEGIN-HEADER------------------------------------>
# ## ConfigMaker
# A Python package for generating configurations of atoms.
# Code structure inspired by the FitSNAP package.
#
# <!-----------------END-HEADER------------------------------------->

from .configmaker import ConfigMaker

#@pt.single_timeit
def main():
    try:
        print("__main.py__ function")
        cm = ConfigMaker()
        #print("ADSF")
        #snap.scrape_configs()
        #snap.process_configs()
        #pt.all_barrier()
        #snap.perform_fit()
        #snap.write_output()
    except Exception as e:
        print("__main.py__ exception")


if __name__ == "__main__":
    main()
