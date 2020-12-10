from setuptools import setup, find_packages
from os import walk, listdir
from os.path import join, normpath, isfile

def recursive_list_dir(path):
    listing=[]
    for x in walk(path):
        if isfile(x[0]):
            listing.append(x[0].split(path+'/')[1])
        for y in listdir(x[0]):
            z = normpath(join(x[0],y))
            if isfile(z):
                listing.append(z.split(path+'/')[1])
    return listing

param = {
    'package_data':{'':recursive_list_dir('tests')},
    'packages': find_packages(),
    'include_package_data': True,
    'scripts': ['main.py','tests.py'],
    'zip_safe': True,
    #'test_suite': 'test_suite',
    #'tests_require': ['nose'],
}

setup(**param)