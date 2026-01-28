# inventory.py
# Inventário simples (Cisco IOS / Arista EOS) para Netmiko
import os
from dotenv import load_dotenv

load_dotenv()

DEVICES = [
    {
        "device_type": "cisco_ios",
        "host": "192.168.2.10",
        "username": os.getenv("CISCO_USERNAME"),
        "password": os.getenv("CISCO_PASSWORD"),
        "device_name" : "Multilayer_Switch",
        "vendor": "Cisco"
    },
    {
        "device_type": "cisco_ios",
        "host": "192.168.2.11",
        "username": os.getenv("CISCO_USERNAME"),
        "password": os.getenv("CISCO_PASSWORD"),
        "device_name" : "SW1",
        "vendor": "Cisco"
    },
    {
        "device_type": "cisco_ios",
        "host": "192.168.2.12",
        "username": os.getenv("CISCO_USERNAME"),
        "password": os.getenv("CISCO_PASSWORD"),
        "device_name" : "SW2",
        "vendor": "Cisco"
    },
    {
        "device_type": "cisco_ios",
        "host": "192.168.2.13",
        "username": os.getenv("CISCO_USERNAME"),
        "password": os.getenv("CISCO_PASSWORD"),
        "device_name" : "SW3",
        "vendor": "Cisco"
    },
    {
        "device_type": "cisco_ios",
        "host": "192.168.2.14",
        "username": os.getenv("CISCO_USERNAME"),
        "password": os.getenv("CISCO_PASSWORD"),
        "device_name" : "SW4",
        "vendor": "Cisco"
   },
    {
        "device_type": "cisco_ios",
        "host": "192.168.2.15",
        "username": os.getenv("CISCO_USERNAME"),
        "password": os.getenv("CISCO_PASSWORD"),
        "device_name" : "SW5",
        "vendor": "Cisco"
    },
    {
        "device_type": "arista_eos",
        "host": "192.168.2.16",
        "username": os.getenv("ARISTA_USERNAME"),
        "password": os.getenv("ARISTA_PASSWORD"),
        "device_name" : "SW6",
        "vendor": "Arista"
    },
    {
        "device_type": "arista_eos",
        "host": "192.168.2.17",
        "username": os.getenv("ARISTA_USERNAME"),
        "password": os.getenv("ARISTA_PASSWORD"),
        "device_name" : "SW7",
        "vendor": "Arista"
    },
        {
        "device_type": "arista_eos",
        "host": "192.168.2.18",
        "username": os.getenv("ARISTA_USERNAME"),
        "password": os.getenv("ARISTA_PASSWORD"),
        "secret": os.getenv("ARISTA_PASSWORD"),
        "device_name" : "SW8",
        "vendor": "Arista"
    },
        {
        "device_type": "arista_eos",
        "host": "192.168.2.19",
        "username": os.getenv("ARISTA_USERNAME"),
        "password": os.getenv("ARISTA_PASSWORD"),
        "secret": os.getenv("ARISTA_PASSWORD"),
        "device_name" : "SW9",
        "vendor": "Arista"
    },
        {
        "device_type": "arista_eos",
        "host": "192.168.2.20",
        "username": os.getenv("ARISTA_USERNAME"),
        "password": os.getenv("ARISTA_PASSWORD"),
        "secret": os.getenv("ARISTA_PASSWORD"),
        "device_name" : "SW10",
        "vendor": "Arista"
    },
]

