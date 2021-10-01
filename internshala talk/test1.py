
from selenium import webdriver
# import pyperclip
# import names
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import random
# import datetime
import pandas as pd


#61


driver = webdriver.Chrome(executable_path='/Users/HP/Desktop/folders/others/chromedriver/chromedriver.exe')

csv = pd.read_csv('csv.csv')
csv = csv.values.tolist()
csv.pop(0)
csv.pop(0)

total = 61

names = '''Abhishek tadkod
akshay r
ashwini panikatti
ashwin g
cheryl d
daneshwar r
digambar tadwad
digambar v
faisal khan'''.split('\n')


fix = len(names)

range_ = total - fix

start = 61
end = 61 + range_
newcsv = csv[start : end]   



for i in newcsv:
    names.append(i[1])

id = []
for i in names:
    name = i.lower().split()
    mid = name[0] + name[1] + str(random.choice(['',random.randint(589,9999)])) + '@gmail.com'
    if random.randint(0,1) == 1:
        id.append([name[0].title(),name[1].title(),mid,random.randint(9000000000,9999999999)])
    else:
        id.append([name[0],name[1],mid,random.randint(9000000000,9999999999)])


random.shuffle(id)

count = 0

print(f'total number of participants are {len(id)}')

if len(id) != total:
    print('Number of participants are not equall')
    exit()

import random

for i in id:

    url_att = 'https://internshala.com/i/TA-ISP20DHUR9620'

    driver.get(url_att)

    email = '#seminar-attendance-form > div:nth-child(1) > input'

    driver.find_element_by_css_selector(email).send_keys(i[2])

    fname = '#first_name'

    driver.find_element_by_css_selector(fname).send_keys(i[0])

    lname = '#last_name'

    driver.find_element_by_css_selector(lname).send_keys(i[1])

    mob = '#seminar-attendance-form > div:nth-child(3) > input'

    driver.find_element_by_css_selector(mob).send_keys(i[3])

    check = '#to_register'

    if count % 5 == 0:

        driver.find_element_by_css_selector(check).click()
    # break

    submit = '#seminar-attendance-form > div:nth-child(5) > button'

    driver.find_element_by_css_selector(submit).click()

    count += 1
    print(count,end = ' : ')
    print(i[2])
    time.sleep(1)






# no = int(input())


    # url = 'https://docs.google.com/forms/d/e/1FAIpQLSd230A0uGQ9mRZ-RBbXavLmLLPzRL7cdtiUPjhpoM7JyeZisw/viewform'
            

    # driver.get(url)


    # rating = '#mG61Hd > div.freebirdFormviewerViewFormCard.exportFormCard > div > div.freebirdFormviewerViewItemList > div:nth-child(1) > div > div > div.freebirdFormviewerComponentsQuestionScaleRoot > div > span > div > label:nth-child(6) > div.freebirdMaterialScalecontentInput > div > div > div.appsMaterialWizToggleRadiogroupRadioButtonContainer'

    # driver.find_element_by_css_selector(rating).click()

    # list1 = ['fabulous',
    #         'great talk',
    #         'usefull',
    #         'awesome broo',
    #         'lit talk thank you',
    #         'good ',
    #         'good content',
    #         'thanks for showing us',
    #         'internshala is awesome',
    #         'yes he was awesome',
    #         'great video',
    #         'great talk',
    #         'great',
    #         'better than others',
    #         'thnks brother',
    #         'good webnar',
    #         'good content',
    #         'crazy bro',
    #         'thanks man',
    #         'internshala is great ',
    #         'dude it was awesome',
    #         'you are too good bro and thanks for sharing',
    #         'very good',
    #         'usefull',
    #         'usefull content and it was good',
    #         'very good',
    #         'awesome video and content',
    #         'it was interactive',
    #         'not boring',
    #         'good',
    #         'he was good',
    #         'crazy webinar bro thanks ',
    #         'cool website and awesome content',
    #         'great internships',
    #         'No',
    #         'He was good',
    #         'excellent',
    #         'good',
    #         'awesome',
    #         'good content',
    #         'Good',
    #         'fab',
    #         'He was too good',
    #         'session was very good',
    #         'very usefull',
    #         'usefull',
    #         'good webinar',
    #         'good talk',
    #         'excellent talk',
    #         'you are awesome bro']

    # input1 = '#mG61Hd > div.freebirdFormviewerViewFormCard.exportFormCard > div > div.freebirdFormviewerViewItemList > div:nth-child(2) > div > div > div.freebirdFormviewerComponentsQuestionTextRoot > div > div.quantumWizTextinputPaperinputMainContent.exportContent > div > div.quantumWizTextinputPaperinputInputArea > input'

    # driver.find_element_by_css_selector(input1).send_keys(list1[random.randint(0,len(list1)-1)])
    # # print(list1[random.randint(0,len(list1))])

    # date = '#mG61Hd > div.freebirdFormviewerViewFormCard.exportFormCard > div > div.freebirdFormviewerViewItemList > div:nth-child(3) > div > div > div:nth-child(2) > div > div > div.quantumWizTextinputPaperinputEl.freebirdThemedInput.freebirdFormviewerComponentsQuestionDateDateInput.modeLight > div.quantumWizTextinputPaperinputMainContent.exportContent > div > div.quantumWizTextinputPaperinputInputArea > input'
    # driver.find_element_by_css_selector(date).send_keys('29-07-2020')

    # mail = '#mG61Hd > div.freebirdFormviewerViewFormCard.exportFormCard > div > div.freebirdFormviewerViewItemList > div:nth-child(4) > div > div > div.freebirdFormviewerComponentsQuestionTextRoot > div > div.quantumWizTextinputPaperinputMainContent.exportContent > div > div.quantumWizTextinputPaperinputInputArea > input'
    # driver.find_element_by_css_selector(mail).send_keys(i[2])

    # submit = '#mG61Hd > div.freebirdFormviewerViewFormCard.exportFormCard > div > div.freebirdFormviewerViewNavigationNavControls > div.freebirdFormviewerViewNavigationButtonsAndProgress > div > div > span > span'
    # # driver.find_element_by_css_selector(submit).click()

    # count += 1

    # print(str(count) + '   ' + i[2])
    

    # id.pop(0)
