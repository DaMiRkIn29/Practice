import asyncio
import time


async def start_strongman(name, power):
    print(f"Силач {name} начал соревнования")

    for ball_number in range(1, 6):
        await asyncio.sleep(1/power)
        print(f"Силач {name} поднял {ball_number} шар")

    print(f"Силач {name} закончил соревнования")

async def start_tournament():
    task1 = asyncio.create_task(start_strongman("Вася", 2))
    task2 = asyncio.create_task(start_strongman("Петя", 3))
    task3 = asyncio.create_task(start_strongman("Михаил", 4))

    await task1
    await task2
    await task3

if __name__ == "__main__":
    asyncio.run(start_tournament())
