# scrapy基础



scrapy环境下在

```python
pip install scrapy -i https://pypi.doubanio.com/simple/
# 这句话后面 -i https://pypi.doubanio.com/simple/ 表示使用豆瓣的源，这样安装会更快
```

url ：https://www.appinn.com/category/windows/



**爬虫.py**

```
import scrapy

# 定义一个类叫做 TitleSpider 继承自 scrapy.Spider
class TitleSpider(scrapy.Spider):
  name = 'title-spider'
  # 设定开始爬取的页面
  start_urls = ['https://www.appinn.com/category/windows/']

  def parse(self, response):
    # 找到所有 article 元素
    for article in response.css('article'):
      # 解析 article 下面 a 元素里的链接和标题
      a = article.css('h2.title a')
      if a:
        result = {
          'title': a.attrib['title'],
          'url': a.attrib['href'],
        }
        # 得到结果
        yield result

    # 解析下一页的链接
    next_page = response.css('a.next::attr(href)').get()
    if next_page is not None:
      # 开始爬下一页，使用 parse 方法解析
      yield response.follow(next_page, self.parse)
```



**运行**

```python
scrapy runspider 爬虫.py -t csv -o apps.py
```

由于数据量较大、系统要缓一会。



官方提供的css选择器体验（交互式体验）

```
scrapy shell "https://www.appinn.com/category/windows/"
```

```
按元素名选择
response.css(‘ul’)

按class选择 用.代替class
response.css('div.container')

按ID选择 用#代替ID
response.css('a#pull')

按层级关系选择
response.css('h2.title.post-title a') 和 select很像


取元素中的文本：拿到了标题位置的 a 元素，想要拿到其中的文本内容就需要在后面加上 ::text
response.css('h2.title.post-title a::text')

获取纯文本
# 取符合条件的第一条数据
response.css('h2.title.post-title a::text').get()

# 取符合条件的所有数据
response.css('h2.title.post-title a::text').getall()

attrib ：获取属性值
# 拿到符合选择器条件的第一个 a 元素
a = response.css('h2.title.post-title a')
a.attrib['href']

或者
for href in response.css('h2.title.post-title a::attr(href)').getall():
  print(href)
```



项目实战：



生成scrapy项目文件 ：appinn

```
scrapy startproject appinn
```



文件目录：

```
appinn
├── appinn         # 项目代码所在的目录
│   ├── __init__.py
│   ├── items.py     # 定义数据的格式
│   ├── middlewares.py
│   ├── pipelines.py   # 处理数据、输出到文件等等
│   ├── settings.py    # 一些设置
│   └── spiders      # 爬虫所在的目录
│       └── __init__.py
└── scrapy.cfg
```

配置：items：爬取内容

在命令行里执行下面的命令并回车，它会帮我们创建一个叫做 **article** 的爬虫，并且只爬取 **www.appinn.com** 下的网页：

```
scrapy genspider article www.appinn.com
```



配置完所有 开始执行

```
scrapy crawl article
```





