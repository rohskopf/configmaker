
# <!----------------BEGIN-HEADER------------------------------------>
# ## ConfigMaker
# A Python package for generating configurations of atoms.
# Code structure inspired by the FitSNAP package.
#
# <!-----------------END-HEADER------------------------------------->

from .parallel_tools import pt
from .configurations import Configurations
from .generate.generator import Generator
#from .scrapers.scraper_factory import scraper
#from .calculators.calculator_factory import calculator
#from .solvers.solver_factory import solver
#from .io.output import output
#from .io.input import config


class ConfigMaker:
    def __init__(self):
        
        #self.scraper = scraper(config.sections["SCRAPER"].scraper)
        
        # Initialize Configurations object, which will store the configuration types and given config.
        self.configurations = Configurations()
        
        # Initialize Generator object.
        self.generator = Generator(self.configurations)
       
        #print(configurations)
        #self.data = []
        #self.calculator = calculator(config.sections["CALCULATOR"].calculator)
        #self.solver = solver(config.sections["SOLVER"].solver)
        #self.fit = None
        #self.multinode = 0
        #if config.sections["EXTRAS"].only_test:
        #    self.fit = output.read_fit()
        
        #pass
      

    """
    @pt.single_timeit
    def scrape_configs(self):
        self.scraper.scrape_groups()
        self.scraper.divvy_up_configs()
        self.data = self.scraper.scrape_configs()
        del self.scraper

    @pt.single_timeit
    def process_configs(self):
        self.calculator.create_a()
        for i, configuration in enumerate(self.data):
            self.calculator.process_configs(configuration, i)
        del self.data
        self.calculator.extras()

    @pt.single_timeit
    def perform_fit(self):
        if not config.args.perform_fit:
            return
        elif self.fit is None:
            self.solver.perform_fit()
        else:
            self.solver.fit = self.fit
        self.solver.fit_gather()
        self.solver.error_analysis()

    @pt.single_timeit
    def write_output(self):
        output.output(self.solver.fit, self.solver.errors)
    """
