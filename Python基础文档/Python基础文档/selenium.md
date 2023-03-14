# selenium基础文档



## 反屏蔽



js检测原理

>   检测当前浏览器窗口下的**window.navigator**对象是否包含**webdriver**属性。正常情况访问 **window.navigator=undefind**
>
>   这类网站会直接屏蔽selenium的访问。

解决办法：可以使用<font color="red">CDP</font>来解决这个问题，通过CDP，我们可以实现在每个页面刚加载时执行J<font color="red">Jscript</font>代码。

```py
from selenium import webdriver

option = webdriver.ChromeOptions()
option.add_experimental_option('excludeSwitches', ['enable-automation'])
option.add_experimental_option('useAutomationExtension', False)
driver = webdriver.Chrome(options=option)
driver.execute_cdp_cmd('Page.addScriptToEvaluateOnNewDocument', {
    'source': 'Object.defineProperty(navigator, "webdriver", {get:()=>undefined})'
})

url = 'https://spa1.scrape.center/'
driver.get(url)
```





## 静默模式

  



```py
# 静默模式
# 初始化配置
from selenium import webdriver

# 初始化配置
options = webdriver.ChromeOptions()
# headless 为静默模式
options.add_argument('--headless')
# 将配置传入浏览器
driver = webdriver.Chrome(options=options)
# 设置窗口大小
driver.set_window_size(1366, 768)
driver.get('https://www.baidu.com')
# 窗口截图
driver.get_screenshot_as_file('preview.png')
```



## 实例化对象

```
from selenium import webdriver

driver = webdriver.Chrome()
driver = webdriver.Firefox()
driver = webdriver.Edge()
driver = webdriver.Safari()
```



## 查找节点

```
driver.get('html')
res = driver.find_elements()
res = driver.find_element()
res = driver.find_element_by_xpath()
res = driver.find_element_by_id()
‘’‘
driver.get('html')
driver.find_element(by='xpath', 'xpath')
driver.find_element_by_css_selector()
driver.find_element_by_partial_link_text()
...
’‘’
```

## 内置方法

```
# 获取属性
webdriver.get_attribute('src')
# 获取文本
webdriver.text
# 获取ID、位置、标签名、大小
webdriver.id
webdriver.location
webdriver.tag_name
webdriver.size
```



## iframe(frame)

父级页面无法直接访问子级页面

```
# 切换Frame  (iframe)
driver.switch_to.frame('iframeResult')
# 切换回父标签
driver.switch_to.parent_frame()  # 不用加参
```

## 延时等待

-   隐式等待：如果selenium没有找到节点，将继续等待，超出时间将抛异常，默认为0

    -   ```
        # 隐式等待
        
        from selenium import webdriver
        
        driver = webdriver.Chrome()
        driver.implicitly_wait(10)
        driver.get()
        ```

        

-   显示等待：
    -   python3网络爬虫开发实战P220

## 网页的前进和后退

方法：

-   前进：forward
-   后退：back

```
driver.forward()
driver.back()
```

## Cookie

使用Selenium对cookie进行：获取、添加、删除。

```
from selenium import webdriver

driver = webdriver.Chrome()

driver.get('html')
cookie = driver.get_cookies()
driver.add_cookie({
    'name': 'name',
    'domain': 'www.baidu.com',
    'value': 'germey'
})
driver.delete_all_cookies()
```

## 选型卡管理

(●'◡'●)：选项卡管理是指网页切换效果

```
import time
from selenium import webdriver
browser = webdriver.Chrome()
browser.get('https://www.baidu.com')
browser.execute_script('window.open()')
print(browser.window_handles)
browser.switch_to.window(browser.window_handles[1])
browser.get('https://www.taobao.com')
time.sleep(1)
browser.switch_to.window(browser.window_handles[0])
browser.get('https://python.org')

# ['CDwindow-D715E5E9FC0EB5FAF76FD4AD6DA617C5', 'CDwindow-09D9E6FF75264D16550D20AB09E4DFED']
```



## 获取源代码



```
browser.page_source
```
