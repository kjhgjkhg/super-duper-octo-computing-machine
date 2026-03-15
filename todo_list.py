#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
简易命令行待办事项管理小程序
功能：添加、查看、删除、标记完成待办事项
"""

from datetime import datetime


def get_valid_date_input():
    """
    获取并验证用户输入的截止日期
    返回：datetime对象或None（如果用户不输入日期）
    """
    while True:
        date_str = input("请输入截止日期（格式：YYYY-MM-DD，直接回车跳过）：").strip()
        if not date_str:
            return None
        try:
            deadline = datetime.strptime(date_str, "%Y-%m-%d")
            return deadline
        except ValueError:
            print("❌ 日期格式无效，请使用 YYYY-MM-DD 格式")


def add_todo(todo_list):
    """
    添加待办事项到列表中
    参数：todo_list - 待办事项列表
    """
    print("\n=== 添加待办事项 ===")
    content = input("请输入待办事项内容：").strip()
    
    if not content:
        print("❌ 待办事项内容不能为空！")
        return
    
    deadline = get_valid_date_input()
    
    todo_item = {
        "content": content,
        "deadline": deadline,
        "completed": False,
        "created_at": datetime.now()
    }
    
    todo_list.append(todo_item)
    print("✅ 待办事项添加成功！")


def sort_todos_by_deadline(todo_list):
    """
    按截止时间排序待办事项
    参数：todo_list - 待办事项列表
    返回：排序后的待办事项列表
    """
    def get_sort_key(item):
        if item["deadline"] is None:
            return datetime.max
        return item["deadline"]
    
    return sorted(todo_list, key=get_sort_key)


def display_todos(todo_list):
    """
    显示所有待办事项（按截止时间排序）
    参数：todo_list - 待办事项列表
    """
    print("\n=== 待办事项列表 ===")
    
    if not todo_list:
        print("📭 暂无待办事项")
        return
    
    sorted_todos = sort_todos_by_deadline(todo_list)
    
    for index, todo in enumerate(sorted_todos, 1):
        status = "✅ 已完成" if todo["completed"] else "⏳ 未完成"
        deadline_str = todo["deadline"].strftime("%Y-%m-%d") if todo["deadline"] else "无截止日期"
        print(f"{index}. [{status}] {todo['content']} (截止：{deadline_str})")


def get_valid_index(prompt, max_value):
    """
    获取并验证用户输入的序号
    参数：prompt - 提示文本，max_value - 最大有效序号
    返回：有效的索引（从0开始）或None（如果输入无效）
    """
    try:
        num = int(input(prompt))
        if 1 <= num <= max_value:
            return num - 1
        else:
            print(f"❌ 序号必须在 1 到 {max_value} 之间")
            return None
    except ValueError:
        print("❌ 请输入有效的数字序号")
        return None


def delete_todo(todo_list):
    """
    删除指定的待办事项
    参数：todo_list - 待办事项列表
    """
    print("\n=== 删除待办事项 ===")
    
    if not todo_list:
        print("📭 暂无待办事项可删除")
        return
    
    display_todos(todo_list)
    sorted_todos = sort_todos_by_deadline(todo_list)
    
    index = get_valid_index("请输入要删除的待办事项序号：", len(sorted_todos))
    if index is not None:
        todo_to_delete = sorted_todos[index]
        todo_list.remove(todo_to_delete)
        print("✅ 待办事项删除成功！")


def mark_completed(todo_list):
    """
    标记待办事项为已完成
    参数：todo_list - 待办事项列表
    """
    print("\n=== 标记待办事项完成 ===")
    
    if not todo_list:
        print("📭 暂无待办事项可标记")
        return
    
    display_todos(todo_list)
    sorted_todos = sort_todos_by_deadline(todo_list)
    
    index = get_valid_index("请输入要标记完成的待办事项序号：", len(sorted_todos))
    if index is not None:
        sorted_todos[index]["completed"] = True
        print("✅ 待办事项已标记为完成！")


def display_menu():
    """
    显示主菜单
    """
    print("\n" + "=" * 40)
    print("📋 简易待办事项管理系统")
    print("=" * 40)
    print("1. 添加待办事项")
    print("2. 查看所有待办事项")
    print("3. 删除待办事项")
    print("4. 标记待办事项完成")
    print("0. 退出系统")
    print("=" * 40)


def get_valid_menu_choice():
    """
    获取并验证用户输入的菜单选项
    返回：有效的选项数字或None
    """
    choice = input("请输入选项（0-4）：").strip()
    if choice in ['0', '1', '2', '3', '4']:
        return int(choice)
    else:
        print("❌ 无效选项，请输入 0-4 之间的数字")
        return None


def main():
    """
    主函数：程序入口
    """
    todo_list = []
    
    print("欢迎使用简易待办事项管理系统！")
    
    while True:
        display_menu()
        choice = get_valid_menu_choice()
        
        if choice is None:
            continue
        
        if choice == 0:
            print("\n👋 感谢使用，再见！")
            break
        elif choice == 1:
            add_todo(todo_list)
        elif choice == 2:
            display_todos(todo_list)
        elif choice == 3:
            delete_todo(todo_list)
        elif choice == 4:
            mark_completed(todo_list)


if __name__ == "__main__":
    main()
