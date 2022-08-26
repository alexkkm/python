## Markdown語法教程

### 標題

不同數量的`#`可以完成不同的標題，如下：

# 一級標題

## 二級標題

### 三級標題

### 2.2 字體

粗體、斜體、粗體和斜體，刪除線，需要在文字前後加不同的標記符號。如下：

**這個是粗體**

*這個是斜體*

***這個是粗體加斜體***

~這里想用刪除線~~

註：如果想給字體換顏色、字體或者居中顯示，需要使用內嵌HTML來實現。

### 2.3 無序列表

無序列表的使用，在符號`-`後加空格使用。如下：

- 無序列表 1
- 無序列表 2
- 無序列表 3

如果要控制列表的層級，則需要在符號`-`前使用空格。如下：

- 無序列表 1
- 無序列表 2
  - 無序列表 2.1
  - 無序列表 2.2

**由於微信原因，最多支持到二級列表**。

### 2.4 有序列表

有序列表的使用，在數字及符號`.`後加空格後輸入內容，如下：

1. 有序列表 1
2. 有序列表 2
3. 有序列表 3

### 2.5 引用

引用的格式是在符號`>`後面書寫文字。如下：

> 讀一本好書，就是在和高尚的人談話。 ——歌德

> 雇用制度對工人不利，但工人根本無力擺脫這個制度。 ——阮一峰

### 2.7 鏈接

微信公眾號僅支持公眾號文章鏈接，即功能變數名稱為`https://mp.weixin.qq.com/`的合法鏈接。使用方法如下所示：

對於該論述，歡迎讀者查閱之前發過的文章，[你是《未來世界的幸存者》麼？](https://mp.weixin.qq.com/s/s5IhxV2ooX3JN_X416nidA)
<a id="jump_8"></a>
### 2.8 圖片

插入圖片，格式如下：

![這里寫圖片描述](https://www.nginx.cn/wp-content/uploads/2020/03/qrcode_for_gh_82cf87d482f0_258.jpg)

支持 jpg、png、gif、svg 等圖片格式，**其中 svg 文件僅可在微信公眾平臺中使用**，svg 文件示例如下：

![](https://markdown.com.cn/images/i-am-svg.svg)

支持圖片**拖拽和截圖粘貼**到編輯器中。

註：支持圖片 ***拖拽和截圖粘貼*** 到編輯器中，僅支持 https 的圖片，圖片粘貼到微信時會自動上傳微信服務器。

### 2.9 分割線

可以在一行中用三個以上的減號來建立一個分隔線，同時需要在分隔線的上面空一行。如下：

---

### 2.10 表格

可以使用冒號來定義表格的對齊方式，如下：

| 姓名   | 年齡 |     工作 |
| :----- | :--: | -------: |
| 小可愛 |  18  | 吃可愛多 |
| 小小勇敢 |  20  | 爬棵勇敢樹 |
| 小小小機智 |  22  | 看一本機智書 |



## 3. 特殊語法

### 3.1 腳註

> 支持平臺：微信公眾號、知乎。

腳註與鏈接的區別如下所示：

```markdown
鏈接：[文字](鏈接)
腳註：[文字](腳註解釋 "腳註名字")
```

有人認為在[大前端時代](https://en.wikipedia.org/wiki/Front-end_web_development "Front-end web development")的背景下，移動端開發（Android、IOS）將逐步退出歷史舞臺。

[全棧工程師](是指掌握多種技能，並能利用多種技能獨立完成產品的人。 "什麼是全棧工程師")在業務開發流程中起到了至關重要的作用。

腳註內容請拉到最下麵觀看。

### 3.2 代碼塊

> 支持平臺：微信代碼主題僅支持微信公眾號！其他主題無限制。

如果在一個行內需要引用代碼，只要用反引號引起來就好，如下：

Use the `printf()` function.

在需要高亮的代碼塊的前一行及後一行使用三個反引號```，同時**第一行反引號後面表示代碼塊所使用的語言**，如下：

```java
// FileName: HelloWorld.java
public class HelloWorld {
  // Java 入口程式，程式從此入口
  public static void main(String[] args) {
    System.out.println("Hello,World!"); // 向控制台列印一條語句
  }
}
```

支持以下語言種類：

```
bash
clojure，cpp，cs，css
dart，dockerfile, diff
erlang
go，gradle，groovy
haskell
java，javascript，json，julia
kotlin
lisp，lua
makefile，markdown，matlab
objectivec
perl，php，python
r，ruby，rust
scala，shell，sql，swift
tex，typescript
verilog，vhdl
xml
yaml
```

如果想要更換代碼高亮樣式，可在上方**代碼主題**中挑選。

其中**微信代碼主題與微信官方一致**，有以下注意事項：

- 帶行號且不換行，代碼大小與官方一致
- 需要在代碼塊處標志語言，否則無法高亮
- 粘貼到公眾號後，用鼠標點代碼塊內外一次，完成高亮

diff 不能同時和其他語言的高亮同時顯示，且需要調整代碼主題為微信代碼主題以外的代碼主題才能看到 diff 效果，使用效果如下:

```diff
+ 新增項
- 刪除項
```

**其他主題不帶行號，可自定義是否換行，代碼大小與當前編輯器一致**

### 3.3 數學公式

塊公式使用方法如下：

$$H(D_2) = -\left(\frac{2}{4}\log_2 \frac{2}{4} + \frac{2}{4}\log_2 \frac{2}{4}\right) = 1$$

矩陣：

$$
  \begin{pmatrix}
  1 & a_1 & a_1^2 & \cdots & a_1^n \\
  1 & a_2 & a_2^2 & \cdots & a_2^n \\
  \vdots & \vdots & \vdots & \ddots & \vdots \\
  1 & a_m & a_m^2 & \cdots & a_m^n \\
  \end{pmatrix}
$$

公式由於微信不支持，目前的解決方案是轉成 svg 放到微信中，無需調整，矢量不失真。

目前測試如果公式量過大，在 Chrome 下會存在粘貼後無響應，但是在 Firefox 中始終能夠成功。

### 3.4 TOC

TOC 全稱為 Table of Content，列出全部標題。

[TOC]

由於微信只支持到二級列表，本工具僅支持二級標題和三級標題的顯示。

### 3.5 註音符號

支持註音符號，用法如下：

Markdown Nice 這麼好用，簡直是{喜大普奔|hē hē hē hē}呀！

### 3.6 橫屏滑動幻燈片

通過`<![](url),![](url)>`這種語法設置橫屏滑動滑動片，具體用法如下：

<![藍1](https://markdown.com.cn/images/blue.jpg),![綠2](https://markdown.com.cn/images/green.jpg),![紅3](https://markdown.com.cn.jpg)>

## 4 其他語法

### 4.1 HTML

支持原生 HTML 語法，請寫內聯樣式，如下：

<span style="display:block;text-align:right;color:orangered;">橙色居右</span>
<span style="display:block;text-align:center;color:orangered;">橙色居中</span>
