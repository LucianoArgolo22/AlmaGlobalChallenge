class TaskHandler:
    """
    The Task Handler is in charge of handling the new values that generates
    the metrics each time, so if those change, then TaskHandler is updated
    """

    def __init__(self, log:object):
        self.implicit_taker_value = 0
        self.implicit_maker_value = 0
        self.implicit_spot_value = 0
        self.log = log
    
    @staticmethod
    def compare_values(previous_value , new_value) -> float: 
        return previous_value != new_value

    def implicit_maker_setter(self, new_value) -> None:
        if TaskHandler.compare_values(previous_value=self.implicit_maker_value, \
                                    new_value=new_value):
            self.log.info(f'New implicit maker rate {new_value }')
            self.implicit_maker_value = new_value                          

    def implicit_taker_setter(self, new_value) -> None:
        if TaskHandler.compare_values(previous_value=self.implicit_taker_value, \
                                    new_value=new_value):
            self.log.info(f'New implicit taker rate {new_value}')
            self.implicit_taker_value = new_value      
    
    def implicit_spot_setter(self, new_value) -> None:
        if TaskHandler.compare_values(previous_value=self.implicit_taker_value, \
                                    new_value=new_value):
            self.log.info(f'New implicit spot rate {new_value}')
            self.implicit_spot_value = new_value   
