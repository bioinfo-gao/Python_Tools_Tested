import os
import zipfile


# 本法读和写分成两个步骤， 我的看法也可以一步

def zip_folder_with_filelist(folder_path, zip_filename):
    """
    打包指定文件夹到 ZIP，并在 ZIP 内生成 filelist.txt 清单
    """
    # 用于记录所有文件路径
    file_list = []

    # 第一步：遍历文件夹，收集所有文件路径
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            full_path = os.path.join(root, file)
            # 计算在 ZIP 中的相对路径
            arcname = os.path.relpath(full_path, folder_path)
            #print(arcname)
            file_list.append(arcname)


    # 第二步：创建 ZIP 文件并写入内容
    with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf: # 它代表“deflate”压缩方法 default

        # 先写入所有文件
        for arcname in file_list:
            #print(arcname) # 相对于 原folder的相对路径
            full_path = os.path.join(folder_path, arcname)
            #print(full_path ) # 再加上folder的路径

            zipf.write(full_path, arcname) # 原文件极其路径。 archive 文件名称
            print(f"📦 已打包: {arcname}")

        # 生成清单内容
        list_content = "打包文件清单:\n" + "=" * 50 + "\n"
        list_content += "\n".join(file_list)
        list_content += f"\n\n总计: {len(file_list)} 个文件"

        # 将清单文件写入 ZIP
        zipf.writestr("filelist.txt", list_content.encode('utf-8'))
        print(f"📋 已生成清单: filelist.txt (含 {len(file_list)} 个文件)")

    print(f"\n✅ 打包完成！ZIP 文件: {zip_filename}")


# ========== 使用示例 ==========
if __name__ == "__main__":
    folder_to_backup = "data"  # 👈 替换为你的文件夹名
    output_zip = "data_with_list.zip"  # 👈 输出 ZIP 文件名

    zip_folder_with_filelist(folder_to_backup, output_zip)