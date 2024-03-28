import pandas as pd
import os
import re

# 读取Excel花名册文件
roster_path = 'exm_name_path.xlsx'
df = pd.read_excel(roster_path, usecols=['姓名', '学号'])  # 提取列名

# 过滤出有学号和姓名的行
df = df.dropna(subset=['姓名', '学号'])

# 将学号转换为字符串，确保格式一致
df['学号'] = df['学号'].astype(str)

# 输入所有已提交实验报告汇总文件夹的路径
folder_path = 'exm_path'

# 输入每个学生应该提交的实验报告数量 N
N = 5

# 读取文件夹中的所有文件
files = os.listdir(folder_path)

# 初始化学生提交状态记录
submission_status = {name: set() for name in df['姓名'].tolist()}

# 检测和分类文件
for file in files:
    # 用正则表达式匹配文件名格式“学号-姓名-专业-实验X”(X表示实验报告序号)
    match = re.match(r'(\d+)-(.+?)-.+?-实验(\d+)', file)
    if match:
        student_number, student_name, report_number = match.groups()
        # 检查学号和姓名是否匹配
        if df[(df['学号'] == student_number) & (df['姓名'] == student_name)].any().any():
            # 记录已提交的实验报告
            submission_status[student_name].add("实验" + report_number)
            # 为每个学生创建或确认文件夹存在
            student_folder = os.path.join(folder_path, student_name)
            if not os.path.exists(student_folder):
                os.makedirs(student_folder)
            # 移动文件到相应的文件夹
            src_path = os.path.join(folder_path, file)
            dst_path = os.path.join(student_folder, file)
            os.rename(src_path, dst_path)

# 创建未提交人员及实验报告记录
with open(os.path.join(folder_path, "未提交.txt"), "w", encoding="utf-8") as f:
    for student, reports_submitted in submission_status.items():
        all_reports = {f"实验{i}" for i in range(1, N + 1)}
        missing_reports = all_reports - reports_submitted
        if missing_reports:
            if len(missing_reports) == N:
                f.write(f"{student}：全部未交\n")
            else:
                missing_reports_str = "，".join(sorted(missing_reports))
                f.write(f"{student}：{missing_reports_str}\n")

print("分类完成，未提交名单已更新")
