# minitask 7
import asyncio
import time

# Change the code in the main function so that the tasks run concurrently
# (stand water, wash cups, boil water), so that the output is something like:
#   boiling kettle starting
#   cleaning cups starting
#   cleaning cups is done
#   boiling kettle is done
#   Executed in 3.02 seconds.


async def perform_task(duration, task_name):
    print(task_name, "starting")
    await asyncio.sleep(duration)
    print(task_name, "is done")


async def main():
    t1 = perform_task(3, "boiling kettle")
    t2 = perform_task(2, "cleaning cups")
    await asyncio.gather(t1, t2)


s = time.perf_counter()
asyncio.run(main())
elapsed = time.perf_counter() - s
print(f"Executed in {elapsed:0.2f} seconds.")
