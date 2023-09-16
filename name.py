import os
import re

def pad_numbers(match):
    """返回两位数的数字字符串."""
    return str(match.group(0)).zfill(2)

def rename_files_in_folder(folder_path):
    for filename in os.listdir(folder_path):
        # 使用正则表达式替换文件名中的一位数字为两位数字
        new_filename = re.sub(r'\b\d\b', pad_numbers, filename)
        if filename != new_filename:
            original_path = os.path.join(folder_path, filename)
            new_path = os.path.join(folder_path, new_filename)
            os.rename(original_path, new_path)
            print(f"Renamed '{original_path}' to '{new_path}'")

if __name__ == "__main__":
    target_folder = './r_online'
    rename_files_in_folder(target_folder)
