import selenium
from selenium import webdriver
import pyautogui
from selenium.webdriver.common.by import By
import time
import PIL.ImageGrab


f = open('information.txt','r')
j=0
info = ["",""]
for i in f:
    split_i = i.split(":")
    split_split_i = split_i[1].split("\n")
    info[j] = split_split_i[0]

    j=j+1


f.close()
    
def codetantra():
    driver = webdriver.Chrome()

    driver.get('https://fkshyderabad.codetantra.com/secure/tla/m.jsp')

    email_box = driver.find_element_by_name('loginId')
    email_box.send_keys(info[0])

    password_box = driver.find_element_by_name('password')
    password_box.send_keys(info[1])

    login_button = driver.find_element_by_id('loginBtn')
    login_button.click()

    #broken
    #change_view = driver.find_element_by_name("button.fc-listView-button.fc-button.fc-button-primary")
    #change_view.click()
    #class_button_chem = element = driver.find_element_by_partial_link_text('"Grade 12"').click()
    #class_button_chem.click()
    #broken

    (x,y)= pyautogui.size()
    s=x/2
    t=y/2
    pyautogui.moveTo(s,t)
    #screensizetheirs/screensizemine = r modify


    #1 Original
    #pyautogui.moveTo(s-300,t+400)
    
    #(x1,y1) = pyautogui.position()
    #urltimetable = driver.current_url
    #while (driver.current_url == urltimetable):
        #pyautogui.click(x1,y1-100)
        #y1=y1-10
    #put an error sheet here
                   
        
    #1 Bandage code
    time.sleep(3)

    #2 
    urljoinpage = driver.current_url
    pyautogui.click(s-550,t-325)
    if(driver.current_url == urljoinpage):
        print("end script")
        return 1
    

    time.sleep(5.5)
    #3 and 5
    pyautogui.click(s-575,t+40)

    time.sleep(1)
    #4
    pyautogui.click(s-645,t-345)

    px2 = PIL.ImageGrab.grab().load()
    rgb=px2[s-575,t+40]

    hexrgb = '#{:02x}{:02x}{:02x}'.format( rgb[0], rgb[1] , rgb[2] )

    #3 and 5
    while(hexrgb != "#008081"):
        px2 = PIL.ImageGrab.grab().load()
        rgb=px2[s-575,t+40]
        hexrgb = '#{:02x}{:02x}{:02x}'.format( rgb[0], rgb[1] , rgb[2] )
    else:
        pyautogui.click(s-575,t+40)

codetantra()

