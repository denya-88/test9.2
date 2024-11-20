import asyncio

# Функция для мигания светодиода
async def blink_led(led_name, delay):
    while True:
        print(f"{led_name} ВКЛЮЧЕН")
        await asyncio.sleep(delay)  # Эмулируем задержку FreeRTOS
        print(f"{led_name} ВЫКЛЮЧЕН")
        await asyncio.sleep(delay)

# Основная программа
async def main():
    # Создаем две задачи (аналог задач в FreeRTOS)
    task1 = asyncio.create_task(blink_led("Светодиод 1", 1))  # Мигание каждые 1 секунду
    task2 = asyncio.create_task(blink_led("Светодиод 2", 0.5))  # Мигание каждые 0.5 секунды

    # Ожидание завершения задач
    await asyncio.gather(task1, task2)

# Запускаем asyncio event loop
asyncio.run(main())
