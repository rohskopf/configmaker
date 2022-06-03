
# <!----------------BEGIN-HEADER------------------------------------>
# ## ConfigMaker
# A Python package for generating configurations of atoms.
#
# <!-----------------END-HEADER------------------------------------->

from .configurations import Configurations
from .generate.generator import Generator

class ConfigMaker:
    def __init__(self):

        #self.scraper = scraper(config.sections["SCRAPER"].scraper)

        # Initialize Configurations object, which will store the configuration types and given config.
        self.configurations = Configurations()

        # Initialize Generator object.
        self.generator = Generator(self.configurations)
      
