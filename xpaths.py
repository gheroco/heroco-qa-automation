from strenum import StrEnum

#Following class contains xpath locators to be used in all tabs of the webpage

class Xpaths(StrEnum):
    # Heroco home page
    apply_now = '//*[@id="__next"]/main/div/div[1]/section/div[1]/a'
    heroco_logo = '//*[@id="__next"]/main/nav/div/a/img'
    
    # Apply Now page
    name = '//*[@id="__next"]/main/div/div[2]/section/div[1]/div[2]/form/label[1]/input'
    email = '//*[@id="__next"]/main/div/div[2]/section/div[1]/div[2]/form/label[2]/input'
    phone = '//*[@id="__next"]/main/div/div[2]/section/div[1]/div[2]/form/label[3]/input'
    career = '//*[@id="select-course-"]/div/div[1]/div[2]'
    career_value = '//*[@id="react-select-select-course--listbox"]'
    connect_button = '//*[@id="__next"]/main/div/div[2]/section/div[1]/div[2]/form/button'

    # Career Paths page
    front_end = '//*[@id="__next"]/main/div/section[1]/div[2]/div[1]/a/div/div/div/p[1]'
    back_end = '//*[@id="__next"]/main/div/section[1]/div[2]/div[2]/a/div/div/div/p[1]'
    devops = '//*[@id="__next"]/main/div/section[1]/div[2]/div[3]/a/div/div/div/p[1]'
    data_science = '//*[@id="__next"]/main/div/section[1]/div[2]/div[4]/a/div/div/div/p[1]'
    android = '//*[@id="__next"]/main/div/section[1]/div[2]/div[5]/a/div/div/div/p[1]'
