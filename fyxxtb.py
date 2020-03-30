#防疫信息填报
#引入webdriver
from selenium import webdriver
#读取配置文件 模块
from configparser import ConfigParser
#实例化配置文件对象
target = ConfigParser()
target.read("config.txt",encoding='utf-8')
username = target.get('fangyi','username')
password = target.get('fangyi','password')
print("读取到的账号是:" + username + "读取到的密码是" + (password[0:2]) + "******" + (password[-2:]) )
driver = webdriver.Chrome()
#最大化浏览器
driver.maximize_window()
driver.get('https://wk.tiangong.edu.cn/app_xgc/work/tjpu/jkxxdj/jkxxdj.jsp')
driver.implicitly_wait(20)
driver.find_element_by_xpath('//*[@id="username"]').send_keys(username)
driver.find_element_by_xpath('//*[@id="password"]').send_keys(password)
driver.find_element_by_xpath('//*[@id="thetable"]/div[7]/span[1]/input[3]').click()
#获取数据
#print(driver.find_element_by_xpath('//*[@id="layui-layer1"]/div[2]').get_attribute("class"))
driver.implicitly_wait(20)
#driver.find_element_by_xpath('//*[@id="layui-layer1"]/div[3]/a').click()
#填写信息是否变化
sfbh = driver.find_element_by_class_name('layui-layer-content')
print("web回显信息：" + sfbh.text)
#未填写
if sfbh.text == '是否和昨天填报信息有变化？':
    print("参数正确，即将模拟点击")
    driver.implicitly_wait(10)
    driver.find_element_by_xpath('//*[@id="layui-layer2"]/div[3]/a[1]').click()
    driver.implicitly_wait(10)
    #是否提交
    sftj = driver.find_element_by_class_name('layui-layer-content layui-layer-padding')
    if sftj.text == '提交成功！':
        driver.implicitly_wait(10)
        driver.find_element_by_xpath('//*[@id="layui-layer3"]/div[3]/a').click()
        status = 1
    else:
        status = 0
elif sfbh.text == '请如实填报，如有隐瞒或虚报，后果自负！':
    driver.find_element_by_xpath('//*[@id="layui-layer1"]/div[3]/a').click()
    driver.find_element_by_xpath('//*[@id="post"]').click()
    status = 1
#已经填写过
elif sfbh.text == """您今天已填写过，当天只能修改一次，请谨慎修改！
请如实填报，如有隐瞒或虚报，后果自负！""":
    driver.implicitly_wait(5)
    driver.find_element_by_xpath('//*[@id="layui-layer1"]/div[3]/a').click()
    print("当日已经填写")
    status = 0
else:
    print("参数错误，请稍后重试")
    status = 0

#判断执行结果
if status == 1:
    print("执行成功")
elif status != 1:
    print("执行失败")
#关闭浏览器的tab
#driver.close()
print("浏览器tab已关闭")