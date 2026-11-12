import argparse
import sys
from cleaner import clean_data
import os
import logging

def main():
    #配置日志
    logging.basicConfig(format='%(asctime)s- %(levelname)s - %(message)s', level=logging.INFO)

    #设置参数解析
    parser = argparse.ArgumentParser(description='可重复的数据清洗流水线')
    parser.add_argument('--input',required=True,help='输入文件路径')
    parser.add_argument('--output', required=True, help='输出文件路径')
    args = parser.parse_args()

    #检查输入文件是否存在
    if not os.path.exists(args.input):
        logging.error(f"找不到输入文件{args.input}")
        sys.exit(1)
    try :
        logging.info("开始数据清洗流水线...")
        clean_data(args.input, args.output)
        sys.exit(0)
    except Exception as e:
        logging.error(f"发生错误{e}")
        sys.exit(1)

if __name__ == '__main__':
    main()
