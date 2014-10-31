#!/usr/bin/python
# -*- coding: utf-8 -*-

### BEGIN LICENSE

# Copyright (C) 2013 National University of Defense Technology(NUDT) & Kylin Ltd

# Author:
#     Wen Bo<wenbo@ubuntukylin.com>
#     Shine Huang<shenghuang@ubuntukylin.com>
# Maintainer:
#     Wen Bo<wenbo@ubuntukylin.com>
#     Shine Huang<shenghuang@ubuntukylin.com>

# This program is free software: you can redistribute it and/or modify it
# under the terms of the GNU General Public License version 3, as published
# by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranties of
# MERCHANTABILITY, SATISFACTORY QUALITY, or FITNESS FOR A PARTICULAR
# PURPOSE.  See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program.  If not, see <http://www.gnu.org/licenses/>.


import os
import re
import subprocess
import commands

def get_run_command(pkgname):
    # 对一些特殊软件单独处理
    if pkgname == 'wps-office':
        pkgname = 'wps-office-wps'
    elif pkgname == 'uget':
        pkgname = 'uget-gtk'
    elif pkgname == 'eclipse-platform':
        pkgname = 'eclipse'
    elif pkgname == 'software-center':
        pkgname = 'ubuntu-software-center'
    elif pkgname == "sogoupinyin":
        pkgname = "fcitx-ui-sogou-qimpanel"
    elif pkgname == "mathwar":
        pkgname = "MathWar"

    fd = os.popen('find /usr/share/applications/ -name "%s.desktop" | xargs grep "Exec"' %pkgname)
    exc = fd.read()
    fd.close()

    command = ['']
    # 截取运行指令部分
    if exc:
        command = re.findall('Exec=(.*)',exc)
    # 有些软件Exec后面会有%U %f等，进行过滤
    if re.findall(' ',command[0]):
        command = re.findall('(.*) ',command[0])
    #split the command to prevent the error: "OSError: [Errno 2] 没有那个文件或目录"
    fullcmd = command[0]
    if fullcmd:
        fullcmd = command[0].split()
    return fullcmd

def run_app(pkgname):
    cmd = get_run_command(pkgname)
    print("\n#####run_app:",cmd)
    p = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=False)

def run_appa():
    p = subprocess.Popen(["eog", "/home/shine/Downloads/009-01.png"], stdin = subprocess.PIPE, stdout = subprocess.PIPE, stderr = subprocess.PIPE, shell = False)

def judge_app_run_or_not(pkgname):
    result = 0
    cmd = get_run_command(pkgname)
    if cmd[0] is not None:
        cmd = 'pgrep -f ' + cmd[0] + ' | wc -l'
        ps = os.popen(cmd)
        result = int(ps.read().replace('/n', ''))
        ps.close()
    return result

def main():
    run_appa()

if __name__ == '__main__':
    main()
