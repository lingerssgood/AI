#1、 导入库
import pandas as pd

# 2、生成异常数据
df = pd.DataFrame({'col1': [1, 120, 3, 5, 2, 12, 13], 'col2': [12, 17, 31, 53, 22, 32, 43]})
print(df)  # 打印输出
# 3、通过Z-Score判断异常值
df_zscore = df.copy()  # 复制一个数据框
cols = df.columns
for col in cols:
    df_col = df[col]
    z_score = (df_col - df_col.mean()) / df_col.std()
    df_zscore[col] = z_score.abs() > 2.2
    print(df_zscore)
#4、 删除异常值所在的记录行
df_drop_outlier = df[df_zscore['col1'] == False]
print(df_drop_outlier)
