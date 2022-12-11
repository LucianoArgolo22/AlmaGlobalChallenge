#%%
from ClientFinanceValues import FinanceValues
from ClientLogger import ClientLogger
from ClientMetrics import Metrics
from TaskHandler import TaskHandler
while True:
    
    log = ClientLogger(filename = './FinanceBot.log', app_name = 'FinanceBot')
    #finance_object = FinanceValues(TickerName='DLR', TickerNameFuture='DLR/MAR23', future_date_contract='2023-03-31')
    #metrics_object = Metrics(finance_object=finance_object)
    #metrics_object.implicit_yearly_rate()