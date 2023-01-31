# url = "https://speed.hetzner.de/100MB.bin"

import urllib.request
import sys


def progress_bar(progress, total):
    percent = progress / float(total)
    bar = "#" * int(percent * 50) + '-' * (50 - int(percent * 50))
    print(f"\r|{bar}| {100 * percent:.2f}%", end="\r")


def progress_hook(blocknum, bs, size):
    progress_bar(blocknum, size / bs)


def download_url(url, output_path):
    urllib.request.urlretrieve(url, filename=output_path, reporthook=progress_hook)


url = sys.argv[1]

download_url(url, url.split('/')[-1])
