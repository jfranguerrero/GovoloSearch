# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import selenium.webdriver.support.expected_conditions as EC
import time
from calendar import monthrange
import sys


if(len(sys.argv)!=5):
    print ("Error de parámetros. Ejemplo: python govolosearch.py AGP BCN 9 2018")
else:

    chromeOptions = webdriver.ChromeOptions()

    prefs = {"profile.managed_default_content_settings.images": 2}
    chromeOptions.add_experimental_option("prefs", prefs)
    chromeOptions.add_argument('--headless')

    driver = webdriver.Chrome(chrome_options=chromeOptions)
    origen=sys.argv[1]
    destino=sys.argv[2]
    mes=sys.argv[3]
    year=sys.argv[4]
    dias_mes=monthrange(int(year), int(mes))

    print ('Origen: '+origen+' -----------> Destino: '+destino)

    i=1

    while i<=dias_mes[1]:
        date=str("{0:0=2d}".format(i))+'/'+str("{0:0=2d}".format(int(mes)))+'/'+year

        driver.get('https://booking.govolo.es/motor/vuelo_espera_1.html?typ=flight&vil_dep='+origen+
        '&vil_arr='+destino+'&dte_dep='+str("{0:0=2d}".format(i))+str("{0:0=2d}".format(int(mes)))+'18&all_ret=non')

        wait = WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.ID, "div_flightPriceMinB")))

        precio = driver.find_element_by_id("div_flightPriceMinB")

        print (date+' = '+precio.text)
        i=i+1

    driver.quit()