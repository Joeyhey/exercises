"""
这是一个小工具
如果不传入参数，那么运行会自动统计该文件自身的 空行数/注释数/代码行数
如果传入参数，则统计指定文件的 空行数/注释数/代码行数
传参方法：python statistical_itself.py destination_file_path
注意目标文件路径用'/'而不是复制粘贴过来的'\'
"""

import sys
import os

if len(sys.argv) > 1:
    filename = sys.argv[1]
else:
    filename = __file__
    # filename = os.path.basename(__file__)
    # filename = sys.argv[0]

print(filename)

blank = 0
comment = 0
code = 0

with open(filename, encoding='utf-8') as file_object:
    lines = file_object.readlines()
for line in lines:
    compare_line = line.strip()
    if compare_line == '':
        blank += 1
    elif compare_line[0] == '#':  # djas
        comment += 1
    else:
        code += 1

print(blank)
print(comment)
print(code)
# else if()

# print(sys.argv)
