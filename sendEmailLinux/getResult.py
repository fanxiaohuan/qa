#!/usr/bin/env python
import os
import re


def runReport(report):
    with open(r"/data/jenkins/workspace/epjs-jmeter/epjsReport.html",
              encoding='gb18030',
              errors='ignore') as f:  # 打开文件
        data = f.read()  # 读取文件
    m = re.findall(r'<td align="center">(.*?)</td>', data, re.I | re.M | re.S)
    list = []
    if m:
        for x in m:
            list.append(x)
    print(list[1])
    if list[1] == '0':
        report = "Successful"
    else:
        report = 'Failures= ' + list[1]
    print(report)

    return report
