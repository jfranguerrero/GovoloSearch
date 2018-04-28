# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.firefox.options import Options
from calendar import monthrange
import sys


if(len(sys.argv)!=5):
    print "Error de parámetros. Ejemplo: python govolosearch.py AGP BCN 9 2018"
else:

    options = Options()
    options.add_argument("--headless")
    driver = webdriver.Firefox(firefox_options=options)
    origen=sys.argv[1]
    destino=sys.argv[2]
    mes=sys.argv[3]
    year=sys.argv[4]
    dias_mes=monthrange(int(year), int(mes))

    print 'Origen: '+origen+' -----------> Destino: '+destino

    i=1

    while i<=dias_mes[1]:
        date=str("{0:0=2d}".format(i))+'/'+str("{0:0=2d}".format(int(mes)))+'/'+year

        driver.get('https://booking.govolo.es/motor/vuelo_error_dispo.html')

        driver.find_element_by_id("m_cphMain_m_ctrlFlightSearchMini_m_rbtSingleTrip").click()
        ida = driver.find_element_by_id("m_cphMain_m_ctrlFlightSearchMini_m_txtDepart")
        ida.clear()
        ida.send_keys(origen)

        vuelta = driver.find_element_by_id("m_cphMain_m_ctrlFlightSearchMini_m_txtDest")
        vuelta.clear()
        vuelta.send_keys(destino)

        fecha = driver.find_element_by_id("m_cphMain_m_ctrlFlightSearchMini_m_txtDateDep")
        fecha.clear()
        fecha.send_keys(date)

        driver.find_element_by_id("m_cphMain_m_ctrlFlightSearchMini_m_btnSearch").click()

        wait = WebDriverWait(driver, 30)
        wait.until(lambda driver: "vuelo_resultado_2.html" in driver.current_url)
        time.sleep(2)

        precio = driver.find_element_by_id("valueAA")

        options = [x for x in precio.find_elements_by_tag_name("option")] 

        print date+' = '+str(options[0].get_attribute("value"))[:-2]+','+str(options[0].get_attribute("value"))[-2:]+'€'
        i=i+1   
