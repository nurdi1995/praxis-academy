import requests
import time
import asyncio
import aiohttp
import multiprocessing

#1. Synchronous Version

def download_site(url, session):
    with session.get(url) as response:
        print(f"Read {len(response.content)} from {url}")


def download_all_sites(sites):
    with requests.Session() as session:
        for url in sites:
            download_site(url, session)


if __name__ == "__main__":
    sites = [
        "https://www.jython.org",
        "http://olympus.realpython.org/dice",
    ] * 80 
    start_time = time.time()
    download_all_sites(sites)
    duration = time.time() - start_time
    print(f"Downloaded {len(sites)} in {duration} seconds")

# 2. threading Version

thread_local = thread_local()

def get_session():
    if not hasattr(thread_local,"session"):
        thread_local.session = requests.sessions()
    return thread_local.session

def download_site(url):
    session = get_session()
    with session.get(url) as response:
        print(f"Read {len(response.content)} from {url}")

def download_all_sites(sites):
    with concurrent.futures.ThreadpoolExecutor(max_workers=5) as executor:
        executor.map(download_site, sites)

if __name__ == "__main__":
    sites = [
        "https://www.jython.org",
        "http://olympus.realpython.org/dice",
    ] * 80
    start_time = time.time()
    download_all_sites(sites)
    duration = time.time() - start_time
    print(f"Download {len(sites)} in {duration} seconds")


# 3. multiprocessing Version
session = None

def set_global_session():
    global session
    if not session:
        session = requests.sessions()

def download_site(url):
    with session.get(url) as response:
        name = multiprocessing.current_process().name
        print(f"{name}: Read {len(response.content)} from {url}")

def download_all_sites(sites):
    with multiprocessing.poll(initializer=set_global_session) as poll:
        pool.map(download_site, sites)


if __name__ == "__main__":
    sites = [
         "https://www.jython.org",
         "http://olympus.realpython.org/dice",
    ] * 80
    start_time = time.time()
    download_all_sites(sites)
    duration = time.time() - start_time
    print(f"Downloaded {len(sites)} in {duration} seconds")


#4. CPU-Bound Synchronous Version

def cpu_bound(number):
    return sum(i * i for i in range (number))

def find_sums(numbers):
    for numbers in numbers:
        cpu_bound(number)

if __name__ == "__main__":
     numbers = [5_000_000 + x for x in range(20)]

    start_time=time.time()
    find_sums(numbers)
    duration = time.time() - start_time
    print(f"Duration {duration} seconds")






