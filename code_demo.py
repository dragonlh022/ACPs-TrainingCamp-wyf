def bubble_sort(arr):
    """冒泡排序：升序排列数字列表"""
    arr = arr.copy()
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def find_first_position(sorted_arr, target):
    """
    查找目标数字第一次出现的索引位置
    :param sorted_arr: 已排序的数字列表
    :param target: 要查找的数字
    :return: 第一个位置索引，不存在返回 None
    """
    for idx, num in enumerate(sorted_arr):
        if num == target:
            return idx
    return None

def get_user_numbers():
    """获取用户输入的数字，带异常处理"""
    while True:
        try:
            user_input = input("请输入一串数字，用空格分隔：")
            num_list = [float(i) for i in user_input.strip().split()]
            return num_list
        except ValueError:
            print("输入错误！请只输入数字和空格，重试")

def get_target_number():
    """获取用户要查找的数字"""
    while True:
        try:
            target = float(input("\n请输入要查找的数字："))
            return target
        except ValueError:
            print("输入错误！请输入有效数字～")

if __name__ == "__main__":
    print("===== 数字排序与查找工具 =====")
    
    # 1. 获取输入并排序
    numbers = get_user_numbers()
    sorted_numbers = bubble_sort(numbers)
    
    print("\n排序前：", numbers)
    print("排序后：", sorted_numbers)
    
    # 2. 查找特定数字
    target = get_target_number()
    pos = find_first_position(sorted_numbers, target)
    
    # 3. 输出结果
    if pos is not None:
        print(f"\n数字 {target} 第一次出现的位置：索引 {pos}")
    else:
        print(f"\n数字 {target} 无")
