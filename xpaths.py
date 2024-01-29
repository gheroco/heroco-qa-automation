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

    # Courses page
    html_css = '//*[@id="__next"]/main/div/section[2]/div[2]/div[1]/div[1]/a'
    javascript = '//*[@id="__next"]/main/div/section[2]/div[2]/div[1]/div[2]/a'
    reactjs = '//*[@id="__next"]/main/div/section[2]/div[2]/div[1]/div[3]/a'
    nodejs = '//*[@id="__next"]/main/div/section[2]/div[2]/div[1]/div[4]/a'
    androidcourse = '//*[@id="__next"]/main/div/section[2]/div[2]/div[1]/div[5]/a'
    kotlin = '//*[@id="__next"]/main/div/section[2]/div[2]/div[1]/div[6]/a'
    expand_button = '//*[@id="__next"]/main/div/section[2]/div[2]/div[2]/button'
    java = '//*[@id="__next"]/main/div/section[2]/div[2]/div[1]/div[7]/a'
    algorithms_and_ds = '//*[@id="__next"]/main/div/section[2]/div[2]/div[1]/div[8]/a'
    computer_science = '//*[@id="__next"]/main/div/section[2]/div[2]/div[1]/div[9]/a'
    machine_learning = '//*[@id="__next"]/main/div/section[2]/div[2]/div[1]/div[10]/a'
    databases = '//*[@id="__next"]/main/div/section[2]/div[2]/div[1]/div[11]/a'
    devops_course = '//*[@id="__next"]/main/div/section[2]/div[2]/div[1]/div[12]/a'
    python = '//*[@id="__next"]/main/div/section[2]/div[2]/div[1]/div[13]/a'
    manual_qa = '//*[@id="__next"]/main/div/section[2]/div[2]/div[1]/div[14]/a'

    #About page
    karo = '//*[@id="__next"]/main/div/section[3]/div[2]/div[1]/div/div/a/img'
    smbat = '//*[@id="__next"]/main/div/section[3]/div[2]/div[2]/div/div/a/img'
    vahe = '//*[@id="__next"]/main/div/section[3]/div[2]/div[3]/div/div/a/img'
    georgi = '//*[@id="__next"]/main/div/section[3]/div[2]/div[4]/div/div/a/img'
    vardges = '//*[@id="__next"]/main/div/section[3]/div[2]/div[5]/div/div/a/img'