# FinanceBot English

### Dependencies:
    - Pyrofex
    - Yfinance
    - logging
    - Datetime
    - Threading
    - sys
    - Unittest

(Tests are in tests folder)

The Main program runs inside the Client Logger to generate a log of what happens so it has
traceability.

On the other hand it generates two objects with the Ticker Rates service to be able to do on one side:
 - with config2.json get one-time implicit rates
 - with the config.json continuously obtain the implicit rate to detect a variation of it and see if there may be an arbitrage opportunity.
 
 The ServiceTickerRates inside works with the classes:
 - FinanceValues, which obtains through pyrofex and yfinance all the necessary financial values
 - Metrics, which receives an object of type FinanceValues as a parameter and generates the implicit rate with the information inside the FinanceValues object
 - TaskHandler, which is in charge of being the handrail that receives again and again the new implicit rates that each object obtains, in this way generating a comparison between rates and seeing if the correlation is broken, favoring some arbitration opportunity.
 
 How was the arbitration alarm considered?
 (Based on the article https://www.estrategiasdeinversion.com/herramientas/diccionario/trading/arbitraje-entre-futuro-y-contado-t-847)
 - I quote a fragment of the link: "The prices of futures on shares move in parallel to the prices of shares. This is a direct consequence of the arbitration relationship that ensures the convergence of futures prices with shares at expiration The forward price of a share is equal to the current share price plus interest on said price for the term to be determined...". Based then on the concept of the correlation between the stock and the future of that stock, I can understand that arbitrage opportunities occur when there is a variation in the existing correlation. That's when I find the opportunity to do arbitration.
 - The scenarios I understand are:
     - If the implicit rate changes and is higher than what it was, it is either because the spot value went down, breaking the correlation, or the future value went up, or perhaps both, giving an opportunity to buy in case that the spot has lowered its value (buying cheaper), or to sell futures in case the future has increased its value (selling more expensive).
     - Analogous case would be that the implicit rate changes and is less than what it was, because the spot increased, because the future fell, or because both made an increase on the spot side and a drop on the future side. Given a similar opportunity, I understand that to buy cheaper futures, or to sell more expensive spot.
     - The alarms that I made in the "compare_rates" of the "TaskHandler" class are for two specific cases (although as I described above I see that there is a broader spectrum of possibilities). I refer to the lines of code:
     
        """
           if new_value < self.implicit_rate_value:
               self.buying_opportunity_alarm(new_value=new_value)
           elif self.implicit_rate_value < new_value:      
               self.selling_opportunity_alarm(new_value=new_value)
        """
        
1) In case the rate increases, notice of a sale opportunity, the sale opportunity would be in the case of being able to sell a more expensive future.
2) In the event that the rate decreases, purchase opportunity notice, the purchase opportunity would be in the case of being able to buy a cheaper future.
---------------------------
# FinanceBot Español

(Los Tests están en la carpeta tests)

El programa Main corre por dentro el Client Logger para generar un log de lo que ocurre y tener
trazabilidad.

por otro lado Genera dos objetos con el service Ticker Rates para poder hacer por un lado:
 - con la config2.json obtener por única vez las tasas implícitas
 - con la config.json obtener continuamente la tasa implícita para detectar una variación de la misma y ver si puede existir una oportunidad de arbitraje.

El ServiceTickerRates por dentro funciona con las clases:
 - FinanceValues, que obtiene mediante pyrofex y yfinance todos los valores financieros necesarios
 - Metrics, que recibe por parámetro un objeto del tipo FinanceValues y genera la tasa implícita con la información dentro del objeto FinanceValues
 - TaskHandler, que se encarga de ser el pasamanos que recibe una y otra vez las nuevas tasas implícitas que obtiene cada objeto, de ésta manera generando una comparación entre tasas y viendo si se rompe la correlación, favoreciendo alguna oportunidad de arbitraje.
 
¿Cómo se consideró la alarma de arbitrajes?
 (Basado en el artículo https://www.estrategiasdeinversion.com/herramientas/diccionario/trading/arbitraje-entre-futuro-y-contado-t-847)
 - Cito un fragmento del link : "Los precios de los futuros sobre acciones se mueven en paralelo a los precios de las acciones. Esto es consecuencia directa de la relación de arbitraje que asegura a vencimiento la convergencia de los precios de los futuros con las acciones. El precio a plazo de una acción es igual al precio actual de la acción más los intereses sobre dicho precio al plazo que se quiere determinar..." . Basado entonces en el concepto de la correlación entre la acción y el futuro de esa acción, puedo comprender que las oportunidades de arbitraje se dan cuando se genera una variación en la correlación que hay (en el caso del ejercicio, la tasa implícita que varía debido a los precios del futuro y del spot). Es entonces ahí cuando me encuentro la oportunidad de arbitrar. 
 - Los escenarios que comprendo son:
     - Si la tasa implícita cambia y es mayor a lo que era, es o por que el valor spot varío bajando rompiendo la correlación, o lo hizo el valor del futuro subiendo, o tal vez ambos, dándo oportunidad (entiendo) a comprar en caso que el spot haya bajado su valor (comprando más barato), o a vender futuros en caso que el futuro haya aumentado su valor (vendiendo más caro).
     - Caso análogo sería que la tasa implicita cambia y es menor a lo que era, por que el spot aumentó, por que el futuro bajó, o por que ambos hicieron un aumento por el lado spot y una baja por el lado futuro. Dando oportunidad análoga, entiendo que a comprar futuros más baratos, o a vender spot más caro.
     - Las alarmas que hice en el "compare_rates" de la clase "TaskHandler" son para dos casos específicos (si bien como describí más arriba veo que hay un espectro más amplio de posibilidades). Hago alusión a las líneas de código:
     
        """
           if new_value < self.implicit_rate_value:
               self.buying_opportunity_alarm(new_value=new_value)
           elif self.implicit_rate_value < new_value:      
               self.selling_opportunity_alarm(new_value=new_value)
        """
        
       1) En caso que la tasa aumente, aviso de una oportunidad de venta , la oportunidad de venta sería para el caso de poder vender un futuro más caro.
       2) En caso que la tasa disminuya, aviso de oportunidad de compra, la oportunidad de compra sería para el caso de poder comprar un futuro más barato.
       
