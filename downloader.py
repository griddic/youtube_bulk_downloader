import re
from multiprocessing.pool import Pool

import pytube


def video_id(link):
    direct_pattern = r'.*/(\w+)$'
    if m := re.match(direct_pattern, link):
        return m.group(1)
    long_pattern = r'.*[?&]v=(\w+)'
    if m := re.match(long_pattern, link):
        return m.group(1)
    return None


def download(link):
    video = pytube.YouTube(link)
    id_ = video.video_id
    print(f'Downloading: {link} with id: {id_}')
    file_path = pytube.YouTube(link).streams.get_highest_resolution().download('downloads', filename_prefix=f'{id_} ')
    print(f'{link} -> {file_path}')


def main():
    with open('video_list.txt') as in_:
        links = [l.strip() for l in in_]
    print(links)
    pool = Pool(10)
    pool.map(download, links)


if __name__ == '__main__':
    main()
