import os
import tarfile


def extract(filename):
    print('Extracting {}...'.format(filename))
    tar = tarfile.open(filename, 'r')
    tar.extractall('data')
    tar.close()


if __name__ == "__main__":
    if not os.path.isdir('data/data_thuyg20'):
        extract('data/data_thuyg20.tar.gz')
