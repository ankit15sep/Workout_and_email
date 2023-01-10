from subprocess import *
import time
Popen('python Papa/generate_random_exr_v7.py')
time.sleep(60)
Popen('python RuchiDi/generate_random_exr_v7_ruchiDi.py')
time.sleep(60)
Popen('python Janu/generate_random_exr-v7_Janu.py')
