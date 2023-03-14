# js基础

script地址





<script>元素

</script>

-   async : 可选、立即开始下载脚本、但不能阻止其他页面的动作（只对外部脚本有用）
-   charset ：了解即可
-   defer :可选、脚本可以延迟到文档全部被解析和显示后在执行。（只对外部脚本有效）
-   integrity ：可选
-   src :可选



## js文件嵌套



### 过去方式

```
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Document</title>
    <script src="./project.js"></script>
    <script src="./project.js"></script>
    <script src="./project.js"></script>
  </head>
  <body></body>
</html>
```



>   过去我们把\<script>元素都放到header标签内：把所有的js代码都下载下来、解析和解释完成后才开始渲染
>
>   缺点：对于页面有很多js代码情况下、页面有明显的延迟。



### 现代 ：\<script>标签一般放到header内容之后

```
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Document</title>
  </head>
  <body>
    <!-- 这里是页面的内容 -->
    <script src=""></script>
    <script src=""></script>
    <script src=""></script>
  </body>
</html>

```



### defer属性 ：来推迟js页面渲染

```
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Document</title>
    <script src="" defer></script>
    <script src="" defer></script>
    <script src="" defer></script>
  </head>
  <body>
    <!-- 这里是页面的内容 -->
  </body>
</html>
```



### 异步执行脚本

```
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Document</title>
    <script src="" async="async"></script>
    <script src="" async="async"></script>
    <script src="" async="async"></script>
  </head>
  <body>
    <!-- 这里是页面的内容 -->
  </body>
</html>
```

>   异步执行，不规定js脚本的下载顺序、也不强制让页面等待js脚本下载、但在此期间不能修改网页的**DOM**
>
>   也就是相当于告诉浏览器、我不会使用 document.write
>
>   一般不推荐使用



### 动态加载脚本

略





## 语法：

不区分小数和整数

### 标识符：



-   区分大小写
-   标识符：必须以（一个字母、下划线 _、 美元符号 $
-   采用驼峰命名法



### 注释

```javascript
// 单行注释
/* 多行注释 */
```



### 严格模式 

>   ECMAScript 5 增加严格模式（strict mode)、



### 设置严格模式

以下代码属于预处理指令

```js
"use strict"
```

也可以单独的对一个函数使用严格模式

```
function doSomething{
	"use strict"
	// 函数体
}
```

所有现代浏览器都支持严格模式



### 语句

```
let sum = a + b  // 不推荐、会造成很多隐藏问题
let diff = a - b ;  // 推荐
```



## :sa:  数据类型

**变量**：**let** a = 10;

​			**var** b = ‘哈哈哈’



**常量**：**conse** PI = 3.14

<font color='red'>常量不能被修改</font>、只能赋值一次、修改后会报错

>   变量：变量存储的是值的内存地址！！
>
>   常量：一般用大写声明  const PI = 3.145

-   字面量：1000、‘哈哈哈’

-   number：数字类型（整数、浮点数）（数值、科学计数法、

    -   infinity(无限大的数 数据大小有限制)

    -   NaN：非法数字（not a Number)   1- ‘a’

        BigInt：大整数（用来表示比较大的整数（一串数字以n结尾）（222222222222222n)没有上限

    -   其他进制数

>   在js中在精度比较高时不适合直接进行计算 （特别是小数运算）

