# go语言基础

## 第一个程序：hollow——world

```
package main

import "fmt"

func main() {
	fmt.Println("Hello World")
}
```

1.   第一行代码package main定义了包名。你必须在源文件中非注释的第一行指明这个文件属于哪个包，如：package main。pack
     age main表示一个可独立执行的程序，每个Go应用程序都包含一个名为main的包。
2.   下一行mpot"fmt"告诉Go编译器这个程序需要使用fmt包（的函数，或其他元素），fmt包实现了格式化IO(输入输出)的
     函数。
3.   下一行func main(0是程序开始执行的函数。main函数是每一个可执行程序所必须包含的，一般来说都是在启动后第一个执行的
     函数（如果有init()函数则会先执行该函数）。
4.   下一行*.*1是注释，在程序执行时将被忽略。单行注释是最常见的注释形式，你可以在任何地方使用以/开头的单行注释。多
     行注释也叫块注释，均已以*开头，并以*/结尾，且不可以嵌套使用，多行注释一般用于包的文档描述或注释成块的代码片段。
5.   下一行fmt.Println(.)可以将字符串输出到控制台，并在最后自动增加换行字符n。
     使用fmt.Print("helo,world\n")可以得到相同的结果。
     Print和Println这两个函数也支持使用变量，如：fmt.Println(arr)。如果没有特别指定，它们会以默认的打印格式将变量arr输出
     到控制台。
6.   当标识符（包括常量、变量、类型、函数名、结构字段等等）以一个大写字母开头，如：Goup1,那么使用这种形式的标识符的
     对象就可以被外部包的代码所使用（客户端程序需要先导入这个包），这被称为导出（像面向对象语言中的public)；标识符如
     果以小写字母开头，则对包外是不可见的，但是他们在整个包的内部是可见并且可用的（像面向对象语言中的protected)。

## go 语言基础语法

### 代码书写规范

go语言和Python一样，没有结尾  **;**  如果你想要将多行代码写到一行、你必须把每个指令后加  **;**

```
var a int = 17; fmt.Println("你好呀")

a := 18  # 自动识别类型
fmt.Println("你好呀")
```

### 基本数据类型：

-   #### 基础类型

    -   数字类型
        -   整数类型(**int**:64、32....)
        -   浮点型(**float**:...)
    -   字符串类型:**string**
    -   布尔值:**bool**

-   #### 派生类型

    -   指针类型(Pointer)
    -   数组类型
    -   结构化类型(struct)
    -   Channel类型
    -   函数类型
    -   切片类型
    -   接口类型(interface)
    -   Map类型



#### 数字类型详解：

| 序号 | 类型和描述                                                   |
| :--- | :----------------------------------------------------------- |
| 1    | **uint8** 无符号 8 位整型 (0 到 255)                         |
| 2    | **uint16** 无符号 16 位整型 (0 到 65535)                     |
| 3    | **uint32** 无符号 32 位整型 (0 到 4294967295)                |
| 4    | **uint64** 无符号 64 位整型 (0 到 18446744073709551615)      |
| 5    | **int8** 有符号 8 位整型 (-128 到 127)                       |
| 6    | **int16** 有符号 16 位整型 (-32768 到 32767)                 |
| 7    | **int32** 有符号 32 位整型 (-2147483648 到 2147483647)       |
| 8    | **int64** 有符号 64 位整型 (-9223372036854775808 到 9223372036854775807) |

#### 浮点型详解：

| 序号 | 类型和描述                        |
| :--- | :-------------------------------- |
| 1    | **float32** IEEE-754 32位浮点型数 |
| 2    | **float64** IEEE-754 64位浮点型数 |
| 3    | **complex64** 32 位实数和虚数     |
| 4    | **complex128** 64 位实数和虚数    |

#### 其他数字类型：

| 1    | **byte** 类似 uint8                      |
| ---- | ---------------------------------------- |
| 2    | **rune** 类似 int32                      |
| 3    | **uint** 32 或 64 位                     |
| 4    | **int** 与 uint 一样大小                 |
| 5    | **uintptr** 无符号整型，用于存放一个指针 |



## go语言的变量声明



### 变量命名规则：

Go 语言变量名由**字母、数字、下划线**组成，其中首个字符不能为数字。

### 定义变量：var

>   注意：字符串声明时 必须使用**双引号**、单引号表示**ASII码表**

定义变量的几种方法：

```
package main

import "fmt"  // 这个也可以多个 导入包

func main() {  // 注意这个大括号不能单独起一行
    // 标准定义
	var a int = 18
	var b string = "哈哈哈哈或"

	//  := 编译器自动判断定义 （！！必须是一个新的变量定义、要不报错）
	c := "哈哈哈哈或"
	d := 14 

	// 较新坂本
	var e = "哈哈哈哈"
	// 打印数据类型（格式化打印）fmt.Printf()
	fmt.Printf("%t : %T\n,%t : %T\n,%t : %T\n,%t : %T\n,%t : %T\n",a,a, b,b, c,c, d,d, e,e)
}

/* 18 : int
,哈哈哈哈或 : string
,哈哈哈哈或 : string
,14 : int
,哈哈哈哈 : string */


// 定义多个变量
var(
	a int = 123
	b string = "哈哈哈哈"
	c = Flase
)
```



### 变量声明

**第一种，指定变量类型，如果没有初始化，则变量默认为零值**。

```
var v_name v_type
v_name = value
```



### 常量声明：const

>   常量声明后、后期不能修改、再重新赋值会报错



```
const a, b, c = 3.16, "hhh", false  // 常量的多个声明
```



### 特殊变量：iota

>   iota 是go 语言内置的，**每一个 const组**iota都是从 **0**开始计数

```
//iota,go语言内置的特殊常量  从第一个const开始为0，以此类推 是个  常量计数器（以组为单位）
const (
		name = iota
		age  = iota
		hhh
		yyy = "hhhh"
		rrr
		i = iota
		p
)
fmt.Println(name, age, hhh, yyy, rrr, i, p) //注意 b没有赋值但还是被赋值为2！！！！
//0 1 2 hhhh hhhh 5 6
```

## go 格式化字符串

-   fmt.Sprintf ()

    ```
    fmt.Sprintf(格式化样式, 参数列表…)
    ```

    -   **格式化样式：**字符串形式，格式化符号以 **%** 开头， %s 字符串格式，%d 十进制的整数格式。
    -   **参数列表：**多个参数以逗号分隔，个数必须与格式化样式中的个数一一对应，否则运行时会报错。

    

    ### Go 字符串格式化符号:

    | 格  式 | 描  述                                   |
    | :----- | :--------------------------------------- |
    | %v     | 按值的本来值输出                         |
    | %+v    | 在 %v 基础上，对结构体字段名和值进行展开 |
    | %#v    | 输出 Go 语言语法格式的值                 |
    | %T     | 输出 Go 语言语法格式的类型和值           |
    | %%     | 输出 % 本体                              |
    | %b     | 整型以二进制方式显示                     |
    | %o     | 整型以八进制方式显示                     |
    | %d     | 整型以十进制方式显示                     |
    | %x     | 整型以十六进制方式显示                   |
    | %X     | 整型以十六进制、字母大写方式显示         |
    | %U     | Unicode 字符                             |
    | %f     | 浮点数                                   |
    | %p     | 指针，十六进制方式显示                   |

-   fmt.Printf

    ```
    fmt.Printf(格式化样式, 参数列表…)
    ```

    -   **格式化样式：**字符串形式，格式化符号以 **%** 开头， %s 字符串格式，%d 十进制的整数格式。
    -   **参数列表：**多个参数以逗号分隔，个数必须与格式化样式中的个数一一对应，否则运行时会报错。

    

    ### Go 字符串格式化符号:

    | 格  式 | 描  述                                   |
    | :----- | :--------------------------------------- |
    | %v     | 按值的本来值输出                         |
    | %+v    | 在 %v 基础上，对结构体字段名和值进行展开 |
    | %#v    | 输出 Go 语言语法格式的值                 |
    | %T     | 输出 Go 语言语法格式的类型和值           |
    | %%     | 输出 % 本体                              |
    | %b     | 整型以二进制方式显示                     |
    | %o     | 整型以八进制方式显示                     |
    | %d     | 整型以十进制方式显示                     |
    | %x     | 整型以十六进制方式显示                   |
    | %X     | 整型以十六进制、字母大写方式显示         |
    | %U     | Unicode 字符                             |
    | %f     | 浮点数                                   |
    | %p     | 指针，十六进制方式显示                   |



## 注释：//



```
// 单行注释
/*
 Author by 菜鸟教程
 我是多行注释
 */
```



## 关键字

下面列举了 Go 代码中会使用到的 25 个关键字或保留字：

| break    | default     | func   | interface | select |
| -------- | ----------- | ------ | --------- | ------ |
| case     | defer       | go     | map       | struct |
| chan     | else        | goto   | package   | switch |
| const    | fallthrough | if     | range     | type   |
| continue | for         | import | return    | var    |

除了以上介绍的这些关键字，Go 语言还有 36 个预定义标识符：

| append | bool    | byte    | cap     | close  | complex | complex64 | complex128 | uint16  |
| ------ | ------- | ------- | ------- | ------ | ------- | --------- | ---------- | ------- |
| copy   | false   | float32 | float64 | imag   | int     | int8      | int16      | uint32  |
| int32  | int64   | iota    | len     | make   | new     | nil       | panic      | uint64  |
| print  | println | real    | recover | string | true    | uint      | uint8      | uintptr |

程序一般由关键字、常量、变量、运算符、类型和函数组成。

程序中可能会使用到这些分隔符：括号 ()，中括号 [] 和大括号 {}。

程序中可能会使用到这些标点符号：.、,、;、: 和 …。



## 运算符

### 算数运算符

下表列出了所有Go语言的算术运算符。假定 A 值为 10，B 值为 20。

| 运算符 | 描述 | 实例               |
| :----- | :--- | :----------------- |
| +      | 相加 | A + B 输出结果 30  |
| -      | 相减 | A - B 输出结果 -10 |
| *      | 相乘 | A * B 输出结果 200 |
| /      | 相除 | B / A 输出结果 2   |
| %      | 求余 | B % A 输出结果 0   |
| ++     | 自增 | A++ 输出结果 11    |
| --     | 自减 | A-- 输出结果 9     |



### 关系运算符

下表列出了所有Go语言的关系运算符。假定 A 值为 10，B 值为 20。

| 运算符 | 描述                                                         | 实例              |
| :----- | :----------------------------------------------------------- | :---------------- |
| ==     | 检查两个值是否相等，如果相等返回 True 否则返回 False。       | (A == B) 为 False |
| !=     | 检查两个值是否不相等，如果不相等返回 True 否则返回 False。   | (A != B) 为 True  |
| >      | 检查左边值是否大于右边值，如果是返回 True 否则返回 False。   | (A > B) 为 False  |
| <      | 检查左边值是否小于右边值，如果是返回 True 否则返回 False。   | (A < B) 为 True   |
| >=     | 检查左边值是否大于等于右边值，如果是返回 True 否则返回 False。 | (A >= B) 为 False |
| <=     | 检查左边值是否小于等于右边值，如果是返回 True 否则返回 False。 | (A <= B) 为 True  |



### 逻辑运算符

下表列出了所有Go语言的逻辑运算符。假定 A 值为 True，B 值为 False。

| 运算符 | 描述                                                         | 实例               |
| :----- | :----------------------------------------------------------- | :----------------- |
| &&     | 逻辑 AND 运算符。 如果两边的操作数都是 True，则条件 True，否则为 False。 | (A && B) 为 False  |
| \|\|   | 逻辑 OR 运算符。 如果两边的操作数有一个 True，则条件 True，否则为 False。 | (A \|\| B) 为 True |
| !      | 逻辑 NOT 运算符。 如果条件为 True，则逻辑 NOT 条件 False，否则为 True。 |                    |



### 位运算符

位运算符对整数在内存中的二进制位进行操作。

下表列出了位运算符 &, |, 和 ^ 的计算：

| p    | q    | p & q | p \| q | p ^ q |
| :--- | :--- | :---- | :----- | :---- |
| 0    | 0    | 0     | 0      | 0     |
| 0    | 1    | 0     | 1      | 1     |
| 1    | 1    | 1     | 1      | 0     |
| 1    | 0    | 0     | 1      | 1     |

Go 语言支持的位运算符如下表所示。假定 A 为60，B 为13：

| 运算符 | 描述                                                         | 实例                                   |
| :----- | :----------------------------------------------------------- | :------------------------------------- |
| &      | 按位与运算符"&"是双目运算符。 其功能是参与运算的两数各对应的二进位相与。 | (A & B) 结果为 12, 二进制为 0000 1100  |
| \|     | 按位或运算符"\|"是双目运算符。 其功能是参与运算的两数各对应的二进位相或 | (A \| B) 结果为 61, 二进制为 0011 1101 |
| ^      | 按位异或运算符"^"是双目运算符。 其功能是参与运算的两数各对应的二进位相异或，当两对应的二进位相异时，结果为1。 | (A ^ B) 结果为 49, 二进制为 0011 0001  |
| <<     | 左移运算符"<<"是双目运算符。左移n位就是乘以2的n次方。 其功能把"<<"左边的运算数的各二进位全部左移若干位，由"<<"右边的数指定移动的位数，高位丢弃，低位补0。 | A << 2 结果为 240 ，二进制为 1111 0000 |
| >>     | 右移运算符">>"是双目运算符。右移n位就是除以2的n次方。 其功能是把">>"左边的运算数的各二进位全部右移若干位，">>"右边的数指定移动的位数。 | A >> 2 结果为 15 ，二进制为 0000 1111  |



### 赋值运算符

下表列出了所有Go语言的赋值运算符。

| 运算符 | 描述                                           | 实例                                  |
| :----- | :--------------------------------------------- | :------------------------------------ |
| =      | 简单的赋值运算符，将一个表达式的值赋给一个左值 | C = A + B 将 A + B 表达式结果赋值给 C |
| +=     | 相加后再赋值                                   | C += A 等于 C = C + A                 |
| -=     | 相减后再赋值                                   | C -= A 等于 C = C - A                 |
| *=     | 相乘后再赋值                                   | C *= A 等于 C = C * A                 |
| /=     | 相除后再赋值                                   | C /= A 等于 C = C / A                 |
| %=     | 求余后再赋值                                   | C %= A 等于 C = C % A                 |
| <<=    | 左移后赋值                                     | C <<= 2 等于 C = C << 2               |
| >>=    | 右移后赋值                                     | C >>= 2 等于 C = C >> 2               |
| &=     | 按位与后赋值                                   | C &= 2 等于 C = C & 2                 |
| ^=     | 按位异或后赋值                                 | C ^= 2 等于 C = C ^ 2                 |
| \|=    | 按位或后赋值                                   | C \|= 2 等于 C = C \| 2               |



### 其他运算符

下表列出了Go语言的其他运算符。

| 运算符 | 描述             | 实例                       |
| :----- | :--------------- | :------------------------- |
| &      | 返回变量存储地址 | &a; 将给出变量的实际地址。 |
| *      | 指针变量。       | *a; 是一个指针变量         |



### 运算符优先级

有些运算符拥有较高的优先级，二元运算符的运算方向均是从左至右。下表列出了所有运算符以及它们的优先级，由上至下代表优先级由高到低：

| 优先级 | 运算符           |
| :----- | :--------------- |
| 5      | * / % << >> & &^ |
| 4      | + - \| ^         |
| 3      | == != < <= > >=  |
| 2      | &&               |
| 1      | \|\|             |

当然，你可以通过使用括号来临时提升某个表达式的整体运算优先级。



## 条件判断

-   **if...(else)..**

    ```
    if 布尔表达式 {
       /* 在布尔表达式为 true 时执行 */
    }else{
      pass
    }
    ```

-   **switch**

    ```
    switch var1 {
        case val1:
            ...
        case val2:
            ...
        default:
            ...
    }
    ```

​		和c很像！！！！

-   **select**

    select 是 Go 中的一个控制结构，类似于 switch 语句。

    select 语句**只能用于通道操作**，每个 case 必须是一个通道操作，要么是发送要么是接收。

    select 语句会监听所有指定的通道上的操作，一旦其中一个通道准备好就会执行相应的代码块。

    如果多个通道都准备好，那么 select 语句会随机选择一个通道执行。如果所有通道都没有准备好，那么执行 default 块中的代码。

    Go 编程语言中 select 语句的语法如下：

    ```
    **select** {
     **case** <- channel1:
      *// 执行的代码*
     **case** value := <- channel2:
      *// 执行的代码*
     **case** channel3 <- value:
      *// 执行的代码*
    
      *// 你可以定义任意数量的 case*
    
     **default**:
      *// 所有通道都没有准备好，执行的代码*
    }
    ```

    代码演示

    ```
    **package** main
    
    **import** (
      "fmt"
      "time"
    )
    
    func main() {
    
      c1 := make(chan string)
      c2 := make(chan string)
    
      **go** func() {
        time.Sleep(1 * time.Second)
        c1 <- "one"
      }()
      **go** func() {
        time.Sleep(2 * time.Second)
        c2 <- "two"
      }()
    
      **for** i := 0; i < 2; i++ {
        **select** {
        **case** msg1 := <-c1:
          fmt.Println("received", msg1)
        **case** msg2 := <-c2:
          fmt.Println("received", msg2)
        }
      }
    }
    ```

    

## 循环：for

### 无限循环

如果循环中条件语句永远不为 false 则会进行无限循环，我们可以通过 for 循环语句中只设置一个条件表达式来执行无限循环：

### 实例

```
package** main

**import** "fmt"

func main() {
  **for** **true** {
    fmt.Printf("这是无限循环。**\n**");
  }
}
```

**循环当然也可以嵌套**

控制语句：

### **break**

### **continue**

### **goto:(跳转到代码指定位置！！！)**

在变量 a 等于 15 的时候跳过本次循环并回到循环的开始语句 LOOP 处：



### goto实例

```
**package** main

**import** "fmt"

func main() {
  */\* 定义局部变量 \*/*
  **var** a int = 10

  */\* 循环 \*/*
  LOOP: **for** a < 20 {
   **if** a == 15 {
     */\* 跳过迭代 \*/*
     a = a + 1
     **goto** LOOP
   }
   fmt.Printf("a的值为 : %d**\n**", a)
   a++   
  } 
}
```



## go语言函数的定义

### 格式：

```
func function_name( [parameter list] ) [return_types] {
   函数体
}
```



### 实例：（函数的定义、函数的引用）

```go
package main

import "fmt"

// 函数的形参要规定类型！！！！
func test(y string) (int, string) {
	var a = 19
	var b = y
	return a, b
}

func main() {
	c, _ := test("hhhh") // 隐变量的使用
	_, d := test("hhhh")
	fmt.Println(c, d)

}

//19 hhhh
```



### 函数参数分为：

-   值传递（默认）：不会改变原值
-   引用传递： 引用传递是指在调用函数时将实际参数的地址传递到函数中，那么在函数中对参数所进行的修改，将影响到实际参数。



### 引用传递案例



```
package main

import "fmt"

func main() {
	/* 定义局部变量 */
	var a int = 100
	var b int = 200

	fmt.Printf("交换前，a 的值 : %d\n", a)
	fmt.Printf("交换前，b 的值 : %d\n", b)

	/* 调用 swap() 函数
	 * &a 指向 a 指针，a 变量的地址
	 * &b 指向 b 指针，b 变量的地址
	 */
	swap(&a, &b)

	fmt.Printf("交换后，a 的值 : %d\n", a)
	fmt.Printf("交换后，b 的值 : %d\n", b)
}

// 主要的交换函数
func swap(x *int, y *int) {
	var temp int
	temp = *x /* 保存 x 地址上的值 */
	*x = *y   /* 将 y 值赋给 x */
	*y = temp /* 将 temp 值赋给 y */
}

```



## go 语言数组



>   数组定义好后、长度固定、多则报错

### 一维数组：声明格式

```go
var variable_name [SIZE] variable_type

//实例化
var balance [10] float32
```



以下演示了数组初始化：

```
var balance = [5]float32{1000.0, 2.0, 3.4, 7.0, 50.0}
```

我们也可以通过字面量在声明数组的同时快速初始化数组：

```
balance := [5]float32{1000.0, 2.0, 3.4, 7.0, 50.0}
```

如果数组长度不确定，可以使用 **...** 代替数组的长度，编译器会根据元素个数自行推断数组的长度：

```
var balance = [...]float32{1000.0, 2.0, 3.4, 7.0, 50.0}
或
balance := [...]float32{1000.0, 2.0, 3.4, 7.0, 50.0}
```

如果设置了数组的长度，我们还可以通过指定下标来初始化元素：

```
//  将索引为 1 和 3 的元素初始化
balance := [5]float32{1:2.0,3:7.0}
```

初始化数组中 **{}** 中的元素个数不能大于 **[]** 中的数字。

如果忽略 **[]** 中的数字不设置数组大小，Go 语言会根据元素的个数来设置数组的大小：

```
 balance[4] = 50.0
```



### 实例

```
package main

import "fmt"

func main() {
   var n [10]int /* n 是一个长度为 10 的数组 */
   var i,j int

   /* 为数组 n 初始化元素 */        
   for i = 0; i < 10; i++ {
      n[i] = i + 100 /* 设置元素为 i + 100 */
   }

   /* 输出每个数组元素的值 */
   for j = 0; j < 10; j++ {
      fmt.Printf("Element[%d] = %d\n", j, n[j] )
   }
}
```

！（和c语言很像）

### 多维数组

```
var variable_name [SIZE1][SIZE2]...[SIZEN] variable_type
```

以下实例声明了三维的整型数组：

```
var threedim [5][10][4]int
```



理解Python里的 pandans和 numpy



二维数组中的元素可通过 **a[ i ][ j ]** 来访问。

### 实例

```
package main

import "fmt"

func main() {
  // Step 1: 创建数组*
  values := [][]int{}

  // Step 2: 使用 append() 函数向空的二维数组添加两行一维数组*
  row1 := []int{1, 2, 3}
  row2 := []int{4, 5, 6}
  values = append(values, row1)
  values = append(values, row2)

  // Step 3: 显示两行数据*
  fmt.Println("Row 1")
  fmt.Println(values[0])
  fmt.Println("Row 2")
  fmt.Println(values[1])

  *// Step 4: 访问第一个元素*
  fmt.Println("第一个元素为：")
  fmt.Println(values[0][0])
}
```



### 向函数传递数组

>   你需要在函数定义时，声明形参为数组，我们可以通过以下两种方式来声明：



#### 方式一

形参设定数组大小：

```
void myFunction(listname [10]int)
{
.
.
.
}
```

#### 方式二

形参未设定数组大小：

```
void myFunction(listname []int)
{
.
.
.
}
```



实例

```
func getAverage(arr []int, size int) float32
{
  var i int
  var avg, sum float32 

  for i = 0; i < size; ++i {
   sum += arr[i]
  }

  avg = sum / size

  return avg;
}
```



浮点数计算有偏差、要设置精度

```
package main
import (
    "fmt"
)
func main() {
    a := 1690           // 表示1.69
    b := 1700           // 表示1.70
    c := a * b          // 结果应该是2873000表示 2.873
    fmt.Println(c)      // 内部编码
    fmt.Println(float64(c) / 1000000) // 显示
```



## go语言指针：&



>变量是一种使用方便的占位符，用于引用计算机内存地址。
>
>Go 语言的取地址符是 &，放到一个变量前使用就会返回相应变量的内存地址。



！打印变量地址

```
package main

import "fmt"

func main() {
   var a = 18
   fmt.Printf("%x", &a)
   // 打印出a的地址：c00009e058
}
```



>   指针变量指定的是一个变量的内存地址
>
>   类似于变量和常量，在使用指针前你需要声明指针。指针声明格式如下：



```
var var_name *var-type

var ip *int        /* 指向整型*/
var fp *float32    /* 指向浮点型 */
```



### 使用指针

指针使用流程：

-   定义指针变量。
-   为指针变量赋值。
-   访问指针变量中指向地址的值。

在指针类型前面加上 * 号（前缀）来获取指针所指向的内容。

### 实例

```
package** main

**import** "fmt"

func main() {
  **var** a int= 20  */\* 声明实际变量 \*/*
  **var** ip *int     */\* 声明指针变量 \*/*

  ip = &a  */\* 指针变量的存储地址 \*/*

  fmt.Printf("a 变量的地址是: %x**\n**", &a  )

  */\* 指针变量的存储地址 \*/*
  fmt.Printf("ip 变量储存的指针地址: %x**\n**", ip )

  */\* 使用指针访问值 \*/*
  fmt.Printf("*ip 变量的值: %d**\n**", *ip )
}
```

以上实例执行输出结果为：

```
a 变量的地址是: 20818a220
ip 变量储存的指针地址: 20818a220
*ip 变量的值: 20
```



### go  空指针



>   当一个指针被定义后、没有分配到任何变量时、它的值为：**nil**
>
>   nil 指针也称为空指针。
>
>   nil在概念上和其它语言的null、None、nil、NULL一样，都指代零值或空值。
>
>   一个指针变量通常缩写为 ptr。



### 空指针判



```
if(pty != nil) 
if(pty == nil)
```



### go 指针数组

>   定义一个指针数组来存放地址

、

有一种情况，我们可能需要保存数组，这样我们就需要使用到指针。

以下声明了整型指针数组：

```
var ptr [MAX]*int;
```

ptr 为整型指针数组。因此每个元素都指向了一个值。以下实例的三个整数将存储在指针数组中：

## 实例

```
package** main

**import** "fmt"

**const** MAX int = 3

func main() {
  a := []int{10,100,200}
  **var** i int
  **var** ptr [MAX]*int;

  **for** i = 0; i < MAX; i++ {
   ptr[i] = &a[i] */\* 整数地址赋值给指针数组 \*/*
  }

  **for** i = 0; i < MAX; i++ {
   fmt.Printf("a[%d] = %d**\n**", i,*ptr[i] )
  }
}
```



以上代码执行输出结果为：

```
a[0] = 10
a[1] = 100
a[2] = 200
```



### 指向指针的指针

>   概念：如果一个指针变量存放的又是另一个指针变量的存放地址，则称这个指针变量为 **指向指针的指针变量**

指向指针的指针变量声明格式如下：

```
var ptr **int;
```

以上指向指针的指针变量为整型。



访问指向指针的指针变量值需要使用两个 * 号，如下所示：

```
package main

import "fmt"

func main() {

   var a int
   var ptr *int
   var pptr **int

   a = 3000

   /* 指针 ptr 地址 */
   ptr = &a

   /* 指向指针 ptr 地址 */
   pptr = &ptr

   /* 获取 pptr 的值 */
   fmt.Printf("变量 a = %d\n", a )
   fmt.Printf("指针变量 *ptr = %d\n", *ptr )
   fmt.Printf("指向指针的指针变量 **pptr = %d\n", **pptr)
}
```



代码结果

```
变量 a = 3000
指针变量 *ptr = 3000
指向指针的指针变量 **pptr = 3000
```



### 向函数传递指针参数

>   通过引用地址传参、在函数调用时可以改变其值
>
>   语言作为指针函数



类似于函数的两值交换、直接改变原值



## 结构体

>    结构体是由一系列具有相同类型或不同类型的数据构成的数据集合。
>
>   结构体表示一项记录，比如保存图书馆的书籍记录，每本书有以下属性：
>
>   -   Title ：标题
>   -   Author ： 作者
>   -   Subject：学科
>   -   ID：书籍ID



​	

```
package main

import "fmt"

// 结构体类型变量使用 struct 关键字定义
type Books struct {
   title   string
   author  string
   subject string
   book_id int
}

func main() {
   /*结构体示例代码*/
   //1、创建一个新的结构体 也可以键值对
   fmt.Println(Books{"go语言", "hhh", "jljj", 19})
}
```



### 访问结构体成员：**.**

```
结构体.成员名"
```



```go
package main

import "fmt"

type Books struct {
   title   string
   author  string
   subject string
   book_id int
}

func main() {
   /*结构体示例代码*/
   //1、创建一个新的结构体 也可以键值对
   var book1 Books // 说明books1为Books类型

   var book2 Books // 说明books2位Books类型

   //books描述
   book1.title = "go原因"
   book1.book_id = 19
   book1.author = "natsume"
   book1.subject = "并发编程"

   book2.title = "python原因"
   book2.book_id = 20
   book2.author = "natsume37"
   book2.subject = "快"

   fmt.Println(book1.title)
   fmt.Println(book1.book_id)
   fmt.Println(book1.subject)
   fmt.Println(book1.author)
}

go原因
19
并发编程
natsume
```



>   go 语言的结构体与 Python的字典非常像，只不过采用了最原始的 **.**方式



### 结构体作为函数参数

>   由于go语言是静态语言、所以在**函数需要参数时u、函数的形参必须要定义类型**



```
package main

import "fmt"

type Books struct {
   title   string
   author  string
   subject string
   book_id int
}

func main() {
   /*结构体示例代码*/
   //1、创建一个新的结构体 也可以键值对
   var book1 Books // 说明books1为Books类型

   var book2 Books // 说明books2位Books类型

   //books描述
   book1.title = "go原因"
   book1.book_id = 19
   book1.author = "natsume"
   book1.subject = "并发编程"

   book2.title = "python原因"
   book2.book_id = 20
   book2.author = "natsume37"
   book2.subject = "快"
	
   // 调用函数
   test(book1)

}

func test(book Books) {
   fmt.Println(book.title)
   fmt.Println(book.book_id)
   fmt.Println(book.subject)
   fmt.Println(book.author)
}
```





### 结构体指针



你可以定义指向结构体的指针类似于其他指针变量，格式如下：

```
var struct_pointer *Books
```

以上定义的指针变量可以存储结构体变量的地址。查看结构体变量地址，可以将 & 符号放置于结构体变量前：

```
struct_pointer = &Book1
```

使用结构体指针访问结构体成员，使用 "." 操作符：

```
struct_pointer.title
```





## 切片（Slice）



>   是go语言内置的强悍的 切片（“动态数组”）好处：长度不固定、可以追加元素、切片容量可以改变



#### 格式

```
var identifier []type
```

切片不需要说明长度。

>   和Python的数组很像、只不过定义方式不一样

或使用 **make()** 函数来创建切片:

```
var slice1 []type = make([]type, len)

也可以简写为

slice1 := make([]type, len)
```

