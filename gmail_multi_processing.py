''' Automation using multi-processing '''

import cProfile
from configparser import ConfigParser
from multiprocessing import Process
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def automate(mail, passwd, index):
    ''' Method to provide automation '''
    driver = webdriver.Chrome()
    driver.get("http://gmail.com")
    try:
        eid = WebDriverWait(driver, 150).until(
            EC.visibility_of_element_located((By.NAME, 'identifier'))
        )
        eid.send_keys(mail)
        #driver.find_element_by_name("identifier").send_keys(mail)
        driver.find_element_by_xpath("//*[@id='identifierNext']/span/span").click()
        #driver.implicitly_wait(20)
        passd = WebDriverWait(driver, 150).until(
            EC.visibility_of_element_located((By.NAME, 'password'))
        )
        passd.send_keys(passwd)
        #driver.find_element_by_name("password").send_keys(passwd)
        driver.find_element_by_xpath("//*[@id='passwordNext']/span/span").click()
        #driver.implicitly_wait(30)
        emails = WebDriverWait(driver, 150).until(
            EC.visibility_of_all_elements_located((By.CLASS_NAME, 'zA'))
        )
        #emails = driver.find_elements_by_class_name('zA')
        emails[index].click()
        body = WebDriverWait(driver, 150).until(
            EC.visibility_of_element_located((By.CLASS_NAME, 'a3s'))
        )
        content = body.text
        #body = driver.find_element_by_class_name('a3s').text
        fname = 'body' + str(index + 1) + '.txt'
        with open(fname, 'w') as wfile:
            wfile.write(content)
    except NoSuchElementException as nsee:
        print(index+1, 'Element not found', nsee)
    except IndexError:
        print(index+1, 'Index out of range')
    except TimeoutException as toe:
        print(index+1, 'Command not completed in time', toe)
    except ElementClickInterceptedException as ecie:
        print(index+1, 'Click command not completed', ecie)
    except WebDriverException as wde:
        print(index+1, 'chrome not reachable', wde)

    driver.close()


if __name__ == "__main__":
    config = ConfigParser()
    config.read('config.ini')

    # Fetching credentials from config.ini
    email = config.get('auth', 'email')
    password = config.get('auth', 'password')

    # Creating processes
    p1 = Process(target=automate, args=(email, password, 0, ))
    p2 = Process(target=automate, args=(email, password, 1, ))
    p3 = Process(target=automate, args=(email, password, 2, ))
    p4 = Process(target=automate, args=(email, password, 3, ))
    p5 = Process(target=automate, args=(email, password, 4, ))
    p6 = Process(target=automate, args=(email, password, 5, ))
    p7 = Process(target=automate, args=(email, password, 6, ))
    p8 = Process(target=automate, args=(email, password, 7, ))
    p9 = Process(target=automate, args=(email, password, 8, ))
    p10 = Process(target=automate, args=(email, password, 9, ))

    cProfile.run('p1.start()')
    #p1.join()

    cProfile.run('p2.start()')
    #p2.join()

    cProfile.run('p3.start()')
    #p3.join()

    cProfile.run('p4.start()')
    #p4.join()

    cProfile.run('p5.start()')
    #p5.join()

    cProfile.run('p6.start()')
    #p6.join()

    cProfile.run('p7.start()')
    #p7.join()

    cProfile.run('p8.start()')
    #p8.join()

    cProfile.run('p9.start()')
    #p9.join()

    cProfile.run('p10.start()')
    #p10.join()
