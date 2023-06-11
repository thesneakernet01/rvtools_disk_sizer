import pandas as pd
import math

excel_file = 'excel_file_name.xlsx'

vpartition_spreadsheet = pd.read_excel(excel_file, sheet_name=4, index_col=0 )
vdisk_spreadsheet = pd.read_excel(excel_file, sheet_name=3, index_col=0 )
vinfo_spreadsheet = pd.read_excel(excel_file, sheet_name=0, index_col=0 )

sum_vpartition_consumedMIB = vpartition_spreadsheet['Consumed MiB'].sum()
sum_vdisk_capacity = vdisk_spreadsheet['Capacity MiB'].sum()
sum_vinfo_capacity = vinfo_spreadsheet['In Use MiB'].sum()
sum_vinfo_provisioned = vinfo_spreadsheet['Provisioned MiB'].sum()

vpartition_size = int(float(sum_vpartition_consumedMIB))
vdisk_size = int(float(sum_vdisk_capacity))
vinfo_size = int(float(sum_vinfo_capacity))
vinfo_provisioned_size = int(float(sum_vinfo_provisioned))

try:
    converted_vpartition_size = (vpartition_size/1024**2)
    converted_vpartition_size = int(converted_vpartition_size)
    print("vPartition indicates we have",converted_vpartition_size, "TB of Disk Consumed")

    converted_vdisk_size = (vdisk_size/1024**2)
    converted_vdisk_size = int(converted_vdisk_size)
    print("vDisk indicates we have",converted_vdisk_size, "TB of Disk Provisioned")

    converted_vinfo_size = (vinfo_size/1024**2)
    converted_vinfo_size = int(converted_vinfo_size)
    print("vinfo indicates we have",converted_vinfo_size, "TB of in use Disk")

    converted_vinfo_provisioned_size = (vinfo_provisioned_size/1024**2)
    converted_vinfo_provisioned_size = int(converted_vinfo_provisioned_size)
    print("vinfo indicates we have",converted_vinfo_provisioned_size, "TB of Provisioned Disk")


except:
    print("Kablam!")