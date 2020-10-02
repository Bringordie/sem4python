import requests  # https://requests.readthedocs.io/en/master/
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import ProcessPoolExecutor
from urllib.parse import urlparse
import multiprocessing


class Ex6():
    def __init__(self, url_list):
        self.url_list = url_list
        self.filenames = {}

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n < len(self.url_list):
            result = self.url_list[self.n]
            self.n += 1
            return result
        else:
            raise StopIteration

    def download(self, url, filepath):
        res = requests.get(url)
        try:
            if res.status_code == 200:
                with open(filepath, 'wb') as fd:
                    for chunk in res.iter_content(chunk_size=1024):
                        fd.write(chunk)
                    print('File downloaded')

            elif res.status_code == 404:
                raise FileNotFoundError
        except FileNotFoundError as error:
            print('Error: ' + repr(error))

    def download_thread(self, url):
        res = requests.get(url)
        bookId = url.split('/')[-1]
        filepath = f'data/{bookId}'
        try:
            if res.ok:
                with open(filepath, 'wb') as f:
                    for chunk in res.iter_content(chunk_size=1024):
                        f.write(chunk)
                    print(f'{bookId} downloaded to {filepath}...')
                    return filepath

            elif res.status_code == 404:
                raise FileNotFoundError
        except FileNotFoundError as error:
            print('Error: ' + repr(error))

    def multi_download(self):
        with ThreadPoolExecutor(5) as ex:
            res = ex.map(self.download_thread, self.url_list)
            self.filenames = list(res)
        print(self.filenames)

    def urllist_generator(self):
        for url in self.url_list:
            print(url)

    def avg_vowels(self, text):
        vowels = set("AEIOUaeiou")
        cons = set("bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ")
        countV = 0
        countC = 0
        with open(text, 'r', encoding='utf8') as file_object:
            contents = file_object.read()
        for c in contents:
            if c in vowels:
                countV += 1
            elif c in cons:
                countC += 1
        average = "%.2f" % round(countV/countC*100, 2)
        return (text, float(average))
        # return (text, '{} % average vowels'.format(average))

    def hardest_read(self):
        workers = multiprocessing.cpu_count()
        textList = []  # self.url_list
        for url in self.url_list:
            textList.append('data/'+url.split('/')[-1])
        with ProcessPoolExecutor(workers) as ex:
            results = ex.map(self.avg_vowels, textList)
        return sorted(results, key=lambda x: x[1], reverse=True)


if __name__ == '__main__':

    urlList = ['https://www.gutenberg.org/files/1342/1342-0.txt',
               'https://www.gutenberg.org/files/11/11-0.txt',
               'http://www.gutenberg.org/cache/epub/1497/pg1497.txt',
               'https://www.gutenberg.org/files/25344/25344-0.txt',
               'https://www.gutenberg.org/files/1250/1250-0.txt',
               'https://www.gutenberg.org/files/1952/1952-0.txt',
               'http://www.gutenberg.org/cache/epub/1232/pg1232.txt',
               'https://www.gutenberg.org/files/84/84-0.txt',
               'https://www.gutenberg.org/files/98/98-0.txt',
               'http://www.gutenberg.org/cache/epub/2542/pg2542.txt'
               ]

# EX 2
    # Ex6.download(
    #     '', 'http://www.gutenberg.org/files/2701/2701-0.txt', 'moby_dick.txt')

# EX 3
    # thread_download = Ex6(urlList)
    # thread_download.multi_download()

# EX 4-5
    # for books in Ex6(urlList):
    #     print(books)

# EX 6
    # generator = Ex6(urlList)
    # generator.urllist_generator()

# EX 7
    # print(Ex6.avg_vowels('', 'data/11-0.txt'))

# EX 8
    # urlList2 = ['data/1342-0.txt',
    #            'data/11-0.txt',
    #            'data/pg1497.txt',
    #            'data/25344-0.txt',
    #            'data/1250-0.txt',
    #            'data/1952-0.txt',
    #            'data/pg1232.txt',
    #            'data/84-0.txt',
    #            'data/98-0.txt',
    #            'data/pg2542.txt'
    #            ]
    # ex6cpu = Ex6(urlList)
    # print(ex6cpu.hardest_read())

# EX1
# 1 init(self, url_list)
# 2 download(url,filename) raises NotFoundException when url returns 404
# 3 multi_download() uses threads to download multiple urls as text and stores filenames as a property
# 4 iter() returns an iterator
# 5 next() returns the next filename (and stops when there are no more)
# 6 urllist_generator() returns a generator to loop through the urls
# 7 avg_vowels(text) - a rough estimate on readability returns average number of vowels in the words of the text
# 8 hardest_read() returns the filename of the text with the highest vowel score (use all the cpu cores on the computer for this work.
