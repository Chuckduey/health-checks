#!/usr/bin/env python3
import os
import sys
import shutil
import socket
#  
def check_no_network():
    """Returns True if it fails to resolve the Google URL, False otherwise"""
    try:
        socket.gethostbyname("www.google.com")
        return False
    except:
        return True

def check_reboot():
    """Returns True if the computer has a pending reboot."""
    return os.path.exists("/run/reboot-required")
def check_disk_full(disk, min_gb, min_percent):
    """Returns True if ther isn't enough disk space, False otherwise"""
    du = shutil.disk_usage(disk)
    percent_free = 100 *du.free/du.total
    gb_free = du.free/2**30
    if percent_free < min_percent or gb_free < min_gb:
        return True
    return False
def check_root_full():
    """Returns True id root partition is full, false otherwise"""
    return check_disk_full("/",2,10)
def main():
     check = [
            (check_reboot, "Pending Reboot"),
            (check_root_full, "Root partition full"),
            (check_no_network, "No Internet Connection")
            ]
     everything_ok = True
     for check, msg in check:
        if check():
            print(msg)
            everything_ok = False
     if not everything_ok:
         sys.exit(1)
     print("Everything is OK.")
     sys.exit(0)
     #added line
main()
