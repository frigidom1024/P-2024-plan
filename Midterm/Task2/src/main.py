# 学生管理系统
import json
import copy
# PS: 可以仅以 “姓名” / “学号” 来代指学生信息

STU_LIST = [
    
]
STU_FILE = "Midterm/Task2/stduent.json"
CLASS="Midterm\Task2\class_info.json"
TYPEHISTORY="Midterm/Task2/operation_type.json"
INFOHISTORY="Midterm/Task2/operation_info.json"

CLASSES={}

operationTypeStack=[] #记录操作

operationInfoStack=[]#记录操作信息
ADD_STUDENT = 1
DELETE_STUDENT = 2
MODIFY_STUDENT = 3
CREATE_CLASS = 4
MODIFY_CLASS_STUDENTS = 5

def view_operation_history():
    """此函数用于，查看操作的历史记录"""
    print("操作历史记录：")
    operationTypeStack1 = copy.deepcopy(operationTypeStack)
    operationInfoStack1 = copy.deepcopy(operationInfoStack)
    while operationTypeStack1:
        operation_type = operationTypeStack1.pop()
        operation_info = operationInfoStack1.pop()
        if operation_type == ADD_STUDENT:
            print(f"操作：添加学生，学生信息：{operation_info}")
        elif operation_type == DELETE_STUDENT:
            print(f"操作：删除学生，被删除学生信息：{operation_info}")
        elif operation_type == MODIFY_STUDENT:
            print(f"操作：修改学生信息，姓名:{operation_info[0]['姓名']} 学号:{operation_info[0]['学号']} -> 姓名:{operation_info[1]['姓名']} 学号:{operation_info[1]['学号']}")
        elif operation_type == CREATE_CLASS:
            print(f"操作：创建班级，班级名称：{operation_info['班级名称']}")
        elif operation_type == MODIFY_CLASS_STUDENTS:
            print(f"操作：修改班级学生，{operation_info['班级名称']}，{operation_info['操作']}，学生姓名：{operation_info['学生姓名']}")
    pass


def stu_init():
    """此函数用于, 从文件中, 初始化学生信息"""
    global STU_LIST
    with open (STU_FILE,'r',encoding='utf-8') as f:
        STU_LIST=json.load(f)
    #with open (TYPEHISTORY,'r',encoding='utf-8') as t:
    #    operationTypeStack=json.load(t)
try:
    with open(TYPEHISTORY, 'r', encoding='utf-8') as t:
        operationTypeStack = json.load(t)
    with open(INFOHISTORY, 'r', encoding='utf-8') as k:
        operationInfoStack = json.load(k)
    with open(CLASS,'r',encoding='utf-8') as w:
        CLASSES=json.load(w)
except Exception as e:

    print(f"读取错误:{e}")
    print("读取成功");
    pass

def get_choice() -> int:
    """此函数用于, 在命令行里, 获取用户输入的选项"""
    choice = input("请输入一个整数（按提示要求输入相应数字）：")
    try:
        result = int(choice)
    except ValueError:
        print("您输入的不是合法的整数，请重新输入！")
        return get_choice()
    return result


def menu():
    """此函数用于, 在命令行里, 打印出菜单"""
    print("1.增加学生");
    print("2.删除学生");
    print("3.修改学生信息");
    print("4.查询学生信息");
    print("5.保存学生信息");
    print("6.查看操作历史");
    print("7.班级操作");
    print("0.退出系统");
    pass


def stu_add():
    """此函数用于, 添加学生信息"""
    studentName=input("姓名:");
    studentId=input("学号:");
    STU_LIST.append({'姓名':studentName,'学号':studentId});

    #记入操作历史
    operationTypeStack.append(1)
    operationInfoStack.append({'姓名':studentName,'学号':studentId})

    print(studentName,studentId);
    pass


def stu_del():
    """此函数用于，删除学生信息"""
    id = input("请输入要删除学生的学号")
    global STU_LIST
    deleted_students = []
    for student in STU_LIST:
        if student['学号'] == id:
            deleted_students.append(student)
    STU_LIST = [student for student in STU_LIST if student['学号']!= id]
    # 将操作类型（2表示删除操作）和被删除的学生信息压入栈
    operationTypeStack.append(2)
    operationInfoStack.append(deleted_students)
    pass



def stu_mod():
    """此函数用于, 修改学生信息"""
    id=input("需修改的学生学号")
    global STU_LIST
    for student in STU_LIST:
        if student['学号']==id:
            print("该学生信息为:",student)
            newname=input("请输入新名字:(输入空格则不进行修改)")
            newid=input("请输入新学号:(输入空格则不进行修改)")
            mod=[]
            mod.append(student)
            if newname!=' ':student['姓名']=newname
            if newid!=' ':student['学号']=newid
            mod.append(student)

            #记入操作历史
            operationTypeStack.append(3)
            operationInfoStack.append(mod)
            print("修改完成")
            return
    print("未查找的相应学生")
    pass


def stu_sel():
    """此函数用于, 查询学生信息"""
    print(f"{'姓名':<10}{'学号':<10}")
    for student in STU_LIST:
        print(f"{student['姓名']:<10}{student['学号']:<10}")
    pass


def stu_save():
    """此函数用于, 将学生信息保存到文件中"""
    print("ndwa")
    global STU_LIST
    with open(STU_FILE, 'w', encoding='utf-8') as f:
        json.dump(STU_LIST, f, ensure_ascii=False, indent=4)
    with open(TYPEHISTORY,'w',encoding='utf-8') as t:
        json.dump(operationTypeStack,t,ensure_ascii=False,indent=4)
    with open(INFOHISTORY,'w',encoding='utf-8') as i:   
        json.dump(operationInfoStack,i,ensure_ascii=False,indent=4)
    with open(CLASS,'w',encoding='utf-8') as k:
        json.dump(CLASSES,k,ensure_ascii=False,indent=4)
    print("信息已保存")
    pass

def class_menu():
    """此函数用于，在班级操作相关界面里，打印出菜单"""
    print("1.创建班级");
    print("2.修改班级学生");
    print("3.查看班级");
    print("0.返回主菜单");
    pass

def class_view_info():
    """此函数用于，查看所有班级信息"""
    print("现有班级信息如下：")
    for class_name, students in CLASSES.items():
        print(f"班级名称：{class_name}")
        print(f"{"姓名":<10}{"学号":<10}")
        for student in students:
            print(f"{student['姓名']:<10}{student['学号']:<10}")
    pass

def class_create():
    """此函数用于，创建班级"""
    class_name = input("请输入班级名称：")
    if class_name in CLASSES:
        print(f"班级 {class_name} 已存在，请重新输入！")
        return
    CLASSES[class_name] = []
    print(f"班级 {class_name} 创建成功！")
    operationTypeStack.append(CREATE_CLASS)
    operationInfoStack.append({'班级名称': class_name})
    pass

def class_modify_students():
    """此函数用于，修改班级学生"""
    print("现有班级：")
    for class_name in CLASSES:
        print(class_name)
    target_class = input("请输入要修改学生的班级名称：")
    if target_class not in CLASSES:
        print(f"班级 {target_class} 不存在，请重新输入！")
        return
    print("1.添加学生到班级")
    print("2.从班级移除学生")
    choice = input("请选择操作（输入对应数字）：")
    if choice == "1":
        student_name = input("请输入要添加的学生姓名：")
        for student in STU_LIST:
            if student['姓名'] == student_name:
                CLASSES[target_class].append(student)
                print(f"学生 {student_name} 已添加到班级 {target_class}")
                # 记入操作历史
                operationTypeStack.append(MODIFY_CLASS_STUDENTS)
                operationInfoStack.append({'班级名称': target_class, '操作': '添加学生', '学生姓名': student_name})
                return
        print(f"未找到名为 {student_name} 的学生，请检查输入！")
    elif choice == "2":
        student_name = input("请输入要移除的学生姓名：")
        students_in_class = CLASSES[target_class]
        new_students_in_class = [student for student in students_in_class if student['姓名']!= student_name]
        CLASSES[target_class] = new_students_in_class
        print(f"学生 {student_name} 已从班级 {target_class} 移除")
        # 记入操作历史
        operationTypeStack.append(MODIFY_CLASS_STUDENTS)
        operationInfoStack.append({'班级名称': target_class, '操作': '移除学生', '学生姓名': student_name})
    else:
        print("无效选项，请重新输入！")
    pass

def class_operation():
    """此函数用于，控制班级操作相关流程"""
    while True:
        class_menu()
        choice = input("请输入一个整数（按提示要求输入相应数字）：")
        try:
            choice = int(choice)
            if choice == 1:
                class_create()
            elif choice == 2:
                class_modify_students()
            elif choice==3 :
                class_view_info()
            elif choice == 0:
                break
            else:
                print("无效选项，请重新输入！")
        except ValueError:
            print("您输入的不是合法的整数，请重新输入！")

    pass

def exec(choice):
    """此函数用于, 根据用户输入的选项, 执行相应的功能"""
    if choice==1:stu_add()
    elif choice==2:stu_del()
    elif choice==3:stu_mod()
    elif choice==4:stu_sel()
    elif choice==5:stu_save()
    elif choice==6:view_operation_history()
    elif choice==7:class_operation()
    elif choice==0:print("退出")
    else :print("无效选项")
    pass


def main():
    """尽量不要修改此函数的代码, 此函数用于全局调用"""
#user_choice = get_choice()
    stu_init()
    user_choice=1
    while user_choice != 0:
        menu()
        user_choice = get_choice()
        exec(user_choice)
    pass


if __name__ == '__main__':
    main()
