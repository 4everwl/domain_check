import os
import requests
import re
import sys
from multiprocessing.pool import ThreadPool
from datetime import datetime
#    _____          __  .__                       ____  ________  ______  
#   /  _  \  __ ___/  |_|  |__   ___________  /\ /_   |/  _____/ /  __  \ 
#  /  /_\  \|  |  \   __\  |  \ /  _ \_  __ \ \/  |   /   __  \  >      < 
# /    |    \  |  /|  | |   Y  (  <_> )  | \/ /\  |   \  |__\  \/   --   \
# \____|__  /____/ |__| |___|  /\____/|__|    \/  |___|\_____  /\______  /
#         \/                 \/                              \/        \/ 

baidu_url = "https://www.aizhan.com/cha/"
output_folder = "out"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:126.0) Gecko/20100101 Firefox/126.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
    'Accept-Encoding': 'gzip, deflate'
}

def check(domain_url):
    try:
        r = requests.get(url=baidu_url + domain_url, headers=headers)
        match1 = re.search(r'/images/br/(\d+)\.png', r.text)
        match2 = re.search(r'/images/mbr/(\d+)\.png', r.text)
        match3 = re.search(r'/images/pr/(\d+)\.png', r.text)
        if match1 or match2 or match3:
            number1 = match1.group(1) if match1 else "N/A"
            number2 = match2.group(1) if match2 else "N/A"
            number3 = match3.group(1) if match3 else "N/A"
            result = f"百度: {number1}  移动: {number2}  谷歌: {number3}  ------ {domain_url}"
            save_to_file(result)
        else:
            print("未找到相关信息:", domain_url)
    except Exception as e:
        print("出错了:", e)

def save_to_file(result):
    global output_file_path
    try:
        with open(output_file_path, 'a', encoding='utf-8') as f:
            f.write(result + "\n")
    except Exception as e:
        print("保存文件出错:", e)

def process_line(line):
    if 'http://' in line:
        line = line[7:]
    elif 'https://' in line:
        line = line[8:]
    line = line.split(":")[0].strip() if ":" in line else line.strip()
    print(line)
    return line

def main():
    if len(sys.argv) != 2:
        # 不带参数 显示 --help
        print("使用方法: python domain_check.py .txt文件路径 ")
        sys.exit(1)
        
    file_path = sys.argv[1]
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            domains = [process_line(line) for line in f if line.strip()]
    except Exception as e:
        print("文件读取错误:", e)
        sys.exit(1)
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    now = datetime.now()
    file_name = now.strftime("%Y-%m-%d_%H-%M-%S") + ".txt"
    global output_file_path
    output_file_path = os.path.join(output_folder, file_name)

   
    pool = ThreadPool(processes=6)  # 你可以根据需要调整线程数
    for domain in domains:
        if domain:
            pool.apply_async(check, (domain,))

    pool.close()
    pool.join()

    print("success!!!")


if __name__ == '__main__':
    main()
