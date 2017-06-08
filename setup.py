#========================================
#    author: Changlong.Zang
#      mail: zclongpop123@163.com
#      time: Thu Jun 08 12:30:17 2017
#========================================
import os, re, time, shutil
from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize
#--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
tm = time.localtime()
PYD_POST_FIX = '{0:0>4d}{1:0>2d}{2:0>2d}{3:0>2d}{4:0>2d}'.format(tm.tm_year, tm.tm_mon, tm.tm_mday, tm.tm_hour, tm.tm_min)

def func(path):
    '''
    '''
    for pt, ds, fs in os.walk(path):

        #- make current dir to this folder
        os.chdir(pt)

        #- build each python file
        for f in fs:
            if not re.search('\.py$',  f):
                continue

            if re.match('setup.py',    f):
                continue

            if re.match('__init__.py', f):
                continue

            if re.search('_rc.py',     f):
                continue

            #- Copy python file to build tag
            origin_name = os.path.splitext(f)[0]
            build_name  = '{0}_{1}'.format(origin_name, PYD_POST_FIX)
            build_file  = '{0}.py'.format(build_name)
            shutil.copy(f, build_file)

            #- build pyd
            extensions = [Extension(build_name, [ build_file ], include_dirs=[])]
            setup(name=build_name, ext_modules=cythonize(extensions))

            #- clean up delete unused files
            for ext in ('c', 'py', 'pyc'):
                delete_file = '{0}.{1}'.format(build_name, ext)
                os.path.isfile(delete_file) and os.remove(delete_file)

            os.path.isfile('{0}.pyc'.format(origin_name)) and os.remove('{0}.pyc'.format(origin_name))

            #- make py and pyd relative
            shutil.copy(f, f+'1')
            with open(f, 'w') as fw:
                fw.write('from {0} import *'.format(build_name))



if __name__ == '__main__':
    path = os.getcwd()
    func(path)
