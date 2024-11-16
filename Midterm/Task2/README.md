# Task 2

请补充个人信息后，在此完成报告！

@Author:林荣强 
@Email:3500954350@qq.com

进行用户输入时在get_choice()中报错
  File "d:\ProgramingPlace\task2\P-2024-plan\Midterm\Task2\src\main.py", line 19, in get_choice
    result=int(choice);
           ^^^^^^^^^^^
ValueError: invalid literal for int() with base 10: '& D:/InstallPath/paython/python.exe d:/ProgramingPlace/task2/P-2024-plan/Midterm/Task2/src/main.py'
在转化时使用try语句,让用户重新输入

使用 json 库，以 json 文件的形式来存贮信息
基于栈实现历史记录;需要用到copy库来复制栈的信息来实现多次查看;在读取时不用try的话读取不成功历史操作的相关信息.
使用set来实现班级操作

