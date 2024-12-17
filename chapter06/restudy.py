# ids = input('input your ID')
#
# if len(ids)==18:
#     if ids[:-1].isdigit() and (ids[-1].isdigit() or ids[-1]=='X'):
#         print('input correctly')
#     else:
#         print('input wrong')
# else:
#     print('input wrong')

import re
print(re.match(r'\d+', '123456890')) # 数字
print(re.match(r'\w+', '123456890')) # 字母数字
print(re.match(r'^\s+$', '  ')) # 空白字符
print(re.match(r'^code\d-\d-\w+$', 'code1-1-re')) # 空白字符
print(re.match(r'^abcc*$', 'abc')) # 空白字符