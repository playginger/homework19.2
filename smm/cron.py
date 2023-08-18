from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime, timedelta


# def my_task():
#     scheduler = BackgroundScheduler()
#     scheduler.add_job(my_task, 'interval', hourse=24)
#
#     scheduler.start()  # запуск задачи
#     print("Задача выполняется ", datetime.now())
#
#     scheduler.shutdown()  # остановка задачи

def my_task():
    print("Задача выполняется", datetime.now())


def add_job(send_time, interval, status):
    # Проверка валидности аргументов
    if interval.lower() not in ["день", "неделя", "месяц"]:
        print("Ошибка: Неверная периодичность. Допустимые значения: день, неделя, месяц.")
        return

    if status.lower() not in ["завершена", "создана", "запущена"]:
        print("Ошибка: Неверный статус рассылки. Допустимые значения: завершена, создана, запущена.")
        return

    # Определяем временной интервал выполнения задачи
    if interval.lower() == "день":
        delta = timedelta(days=1)
    elif interval.lower() == "неделя":
        delta = timedelta(weeks=1)
    elif interval.lower() == "месяц":
        delta = timedelta(days=30)  # Приблизительное значение для месяца

    next_send_time = datetime.now().replace(hour=send_time.hour, minute=send_time.minute, second=send_time.second)
    while next_send_time < datetime.now():
        next_send_time += delta

    # Запускаем задачу с указанными параметрами
    scheduler.add_job(my_task, 'date', run_date=next_send_time)
    print(
        f"Задача расписания добавлена: Время рассылки - {next_send_time}, Периодичность - {interval}, Статус - {status}")


scheduler = BackgroundScheduler()

try:
    send_time = datetime.now() + timedelta(seconds=10)  # Предполагаемое время первой рассылки (10 секунд для примера)
    interval = "день"  # Периодичность рассылки
    status = "создана"  # Статус рассылки

    add_job(send_time, interval, status)
    scheduler.start()  # Запуск задачи

    while True:
        pass  # Добавьте свой код здесь, если требуется

except KeyboardInterrupt:
    print("Остановка задачи...")
    scheduler.shutdown()  # Останавливаем задачу перед выходом
