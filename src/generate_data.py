import pandas as pd
import numpy as np
import os

# 确保目录存在
os.makedirs('../data/raw', exist_ok=True)

# 制造 100 行数据
data = {
    'id': [1, 2, 3, 3, 4, 5, np.nan], # 有缺失，有重复
    'name': ['Alice', 'Bob', 'Charlie', 'Charlie', 'David', '', 'Eve'], # 有空字符串
    'age': [25, -5, 30, 30, 45, 200, 'unknown'], # 有非法值(-5, 200, unknown)
    'date': ['2023-01-01', '2023-13-45', '2023-02-01', '2023-02-01', '2023-03-01', '2023-04-01', '2023-05-01'] # 有非法日期
}

df = pd.DataFrame(data)
df.to_csv('../data/raw/dirty_data.csv', index=False, encoding='utf-8')
print("脏数据生成成功！路径：data/raw/dirty_data.csv")