#!/usr/bin/python2.4
# -*- coding: utf-8 -*-
#
# Copyright 2010 Google Inc. All Rights Reserved.

"""Simple command-line example for Translate.

Command-line application that translates
some text.
"""

__author__ = 'jcgregorio@google.com (Joe Gregorio)'

import gflags
import logging
import pprint
import sys

from apiclient.discovery import build
from apiclient.model import LoggingJsonModel


FLAGS = gflags.FLAGS
# Uncomment the next line to get very detailed logging
# httplib2.debuglevel = 4

# create logger
logger = logging.getLogger()
logger.setLevel(logging.INFO)


def main(argv):
  try:
    argv = FLAGS(argv)  # parse flags
  except gflags.FlagsError, e:
    print '%s\\nUsage: %s ARGS\\n%s' % (e, argv[0], FLAGS)
    sys.exit(1)

  service = build('translate', 'v2',
                  developerKey='AIzaSyDRRpR3GS1F1_jKNNM9HCNd2wJQyPG3oN0',
                  model=LoggingJsonModel())
  print service.translations().list(
      source='en',
      target='fr',
      q=['flower', 'car']
    ).execute()

if __name__ == '__main__':
  main(sys.argv)
