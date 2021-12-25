from typing import KeysView
from selenium.webdriver.common import by
from selenium.webdriver.support import expected_conditions, ui
from selenium.webdriver.support.wait import WebDriverWait


def solve_recaptcha():
    import speech_recognition as sr
    import ffmpy, urllib, pydub
    import os
    from selenium import webdriver
    driver=webdriver.Chrome()
    from selenium.webdriver.common import by
    from selenium.webdriver.support import ui 
    from selenium.webdriver.support import expected_conditions

    
    frame_select('recaptcha-audio-button')
    frame_select('PLAY')

    audio_path_mp3 = os.path.join('sample.mp3')
    audio_path_wav = os.path.join('sample.wav')

    frame_select('audio-source','attrib','src')
    print('[INFO] Audio src:',src)
    urllib.request.urlretrieve(src,audio_path_mp3)

    sound = pydub.AudioSegment.from_mp3(audio_path_mp3)
    sound.export(audio_path_wav,format='wav')
    sample_audio = sr.AudioFile(audio_path_wav)
    print('[+] Audio Saved')

    r = sr.Recognizer()
    with sample_audio as source:
        audio = r.record(source)
    key = r.recognize_google(audio)
    print('[INFO] Recaptcha Passcode:',key)

    frame_select('audio-response','key',key)
    frame_select('recaptcha-verify-button')
    print('[+] Passcode Sent')
    driver.close()

def recaptcha_check(check):
    waiting = WebDriverWait(ui,1)
    try:
        for frame in ui.find_elements_by_tag_name('iframe'):
            ui.switch_to.default_content()
            ui.switch_to.frame(frame)
            for x in ['@class=','@id=','@name=','@for=','text()=']:
                try: waiting.until(expected_conditions.presence_of_element_located((by.XPATH,f"//*[{x}'{check}']")))
                except: continue
                else: return True
    except: return False


def frame_select(selector, action='click', file=''):

    find_elem(selector,action,file)

    if not element:
        for frame in ui.find_elements_by_tag_name('iframe'):
            ui.switch_to.default_content()
            ui.switch_to.frame(frame)
            print('[*] Trying Next Frame:', selector)
            
            find_elem(selector,action,file)

            ui.switch_to.default_content()
            if element: break


def find_elem(selector,action='click',file=''):
        global element, src
        element = False
        for x in ['@id=','@name=','@for=','@class=','text()=']:
            try:
                print(f"\033[90m [*] //*[{x}'{selector}'] \033[0m")
                if action == 'click': 
                    ui.find_element_by_xpath(f"//*[{x}'{selector}']").click()
                    print('\033[32m [+] Click: \033[0m', selector)
                elif action == 'key':
                    ui.find_element_by_xpath(f"//*[{x}'{selector}']").send_keys(file,KeysView.RETURN)
                    print('\033[32m [+] Return: \033[0m', selector)
                elif action == 'attrib':
                    src = ui.find_element_by_xpath(f"//*[{x}'{selector}']").get_attribute(file)
                    print('\033[32m [+] Get Attribute: \033[0m', selector, file)
                element = True
                break
            except: continue