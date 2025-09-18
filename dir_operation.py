import os
import shutil

# 1️⃣ 获取当前工作目录
current_dir = os.getcwd()
print(f"当前工作目录: {current_dir}")

# 2️⃣ 创建新目录（如果不存在）
new_dir_name = "my_new_folder"
new_dir_path = os.path.join(current_dir, new_dir_name)

os.makedirs(new_dir_path, exist_ok=True)  # exist_ok=True 避免目录已存在时报错
print(f"已创建目录: {new_dir_path}")

# 3️⃣ 复制文件到新目录
source_file = "example.txt"      # 👈 替换为你想复制的源文件路径
dest_file = os.path.join(new_dir_path, "example.txt")

try:
    shutil.copy2(source_file, dest_file)  # copy2 保留元数据（如修改时间）
    print(f"✅ 文件已复制: {source_file} → {dest_file}")
except FileNotFoundError:
    print(f"❌ 源文件 '{source_file}' 不存在！")
except PermissionError:
    print(f"❌ 权限不足，无法复制文件！")
except Exception as e:
    print(f"❌ 复制失败: {e}")