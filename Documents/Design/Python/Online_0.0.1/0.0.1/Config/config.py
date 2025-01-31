#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time     : 2018/3/8下午4:50
# @Author   : Saseny Zhou
# @Site     : 
# @File     : config.py
# @Software : PyCharm


main_config = {
    "url": "https://manufacturing.apple.com/",
    "backup-data": True,
    "time out": 100,
    "serial number read":
        {
            "rule": "C02[A-Z].{8}"
        },
    "product-station-command":
        {
            "J79A":
                {
                    "FACT":
                        {
                            "cmd-link": "command/FACT/FACT_FATP_Audit_V1.29.py",
                            "config": "command/FACT/FACT_config.json",
                            "explain": "/anaconda3/bin/python3",
                            "download":
                                {
                                    "special project name":
                                        {
                                            "whether": False,
                                            "changed": ""
                                        },
                                    "auditOnly": "Y",
                                    "overlay":
                                        [
                                            "1.14.51v041 - Audit"
                                        ],
                                    "station": "FACT",
                                    "project": "J79A",
                                    "frequency": "weekly",
                                    "radar number": "32173240",
                                    "form_start_time": 30,
                                    "special": False,
                                    "special sn list":
                                        [

                                        ]
                                }
                        },
                    "BUTTON":
                        {
                            "cmd-link": "command/BUTTON/Button_audit.py",
                            "config": "command/BUTTON/config.json",
                            "explain": "/anaconda3/bin/python3",
                            "download":
                                {
                                    "special project name": {
                                        "whether": False,
                                        "changed": ""
                                    },
                                    "auditOnly": "Y",
                                    "overlay": [
                                        "1.14.51v041 - Audit"
                                    ],
                                    "station": "BUTTON",
                                    "project": "J79A",
                                    "frequency": "weekly",
                                    "radar number": "32173240",
                                    "form_start_time": 30,
                                    "special": False,
                                    "special sn list":
                                        [

                                        ]
                                }
                        }
                },
            "J80A":
                {
                    "FACT":
                        {
                            "cmd-link": "command/FACT/FACT_FATP_Audit_V1.30.py",
                            "config": "command/FACT/FACT_config.json",
                            "explain": "/anaconda3/bin/python3",
                            "download":
                                {
                                    "special project name":
                                        {
                                            "whether": False,
                                            "changed": ""
                                        },
                                    "auditOnly": "Y",
                                    "overlay":
                                        [
                                            "1.14.51v034A"
                                        ],
                                    "station": "FACT",
                                    "project": "J80A",
                                    "frequency": "weekly",
                                    "radar number": "32173240",
                                    "form_start_time": 30,
                                    "special": False,
                                    "special sn list":
                                        [

                                        ]
                                }
                        },
                    "WIFI-BT-COND":
                        {
                            "cmd-link": "command/SMT_WiPas/QSMC_SMT_Wipas_audit_V1.5.21.py",
                            "config": "command/SMT_WiPas/config.json",
                            "explain": "/anaconda3/bin/python3",
                            "download":
                                {
                                    "special project name": {
                                        "whether": False,
                                        "changed": ""
                                    },
                                    "auditOnly": "Y",
                                    "overlay": [
                                        "5AAvP34-1.20"
                                    ],
                                    "station": "WIFI-BT-COND",
                                    "project": "J80A",
                                    "frequency": "weekly",
                                    "radar number": "32173240",
                                    "form_start_time": 30,
                                    "special": False,
                                    "special sn list":
                                        [

                                        ]
                                }
                        },
                    "WIFI-BT-COND-B":
                        {
                            "cmd-link": "command/SMT_WiPas/QSMC_SMT_Wipas_audit_V1.5.21.py",
                            "config": "command/SMT_WiPas/config.json",
                            "explain": "/anaconda3/bin/python3",
                            "download":
                                {
                                    "special project name": {
                                        "whether": False,
                                        "changed": ""
                                    },
                                    "auditOnly": "Y",
                                    "overlay": [
                                        "5AAvP34-1.20"
                                    ],
                                    "station": "WIFI-BT-COND-B",
                                    "project": "J80A",
                                    "frequency": "weekly",
                                    "radar number": "32173240",
                                    "form_start_time": 30,
                                    "special": False,
                                    "special sn list":
                                        [

                                        ]
                                }
                        }
                }
        }
}

from Path.path import *


def writer_config():
    collectLogs.logger.info("Write New Config File: {}".format(os.path.join(resources, "config.json")))
    write_json_file(main_config, os.path.join(resources, "config.json"))

# writer_config()
