#!/usr/bin/env python2.7
#coding:utf-8

# 需要重命名的文件放在Files文件夹中

import os

# UI文件夹的名称
ui_dir_name = 'assets'

def rename_files(files_path):
	
	# 获取目录下所有的文件
	file_names = os.listdir(files_path)

    # print('所有文件%s' % file_names)

	if len(file_names):
		files_dir_name = os.path.basename(files_path)

		pre_str = raw_input('请输入 %s 内需要重命名的前缀：' % files_dir_name)
		# print pre_str

		for temp in file_names:
			sub_file_path = os.path.join(files_path, temp)
			if os.path.isdir(sub_file_path):
				print ('文件夹%s'%sub_file_path)
				rename_files(sub_file_path)
				continue
			# iOS不需要用到@1.5x的图，所以需要删除
			if '@1.5' in temp:
				os.remove(sub_file_path)
			# 忽略隐藏文件 不对隐藏文件进行命名，且已经命名过的 不再命名
			elif (temp[0] != '.') and ((pre_str in temp) == False):
			    fname, ext = os.path.splitext(temp)
			    # 去除文件名中多余的空格
			    fname = fname.replace(' ','')
			    # base_name = os.path.basename(fname)
			    new_n = pre_str + '_' + fname + ext
			    print('%s =====> %s' % (temp ,new_n))
			    # print(os.path.join(files_path, new_n))
			    os.rename(sub_file_path, os.path.join(files_path, new_n))
	        # else:  
			    # print('!!!隐藏文件%s' % temp)
	else:
		print('%s文件夹是空的！！' % ui_dir_name)


if __name__ == '__main__':
	
	# 获取当前目录的绝对路径
	path = os.path.abspath('.')
	# print(path)

	files_path = os.path.join(path, ui_dir_name)
	# print(files_path)

	if os.path.exists(files_path) == True:
		rename_files(files_path)
	else:
		print('当前不存在%s文件夹！！' % ui_dir_name)

