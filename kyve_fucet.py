import time
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import helpers

def faucet_send():
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
    w.find_elements_by_class_name('folderIconWrapper-1oRIZr')[1].click()
    time.sleep(5)
    print('Заходим на сервер')

    w.find_element_by_xpath("//div[@data-list-item-id='guildsnav___817113909957361664']").click()

    time.sleep(5)
    print('Заходим в чат gm-gn')
    #w.find_element_by_class_name('name-28HaxV overflow-1wOqNV').find_elements_by_class_name('channelName-3KPsGw').click()
    w.find_element_by_xpath("//*[contains(text(), '🚰┊faucet')]").click()
    time.sleep(5)
    print('Пишем сообщение')

    w.find_element_by_xpath("//div[@class='markup-eYLPri editor-H2NA06 slateTextArea-27tjG0 fontSize16Padding-XoMpjI']").send_keys(helpers.kyveFaucet + Keys.ENTER)

    time.sleep(5)


if __name__ == '__main__':
    faucet_send()
