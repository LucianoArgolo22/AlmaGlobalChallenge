#%%
from client.ClientFinanceValues import FinanceValues
from client.ClientLogger import ClientLogger
from client.ClientMetrics import Metrics
from job.TaskHandler import TaskHandler
while True:
    log = ClientLogger(filename = './FinanceBot.log', app_name = 'FinanceBot')
    #finance_object = FinanceValues(TickerName='DLR', TickerNameFuture='DLR/MAR23', future_date_contract='2023-03-31')
    #metrics_object = Metrics(finance_object=finance_object)
    #metrics_object.implicit_yearly_rate()