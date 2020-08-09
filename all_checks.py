#!/usr/bin/env python3
import os
import sys
import shutil

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
def main():
     if check_reboot():
          print("Pending Reboot")
          sys.exit(1)
     if check_disk_full("/",2,10):
         print("Disk is full")
         sys.exit(1)
     print("Everything is OK.")
     sys.exit(0)
     #added line
main()
