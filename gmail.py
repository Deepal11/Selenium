from selenium import webdriver
driver = webdriver.Chrome()
driver.get("http://gmail.com")
driver.find_element_by_name("identifier").send_keys('deepaljain11@gmail.com')
driver.find_element_by_xpath("//*[@id='identifierNext']/span/span").click()
driver.implicitly_wait(10)
driver.find_element_by_name("password").send_keys('Deepal_123')
driver.find_element_by_xpath("//*[@id='passwordNext']/span/span").click()
driver.implicitly_wait(10)
emails = driver.find_elements_by_class_name('zA')
if len(emails)>1:
    emails[1].click()
    body = driver.find_element_by_class_name('a3s').text
    with open('body.txt','w') as w:
        w.write(body)
driver.close()