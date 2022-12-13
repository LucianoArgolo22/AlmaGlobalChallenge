#%%
import traceback
from client.ClientLogger import ClientLogger
from service.ServiceTicker import ServiceTickerRates
from utils.MiscFunctions import open_json

if __name__ == '__main__':
    logger = ClientLogger(filename = './FinanceBot.log', app_name = 'FinanceBot')
    log = logger.get_log()
    configs = open_json('./utils/config.json')
    configs2 = open_json('./utils/config_2.json')
    
    try:
        #obtengo las tasas implicitas de cada Ticker
        ticker_rates_one_iteration = ServiceTickerRates(configs=configs2, log=log)
        for config in configs2:
            ticker_rates_one_iteration.get_implicit_rates(config=config)

        ticker_rates = ServiceTickerRates(configs=configs, log=log)
        ticker_rates.run_for_all()
    except:
        log.info(f'Internal Thread Error ----- {traceback.format_exc()}')
    
