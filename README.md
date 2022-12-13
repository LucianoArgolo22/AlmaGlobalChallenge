# AlmaGlobalChallenge
Desafío/Ejercicio Técnico para entrevista alma global

El programa Main corre por dentro el Client Logger para generar un log de lo que ocurre y tener
trazabilidad.

por otro lado Genera dos objetos con el service Ticker Rates para poder hacer por un lado:
 - con la config2.json obtener por única vez las tasas implícitas
 - con la config.json obtener continuamente la tasa implícita para detectar una variación de la misma y ver si puede existir una oportunidad de arbitraje.

El ServiceTickerRates por dentro funciona con las clases:
 - FinanceValues, que obtiene mediante pyrofex y yfinance todos los valores financieros necesarios
 - Metrics, que recibe por parámetro un objeto del tipo FinanceValues y genera la tasa implícita con la información dentro del objeto FinanceValues
 - TaskHandler, que se encarga de ser el pasamanos que recibe una y otra vez las nuevas tasas implícitas que obtiene cada objeto, de ésta manera generando una comparación entre tasas y viendo si se rompe la correlación, favoreciendo alguna oportunidad de arbitraje.