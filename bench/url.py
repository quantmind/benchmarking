from timeit import timeit

from common import nice


def benchmark():

    nice(
        'urlparse  ',
        timeit('urlparse("https://github.com/quantmind/pulsar")',
               'from urllib.parse import urlparse')
    )
    nice(
        'httptools ',
        timeit('parse_url(b"https://github.com/quantmind/pulsar")',
               'from httptools import parse_url')
    )
    nice(
        'yarl      ',
        timeit('URL("https://github.com/quantmind/pulsar")',
               'from yarl import URL')
    )



if __name__ == '__main__':
    benchmark()
