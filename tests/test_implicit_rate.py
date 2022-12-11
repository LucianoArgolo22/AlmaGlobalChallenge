#%%

from unittest import TestCase, mock
from unittest.mock import MagicMock
import sys
#sys.path.append('../client')
#sys.path.append('../job')
from threading import Thread
from client.ClientFinanceValues import FinanceValues
from client.ClientMetrics import Metrics
from client.ClientLogger import ClientLogger
import time
#['marketData']['LA']['price']
@mock.patch('client.ClientFinanceValues.FinanceValues.get_future_value', return_value={'marketData':{'LA':{'price':107.4}}})
class MetricsTest(TestCase):
    def test_get_files_from_owner(self, get_future_value):
            logger = ClientLogger(filename = './FinanceBot.log', app_name = 'FinanceBot')
            log = logger.get_log()
            finance_object = FinanceValues(TickerName='Prueba', TickerNameFuture = 'Prueba/MAR23', future_date_contract= '2023-03-31', log=log)
            finance_object.TickerInfo = {'bid': '', 'ask': '', 'regularMarketPrice': 101.96}
            #self.future_price = 107.4
            #metrics_object = Metrics(finance_object=finance_object, log=self.log)
            metrics_object = Metrics(log=log, finance_object=finance_object)
            implicit_rate = metrics_object.implicit_yearly_rate('regularMarketPrice')
            self.assertEqual(implicit_rate, 1.5862767377992748)
