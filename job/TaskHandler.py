
class TaskHandler:
    def __init__(self, log:object):
        self.implicit_rate_value = 0
        self.log = log
    
    def compare_rates(self, new_value:float) -> None: 
        """_summary_
        Dado que el futuro y el contado mantienen una correlación "perfecta"(en teoría
        , entiendo que es una clase de peg), hay momentos que por muy poco tiempo se rompe
        dando lugar a una oportunidad para arbitrar comprando futuros para obtener un mayor porcentaje
        o por el contrario vendiendo spot para obtener un mejor valor en relación al futuro (y posteriormente
        cuando el precio se nivele o vuelva a su correlación adecuada, comprar más futuros)
        Args:
                    new_value (_type_): the new implicit rate
        """
        if new_value < self.implicit_rate_value:
            self.buying_opportunity_alarm(new_value=new_value)
        elif self.implicit_rate_value < new_value:      
            self.selling_opportunity_alarm(new_value=new_value)
        
    def buying_opportunity_alarm(self, new_value) -> None:
        self.log.warning(f'new implicit rate: {new_value} \n Last implicit rate: {self.implicit_rate_value} \
                        \n Opportunity to get better Rate buying Future')
        self.implicit_rate_value = new_value                          

    def selling_opportunity_alarm(self, new_value) -> None:
        self.log.warning(f'new implicit rate: {new_value} \n Last implicit rate: {self.implicit_rate_value} \
            \n Opportunity to Sell at a better price')
        self.implicit_rate_value = new_value      
    