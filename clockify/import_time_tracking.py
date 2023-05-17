import pyautogui
from helpers.utils import open_browser
from helpers.utils import loading_screen
import pandas as pd
from helpers.utils import get_login_clockify


#ABIR SITE DO CLOCKIFY
def access_browser_clockify():
    open_browser('https://clockify.me/')


#FAZER LOGIN
def do_login_clockify():
    pyautogui.sleep(2)
    pyautogui.press('tab', presses=4)
    pyautogui.press('enter')
    loading_screen('clockify_login')
    button_location = pyautogui.locateOnScreen('images/login_google_clockify.png', confidence=0.80)
    if button_location:
        pyautogui.sleep(2)
        button_location_center = pyautogui.center(button_location)
        pyautogui.click(button_location_center.x, button_location_center.y)
        pyautogui.sleep(1.5)
        loading_screen('another_google_account_clockify')
        button_another_account = pyautogui.locateOnScreen('images/another_google_account_clockify.png', confidence=0.80)
        button_another_account_center = pyautogui.center(button_another_account)
        pyautogui.click(button_another_account_center.x, button_another_account_center.y)
        pyautogui.sleep(1)
        pyautogui.keyDown('ctrl')
        pyautogui.press('a')
        pyautogui.keyUp('ctrl')
        get_login_clockify()


#LER EXCEL
def read_clockify_database():
    loading_screen('clockify_work_page')
    # Necessário inserir tratamento de erro (demora do site após login em casos eventuais)
    # Necessário verificar se está em timer(n) ou manual(m) antes do inicio das próximas ações e seguir de acordo
    data_table = pd.read_excel('clockify/clockify_database.xlsx')
    day = data_table['DIA']
    description = data_table['DESCRIÇÃO']
    project = data_table['PROJETO']
    tag = data_table['TAGS']
    start_time = data_table['HORA INICIO']
    start_time = pd.to_datetime(start_time, format='%H:%M:%S').dt.strftime('%H%M')
    end_time = data_table['HORA FIM']
    end_time = pd.to_datetime(end_time, format='%H:%M:%S').dt.strftime('%H%M')
# IMPORTAR CADA LINHA UTILIZANDO A LÓGICA DOS TABS
    for day, description, project, tag, start_time, end_time in zip(day, description, project, tag, start_time, end_time):
        pyautogui.sleep(1.5)
        pyautogui.typewrite(description)
        pyautogui.sleep(1)
        click_project = pyautogui.locateOnScreen('images/clockify_project.png', confidence=0.80)
        click_project_center = pyautogui.center(click_project)
        pyautogui.click(click_project_center.x, click_project_center.y)
        pyautogui.sleep(1)
        pyautogui.typewrite(project)
        pyautogui.sleep(1)
        pyautogui.press('enter')
        pyautogui.sleep(1)
        pyautogui.press('tab')
        pyautogui.typewrite(tag)
        pyautogui.sleep(1)
        tag_click = pyautogui.locateOnScreen('images/clockify_select_tag.png', confidence=0.75)
        tag_click_center = pyautogui.center(tag_click)
        pyautogui.click(tag_click_center.x, tag_click_center.y)
        pyautogui.sleep(1)
        pyautogui.press('tab', presses=2)
        pyautogui.typewrite(start_time)
        pyautogui.press('tab')
        pyautogui.typewrite(end_time)
        pyautogui.press('tab', presses=3)
        pyautogui.typewrite(day.strftime('%d/%m/%Y'))
        click_add = pyautogui.locateOnScreen('images/clockify_add.png', confidence=0.80)
        pyautogui.click(click_add)


def run():
    access_browser_clockify()
    do_login_clockify()
    read_clockify_database()
