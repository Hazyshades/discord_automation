import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys


# options = webdriver.ChromeOptions()
from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument("user-agent=Hello") #Path to your chrome profile

w = webdriver.Chrome(executable_path="C:\\Users\\chromedriver.exe", chrome_options=options)

w.get("https://discord.com/channels/@me")

email_input = w.find_element_by_name("email")
email_input.clear()
email_input.send_keys("test@mail.com")

pass_input = w.find_element_by_name("password")
pass_input.send_keys("test")
pass_input.send_keys(Keys.ENTER)
time.sleep(5)

w.find_element_by_css_selector('#app-mount > div.app-3xd6d0 > div > div.layers-OrUESM.layers-1YQhyW > div > div.container-1eFtFS > nav > ul > div.scroller-3X7KbA.none-2-_0dP.scrollerBase-_bVAAt > div:nth-child(3) > div:nth-child(2) > div:nth-child(2) > div > div > svg > foreignObject > div').click()
time.sleep(5)
w.find_element_by_css_selector('#channels > ul > li:nth-child(19) > div > div.content-1gYQeQ > a > div.name-28HaxV.overflow-1wOqNV > div').click()
time.sleep(5)
pass_input2= w.find_element_by_css_selector('#app-mount > div.app-3xd6d0 > div > div.layers-OrUESM.layers-1YQhyW > div > div.container-1eFtFS > div > div > div.chat-2ZfjoI > div > main > form > div > div > div > div.scrollableContainer-15eg7h > div > div.textArea-2CLwUE.textAreaSlate-9-y-k2.slateContainer-3x9zil > div > div.markup-eYLPri.editor-H2NA06.slateTextArea-27tjG0.fontSize16Padding-XoMpjI > div')
pass_input2.send_keys("gn")
pass_input2.send_keys(Keys.ENTER)