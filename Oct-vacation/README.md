# Oct-vacation

十一到了！

刚刚进入先锋的 xdx 们，准备好你们的第一战了吗？他来了！

最后的产物，请交到 github 上。也就是说，你们需要先 fork 此仓库，在自己的仓库里进行开发！最后，我希望得到的文件夹结构如下：

```shell
****\P-2024> tree .\Oct-vacation\
****\P-2024\OCT-VACATION
├───Task1
├───Task2
├───Task3
└───Task4
```

还有一件事，每个任务的文档，请记录在对应的文件夹的 `README.md` 文件中！

## 目录

- [Oct-vacation](#oct-vacation)
  - [目录](#目录)
  - [Task 1. Language - C](#task-1-language---c)
    - [Background](#background)
    - [Task](#task)
    - [Resources](#resources)
  - [Task 2. Algorithm in C](#task-2-algorithm-in-c)
    - [Background](#background-1)
    - [Task](#task-1)
    - [Resources](#resources-1)
  - [Task 3. Language - JavaScript](#task-3-language---javascript)
    - [Background](#background-2)
    - [Task](#task-2)
    - [Resources](#resources-2)
  - [Task 4. JavaScript in Browser](#task-4-javascript-in-browser)
    - [Background](#background-3)
    - [Task](#task-3)
    - [Resources](#resources-3)

## Task 1. Language - C

### Background

在我们大学里面，C 语言是计算机科学的基础，它可以帮助你理解计算机是如何工作的，以及如何编写程序来控制计算机。由于出现的时间较早，后来的语言相当多的借鉴了 C 的思想或风格，所以，可以片面的理解为，C 语言是其他现代编程语言的基础。

大部分的 xdx，老师都会让你使用 CodeBlocks 这款 IDE。它本身也确实是一个很不错的软件，但是，它并不支持现代的 C/C++ 标准。

所以，我们推荐你使用 Visual Studio Code，它是一款开源的、跨平台的、轻量级的、功能强大的 IDE，它支持多种编程语言，包括 C、C++、Python、Java、仓颉、rust 等等等，并且支持多种插件，可以满足你的大部分的开发需求！（此处尼哥注：用 python 做大项目，还是老实的使用 pycharm 吧）

### Task

所以，你们的任务 1 就是，使用 Visual Studio Code，想办法在你的主操作系统环境下，搭建起一个 C 语言开发环境。

PS：尽量记录过程中遇到的问题！！！

### Resources

- [VS code 下载处](https://code.visualstudio.com/Download)
- [VS code 官方文档](https://code.visualstudio.com/docs)

## Task 2. Algorithm in C

### Background

算法是计算机科学的基础，它本质上来说，就是“做事的方法”。不是说，“我又不打 acm，我学个毛线算法！”，而是算法能力是任何一个需要编程的人的核心能力、基础能力。算法的能力决定了你的上限，更决定了你的下限！

### Task

所以，你们的任务 2 就是，使用刚搭建起的 C 语言开发环境，编写一个排序算法，解决一个实际问题。排序算法的种类，可以由你们自选。但是，请不要使用 AI！AI 生成的代码，我们很可能认不出来，但是用 AI 写的代码，对你会有任何提高吗？

PS：还是那句话，尽量记录过程中遇到的问题！！！

### Resources

- [八大排序算法](https://blog.csdn.net/hguisu/article/details/7776068)

不得不承认，有些 csdn 博客真的不错。但是，有些 csdn 博客真的不行。一旦你们遇到了不行的博客，还没有辨认出来，那你就准备踩坑吧。

PS：我在大一时，在老师的帮助下，想到了一个本质上是极为类似桶排序的算法，其时间复杂度可以低至 O(8n)。如果你们有兴趣，后续我会把思路讲出来，我们一起实现它！做一个先锋的排序算法代码 show！

## Task 3. Language - JavaScript

### Background

JavaScript 是一种脚本语言，它可以在浏览器中运行，也可以在服务器端运行。它是一种非常灵活的语言，可以用来编写各种类型的程序，包括网页、移动应用、桌面应用、服务器应用等等。它不是 html 那种语言，但它能够改变 html 里的内容，xdx 们可以理解为，它是能够被浏览器解析的 python。

由于 JavaScript(下文统称 js) 是弱类型语言，使得它有极低的入门门槛，这曾经吸引了大量大量的人投身使用 js 的 web 前端开发，这些人中的大部分，最终都成为了前端开发工程师。但是，js 的弱类型，使得它有很多难以察觉的 bug，使得 js 的代码质量参差不齐，甚至无法维护。(这也是为什么我不喜欢学 js )

因此，后续出现了像 TS 一样的语言。但它本质上，是 js 的“超集”(可以暂时理解为基于 js 的脚本语言)，所以想要学现在火热的 ts，甚至以后学习鸿蒙开发用的 ArkTS，js 是要会的。

### Task

js 的能力取决于它的运行环境，在浏览器内，它能够改变 html 的代码；而在 nodejs 里，它能够做类似 python 能做的事(网络请求、文件操作等)。所以，你们的任务 3 就是，使用 nodejs，搭建起一个 JavaScript 开发环境。然后，你们需要想办法使得我提供的 js 代码能够正确执行 “计算器” 的效果。

PS：尽量记录过程中遇到的问题！！！

### Resources

- [nodejs 下载处](https://nodejs.org/zh-cn/download/)
- [怎么用 nodejs 编译 js 文件](https://cloud.tencent.com/developer/article/1836840)

## Task 4. JavaScript in Browser

### Background

### Task

你们的任务 4 是，保证一个菜鸟教程里的示例代码(**点亮灯泡**的那部分)能够在本地浏览器里运行起来。

也就是说，你们需要使得 `./Task4/example-bul.html` 能够`通过点击，开关小灯`。两个 gif 和你们可以稍微借鉴的 js 源代码，我已经附在此任务的 resources 文件夹里了。

PS：尽量记录过程中遇到的问题！！！并且，请使用我提供的那两个 gif，用人家的图片也可以！(这样你们能学习到一些“路径”的知识)

另附：我在我的 `VS code` 里，安装了 `TODO Tree` 这个插件，这个插件会高亮显示代码中的 TODO 注释，这样我能知道，代码里，我有什么地方还没去完善，推荐一波~

### Resources

- [示例代码寻址处 / js 教程](https://www.runoob.com/js/js-intro.html)
- [另一个还可以的 js 教程](https://zh.javascript.info/)