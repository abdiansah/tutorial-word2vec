# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 22:34:59 2020

@author: Abdiansah
"""

import os, sys

""" FUNGSI UNTUK MENGUBAH SEMUA NAMA BERKAS """
#rename_seluruh_file('./folder/','file','pdf')
def rename_files(src_dir, label, buka_folder=False):
    i = 1
    des_dir = src_dir
    filenames = os.listdir(src_dir)
    for filename in filenames:
        des_dir += '{}-{}'.format(label,str(i))
        os.rename('{}{}'.format(src_dir, filename), des_dir)
        des_dir = src_dir
        i+=1
    print('\nProses perubahan nama file selesai.')
    print('Directory: {} ({} files - initial {})'.format(src_dir, i-1, label))
    if buka_folder:
        os.system('dolphin '+src_dir)
        
#rename_files('./AF/','f') 

if __name__ == "__main__":
   rename_files(sys.argv[1], sys.argv[2])
