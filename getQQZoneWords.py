from selenium import webdriver
import time
import random
import traceback


def convertCookies(cookie_before):
    cookiesS = []  # 初始化cookies字典变量

    for line in cookie_before.split(';'):  # 按照字符：进行划分读取
        # 其设置为1就会把字符串拆分成2份
        cookies = {'name': '', 'value': ''}
        cookies['name'], cookies['value'] = line.strip().split('=', 1)
        cookiesS.append(cookies)
    print(cookiesS)
    return cookiesS


def saveShuoShuo(bdelements):
    for i in bdelements:
        print(i.text)
        try:
            print(i.find_element_by_tag_name('a').get_attribute("data-uin"))
            assert i.find_element_by_tag_name('a').get_attribute("data-uin") != None
            if i.find_element_by_tag_name('pre').text != "":
                with open("D:\programming\sentence\\" + str(
                        i.find_element_by_tag_name('a').get_attribute("data-uin")) + '_' + str(
                    random.randrange(0, 999999999, 1)) + '.txt', 'w') as f:
                    f.write(i.find_element_by_tag_name('pre').text)
            print(str(i.find_element_by_tag_name('a').get_attribute("data-uin")) + ':' + i.find_element_by_tag_name(
                'pre').text)
        except:
            continue


chrome_opt = webdriver.ChromeOptions()
# 设置不加载图片
prefs = {"profile.managed_default_content_settings.images": 2}
chrome_opt.add_experimental_option("prefs", prefs)

# chrome_opt.add_argument('--headless')
# chrome_options.add_argument('--disable-gpu')
driver = webdriver.Chrome(chrome_options=chrome_opt, executable_path='C:\Windows\System32\chromedriver')


def login(driver, cookiesText):
    driver.get("https://user.qzone.qq.com/")
    time.sleep(5)
    cookies = convertCookies(cookiesText)
    for i in cookies:
        print(i)
        driver.add_cookie(i)
    # body = driver.find_element_by_id("QZ_Body")
    # login
    driver.switch_to_frame('login_frame')
    driver.find_element_by_xpath("//a[@uin='QQ']").click()  # please replace this
    driver.save_screenshot("D:\programming\qqZone\login.png")
    return driver


def getQQZone(qqNumber, driver):  # qqNumber is a String
    driver.get('https://user.qzone.qq.com/' + qqNumber)
    # goto shuoshuo page
    # driver.get('https://user.qzone.qq.com/191847115')
    time.sleep(30)
    driver.switch_to.default_content()
    driver.save_screenshot("D:\programming\qqZone\aftersth.png")
    print(driver.find_element_by_tag_name('body').text)
    print(driver.current_url)
    try:
        time.sleep(30)
        driver.find_element_by_xpath("//a[@accesskey='6']").click()
    except:
        try:
            driver.find_element_by_xpath("//a[@title='说说']").click()
        except:
            driver.switch_to.default_content()
            driver.find_element_by_xpath("//li[@class='menu_item_311']").click()

    time.sleep(30)
    driver.save_screenshot('D:\programming\qqZone\shuoshuo.png')

    # get pege number
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(10)
    driver.switch_to.default_content()
    driver.switch_to.frame("app_canvas_frame")
    pageText = driver.find_element_by_xpath('//a[@title="末页"]/span').text
    pageNumber = int(pageText)

    for number in range(pageNumber - 1):
        # driver.execute_script("""var jqry = document.createElement('script');jqry.src='https://code.jquery.com/jquery-3.3.1.js';var head = document.getElementsByTagName('head');head[0].appendChild(jqry);var page = $('[title="下一页"]');page.get(0).click()""")
        # find elements
        # driver.switch_to.frame(0)
        shuoshuoNeiRong = driver.find_elements_by_xpath("//div[@class='bd']")

        # save
        saveShuoShuo(shuoshuoNeiRong)
        driver.save_screenshot("D:\programming\qqZone\shuoshuo" + str(number + 1) + '.png')

        driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        time.sleep(10)
        # next page
        try:
            driver.find_element_by_xpath('//a[@title="下一页"]').click()
        except:
            print('\n\n\n\n\n\n\n\n\n\n\n\n\nn\n\n\n\n')
            print("bug")
            with open("D:\programming\mlwords\\bugs.txt", "w+") as f:
                f.write('\n\n\n\n')
                f.write(traceback.format_exc())
            continue
        time.sleep(40)


cookiesText = """  """
driver = login(driver, cookiesText)
time.sleep(30)

qqNumberList = [""]
for i in qqNumberList:
    getQQZone(i, driver)
