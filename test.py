import datetime
import time
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import helpers
from datetime import datetime

def typegm():
    options = webdriver.ChromeOptions()

    w = webdriver.Chrome(executable_path="C:\\Users\\chromedriver.exe", chrome_options=options)

    w.get("https://discord.com/channels/@me")

    email_input = w.find_element_by_name("email")
    email_input.clear()
    email_input.send_keys("test@test.com")

    pass_input = w.find_element_by_name("password")
    pass_input.send_keys("test")
    pass_input.send_keys(Keys.ENTER)
    time.sleep(5)

    print('Находим 1-ую по счету папку с нужным сервером')
    w.find_elements_by_class_name('folderIconWrapper-1oRIZr')[0].click()
    time.sleep(5)
    print('Заходим на сервер')

    w.find_element_by_xpath("//div[@data-list-item-id='guildsnav___933846070344167464']").click()

    time.sleep(15)
    print('Заходим в чат gm-gn')
    w.find_element_by_xpath("//*[contains(text(), 'gm-gn')]").click()
    time.sleep(5)
    print('Пишем сообщение')
    current_time = datetime.now().strftime("%H:%M:%S")

    if current_time > helpers.deadline_gm:
        w.find_element_by_xpath(
            "//div[@class='markup-eYLPri editor-H2NA06 slateTextArea-27tjG0 fontSize16Padding-XoMpjI']").send_keys(
            helpers.gm + Keys.ENTER)
    else:
        w.find_element_by_xpath(
            "//div[@class='markup-eYLPri editor-H2NA06 slateTextArea-27tjG0 fontSize16Padding-XoMpjI']").send_keys(
            helpers.gn + Keys.ENTER)

    time.sleep(5)


if __name__ == '__main__':
    typegm()
