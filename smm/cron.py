# from apscheduler.schedulers.background import BackgroundScheduler
# from datetime import datetime
#
#
# def my_task():
#     scheduler = BackgroundScheduler()
#     scheduler.add_job(my_task, 'interval', hourse=24)
#
#     scheduler.start()  # запуск задачи
#     print("Задача выполняется ", datetime.now())
#
#     scheduler.shutdown()  # остановка задачи
#

# import winioctlcon
# import os
#
# drive = 'C:'
# handle = os.open(drive, os.O_RDONLY | os.O_BINARY)
# ioctl = winioctlcon.IOCTL_DISK_GET_LENGTH_INFO
# buf = winioctlcon.STORAGE_DEVICE_DESCRIPTOR()
# winioctlcon.DeviceIoControl(handle, ioctl, None, 0, buf, len(buf))
# os.close(handle)
