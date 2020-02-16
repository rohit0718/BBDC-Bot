from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome('insert_path_to_chromedriver_here')

username = 'insert_your_username_here'
password = 'insert_your_password_here'

browser.get('https://info.bbdc.sg/members-login/')
idLogin = browser.find_element_by_id('txtNRIC')
idLogin.send_keys(username)
idLogin = browser.find_element_by_id('txtPassword')
idLogin.send_keys(password)
loginButton = browser.find_element_by_name('btnLogin')
loginButton.click()

# Switching to Left Frame and accessing element by text
browser.switch_to.default_content()
frame = browser.find_element_by_name('leftFrame')
browser.switch_to.frame(frame)
nonFixedInstructor = browser.find_element_by_link_text('Booking without Fixed Instructor')
nonFixedInstructor.click()

# Switching back to Main Frame and pressing 'I Accept'
browser.switch_to.default_content()
wait = WebDriverWait(browser, 300)
wait.until(EC.frame_to_be_available_and_switch_to_it(browser.find_element_by_name('mainFrame')))
wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "btn"))).click()

# Selection menu
browser.switch_to.default_content()
wait = WebDriverWait(browser, 300)
wait.until(EC.frame_to_be_available_and_switch_to_it(browser.find_element_by_name('mainFrame')))
wait.until(EC.visibility_of_element_located((By.ID, "checkMonth")))

# 0 refers to first month, 1 refers to second month, and so on...
months = browser.find_elements_by_id('checkMonth')
months[12].click() # all months

# 0 refers to first session, 1 refers to second session, and so on...
sessions = browser.find_elements_by_id('checkSes')
sessions[8].click() # all sessions

# 0 refers to first day, 1 refers to second day, and so on...
days = browser.find_elements_by_id('checkDay')
days[7].click() # all days

# Selecting Search
browser.find_element_by_name('btnSearch').click()

# Dismissing Prompt
wait = WebDriverWait(browser, 300)
wait.until(EC.alert_is_present())
alert_obj = browser.switch_to.alert
alert_obj.accept()
wait.until(EC.visibility_of_element_located((By.NAME, "slot")))

# 0 refers to first slot, 1 refers to second slot, and so on...
slots = browser.find_elements_by_name('slot')
for slot in slots:     # Selecting all checkboxes
    slot.click()
    browser.find_element_by_class_name('pgtitle').click()     # clicking random element to hide hover effect

# Selecting Submit
browser.find_element_by_name('btnSubmit').click()

# Selecting confirm
wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@value='Confirm']")))
browser.find_element_by_xpath("//input[@value='Confirm']").click()

