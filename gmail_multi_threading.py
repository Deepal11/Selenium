''' Automation using multi-threading '''

import cProfile
import threading
from configparser import ConfigParser
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MyThread(threading.Thread):
    ''' Thread class '''
    config = ConfigParser()
    config.read('config.ini')

    # Fetching credentials from config.ini
    email = config.get('auth', 'email')
    password = config.get('auth', 'password')

    def __init__(self, index):
        threading.Thread.__init__(self)
        self.index = index
    def run(self):
        automate(MyThread.email, MyThread.password, self.index)

def automate(email, password, index):
    ''' Method to provide automation '''
    driver = webdriver.Chrome()
    driver.get("http://gmail.com")
    try:
        eid = WebDriverWait(driver, 150).until(
            EC.visibility_of_element_located((By.NAME, 'identifier'))
        )
        eid.send_keys(email)
        driver.find_element_by_xpath("//*[@id='identifierNext']/span/span").click()
        passd = WebDriverWait(driver, 150).until(
            EC.visibility_of_element_located((By.NAME, 'password'))
        )
        passd.send_keys(password)
        driver.find_element_by_xpath("//*[@id='passwordNext']/span/span").click()
        emails = WebDriverWait(driver, 150).until(
            EC.visibility_of_all_elements_located((By.CLASS_NAME, 'zA'))
        )
        emails[index].click()
        content = WebDriverWait(driver, 150).until(
            EC.visibility_of_element_located((By.CLASS_NAME, 'a3s'))
        )
        body = content.text
        fname = 'body' + str(index + 1) + '.txt'
        with open(fname, 'w') as wfile:
            wfile.write(body)
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
    # Creating threads
    t1 = MyThread(0)
    t2 = MyThread(1)
    t3 = MyThread(2)
    t4 = MyThread(3)
    t5 = MyThread(4)
    t6 = MyThread(5)
    t7 = MyThread(6)
    t8 = MyThread(7)
    t9 = MyThread(8)
    t10 = MyThread(9)

    # Starting threads
    cProfile.run('t1.start()')
    cProfile.run('t2.start()')
    cProfile.run('t3.start()')
    cProfile.run('t4.start()')
    cProfile.run('t5.start()')
    cProfile.run('t6.start()')
    cProfile.run('t7.start()')
    cProfile.run('t8.start()')
    cProfile.run('t9.start()')
    cProfile.run('t10.start()')
