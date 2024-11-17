# -*- coding: utf-8 -*-
#
# You need to fill the blank line at the end of the source file.
#
from pydub import AudioSegment 
from gtts import gTTS
import os
import time
import sys

#print ('argument list', sys.argv)
name = sys.argv[1]
print ("Hello {}. How are you?".format(name))