import json as log
import numpy as ny

import re


file_log = open(r'D:\project\python\6-25\secure.log')

log_error = []
for item in file_log:
    # print(type(item))
    if "Failed password for root" in item:
        reg = re.compile(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})')
        all_ip = re.findall(reg, item)
        log_error.append(all_ip[0])


myset = set(log_error)
log_error_times = []
for item in myset:
    c = item, log_error.count(item)
    log_error_times.append(c)


final_log = []
for item in log_error_times:
    if item[1] > 4:
        al = 'IP:'+item[0]+'进入服务器'+str(item[1])+'次'
        final_log.append(al)
print(final_log)

f = open('D:/test.txt', 'a')
for item in final_log:
    f.write(item)
    f.write("\n")

f.close()
