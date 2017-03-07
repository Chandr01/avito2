
from selenium import webdriver
from time import sleep
from PIL import Image
from pytesseract import image_to_string


class Bot:

    def tel_recon(self):
        image = Image.open('tel.gif')
        print(image_to_string(image))

    def __init__(self):
        self.driver = webdriver.Firefox(executable_path = 'C:\\Users\\sep\\Downloads\\geckodriver.exe')
        self.navigate()

    def take_scrinshot(self):
        self.driver.save_screenshot('avito_scs.png')
    def crop(self, location, size):
        image = Image.open('avito_scs.png')
        x = location['x']
        y = location['y']
        widh = size['width']
        heigt = size['height']

        image.crop((x, y, x+widh, y+heigt)).save('tel.gif')

        self.tel_recon()


    def navigate(self):
        self.driver.get('https://www.avito.ru/moskva/telefony/novye_xiaomi_redmi_note_4x_i_note_4_vo_vseh_tsvetah_922189984')
        button = self.driver.find_element_by_xpath('//button[@class="button item-phone-button js-item-phone-button button-origin button-origin-blue button-origin_full-width button-origin_large-extra item-phone-button_hide-phone item-phone-button_card js-item-phone-button_card"]')
        button.click()
        sleep(3)
        self.take_scrinshot()
        image = self.driver.find_element_by_xpath('//div[@class="item-phone-big-number js-item-phone-big-number"]//*')
        location = image.location
        size = image.size
        self.crop(location, size)



b = Bot()
#def main():
#    b = Bot()

#if __name__() == '__main__':
#    main()







