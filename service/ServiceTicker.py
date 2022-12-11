#%%
import sys
sys.path.append('../client')
sys.path.append('../job')
from threading import Thread
from client.ClientFinanceValues import FinanceValues
from client.ClientMetrics import Metrics
from job.TaskHandler import TaskHandler
from utils.MiscFunctions import open_json
import time

class ServiceTickerRates:
    """
    Service Ticker Rates is in charge of running the whole process over and over
    so if a new opportunity of arbitrion appears
    then it catches it
    """
    def __init__(self, log:object, configs:list):
        self.log = log
        self.configs = configs
    
    def run_service_for_Ticker(self, config) -> None:
        handler = TaskHandler(log=self.log)
        while True:
            finance_object = FinanceValues(TickerName=config['TickerName'], TickerNameFuture = config['TickerNameFuture'], future_date_contract= config['FutureDate'], log=self.log)
            metrics_object = Metrics(finance_object=finance_object, log=self.log)

            implicit_taker_rate = metrics_object.get_implicit_taker_rate()
            implicit_maker_rate = metrics_object.get_implicit_maker_rate()
            implicit_spot_rate =  metrics_object.get_implicit_spot_rate()

            handler.implicit_maker_setter(new_value=implicit_taker_rate)
            handler.implicit_taker_setter(new_value=implicit_maker_rate)
            handler.implicit_taker_setter(new_value=implicit_spot_rate)
            implicit_spot_rate =  metrics_object.get_implicit_spot_rate()

            if metrics_object.arbitration_chance(implicit_maker_rate, implicit_taker_rate):
                self.log.warning('Arbitritation Can be done')
            
            time.sleep(10)
    
    def run_for_all(self) -> None:
        for config in self.configs:
            print(config)
            thread = Thread(target= self.run_service_for_Ticker, args=(config,))
            thread.start()

