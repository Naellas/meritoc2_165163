import asyncio
import aiohttp
import time

print("==========================================================================")
print("1. Write a Python program that creates an asynchronous function to print 'Python Exercises!' with a two second delay.")
print("==========================================================================")

async def print_message():
    await asyncio.sleep(2)
    print("Python Exercises!")

asyncio.run(print_message())

print("==========================================================================")
print("2. Write a Python program that creates three asynchronous functions and displays their respective names with different delays (1 second, 2 seconds, and 3 seconds).")
print("==========================================================================")

async def task_1():
    await asyncio.sleep(1)
    print("Task 1")

async def task_2():
    await asyncio.sleep(2)
    print("Task 2")

async def task_3():
    await asyncio.sleep(3)
    print("Task 3")

async def run_tasks():
    await asyncio.gather(task_1(), task_2(), task_3())

asyncio.run(run_tasks())

print("==========================================================================")
print("3. Write a Python program that creates an asyncio event loop and runs a coroutine that prints numbers from 1 to 7 with a delay of 1 second each.")
print("==========================================================================")

async def print_numbers():
    for i in range(1, 8):
        print(i)
        await asyncio.sleep(1)

asyncio.run(print_numbers())

print("==========================================================================")
print("4. Write a Python program that implements a coroutine to fetch data from two different URLs simultaneously using the 'aiohttp' library.")
print("==========================================================================")

async def fetch_url(session, url):
    async with session.get(url) as response:
        return await response.text()

async def fetch_data():
    urls = ["https://jsonplaceholder.typicode.com/posts/1", "https://jsonplaceholder.typicode.com/posts/2"]
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_url(session, url) for url in urls]
        responses = await asyncio.gather(*tasks)
        for response in responses:
            print(response[:100])  # Print first 100 characters of each response

asyncio.run(fetch_data())

print("==========================================================================")
print("5. Write a Python program that runs multiple asynchronous tasks concurrently using asyncio.gather() and measures the time taken.")
print("==========================================================================")

async def async_task(name, delay):
    await asyncio.sleep(delay)
    print(f"Task {name} completed")

async def measure_time():
    start = time.time()
    await asyncio.gather(async_task("A", 2), async_task("B", 3), async_task("C", 1))
    end = time.time()
    print(f"Total time taken: {end - start} seconds")

asyncio.run(measure_time())

print("==========================================================================")
print("6. Write a Python program to create a coroutine that simulates a time-consuming task and use asyncio.CancelledError to handle task cancellation.")
print("==========================================================================")

async def long_running_task():
    try:
        print("Task started")
        await asyncio.sleep(10)
        print("Task completed")
    except asyncio.CancelledError:
        print("Task was cancelled")

async def cancel_task():
    task = asyncio.create_task(long_running_task())
    await asyncio.sleep(2)
    task.cancel()
    try:
        await task
    except asyncio.CancelledError:
        print("Caught task cancellation")

asyncio.run(cancel_task())

print("==========================================================================")
print("7. Write a Python program that implements a timeout for an asynchronous operation using asyncio.wait_for().")
print("==========================================================================")

async def task_with_timeout():
    await asyncio.sleep(5)
    return "Task completed"

async def run_with_timeout():
    try:
        result = await asyncio.wait_for(task_with_timeout(), timeout=2)
        print(result)
    except asyncio.TimeoutError:
        print("Task timed out")

asyncio.run(run_with_timeout())

print("==========================================================================")
print("8. Write a Python program that uses asyncio queues to simulate a producer-consumer scenario with multiple producers and a single consumer.")
print("==========================================================================")

async def producer(queue, n):
    for x in range(n):
        await asyncio.sleep(1)
        item = f"Item {x}"
        await queue.put(item)
        print(f"Produced {item}")

async def consumer(queue):
    while True:
        item = await queue.get()
        if item is None:
            break
        print(f"Consumed {item}")
        queue.task_done()

async def run_producer_consumer():
    queue = asyncio.Queue()
    producers = [asyncio.create_task(producer(queue, 5)) for _ in range(2)]
    consumer_task = asyncio.create_task(consumer(queue))
    await asyncio.gather(*producers)
    await queue.put(None)  # Signal consumer to exit
    await consumer_task

asyncio.run(run_producer_consumer())