#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time     : 2018/2/21下午1:32
# @Author   : Saseny Zhou
# @Site     : 
# @File     : return_code.py
# @Software : PyCharm


return_code = {
    "1": "TASK HAS QUEUED",
    "2": "TASK HAS BEEN SUBMITTED FOR PROCESSING",
    "3": "TASK HAS BEEN SUBMITTED",
    "4": "EXPORTS IN PROCESS OF GENERATION",
    "5": "EXPORTS FINISHED GENERATION",
    "6": "TASK FAILED",
    "7": "EXPORTS READY",
    "8": "TASK HAD AN ERROR AND NOTIFICATION HAS BEEN SENT",
    "9": "EXPORTS HAVE BEEN DOWNLOADED",
    "10": "TASK TIMEOUT",
    "11": "ERROR OCCURED WHILE MONITORING STATUS",
    "21": "TASK STATUS SUBMITTED TO SPARK -- for META DATA",
    "200": "SUBMIT REQUEST SUCCEED",
    "400": "SUBMIT REQUEST FAILED",
    "1000": "PROCESS DATA SUCCEED",
    "1001": "PROCESS DATA FAILED",
    "1002": "REQUEST TASK FAILED"
}

"""
message = "UNDOCUMENTED RETURN %s" % str(taskStatus)
"""

from functions.path import *
from functions.json_file import *


def unknown_code(code):
    message = "UNDOCUMENTED RETURN %s" % str(int(code))
    return message


def writer_code():
    write_json_file(return_code, os.path.join(resources, "code.json"))


writer_code()