import pandas as pd
import logging
logger = logging.getLogger(__name__)
def clean_data(input_path, output_path):
    logging.info(f"开始读取数据{input_path}")
    try:
        df = pd.read_csv(input_path,encoding='utf-8')
    except UnicodeDecodeError:
        logging.warning("UTF-8读取失败，尝试 GBK 编码")
        df = pd.read_csv(input_path,encoding='gbk')

    #清洗数据
    initial_rows = df.shape[0]

    #去除完全重复的行
    df = df.drop_duplicates()

    # 处理非法值
    df['age'] = pd.to_numeric(df['age'], errors='coerce')
    df= df[(df['age'] >= 0) & (df['age'] <= 120)]
    df['date'] = pd.to_datetime(df['date'], errors='coerce')

    #去除id,date缺失的行，并填充name缺失的样本
    df = df.dropna(subset = ['id','date'])
    df['name'] = df['name'].replace('', pd.NA).fillna("Unknown")

    #保存清洗后的数据
    df.to_csv(output_path, index=False, encoding='utf-8')
    logging.info(f"清洗完成！原始数据 {initial_rows} 行，清洗后 {len(df)} 行。已保存至: {output_path}")

if __name__ == '__main__':
    clean_data('../data/raw/dirty_data.csv','../data/processed/clean_data.csv')
