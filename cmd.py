#!/bin/env python
#coding=utf-8

from optparse import OptionParser
import os

options = {}
functionList = ["list","add","remove"]

def init_options():
  global options
  global functionList
  parser = OptionParser()
  parser.add_option("-o","--opt",dest="opt",help="optiont to port , <list,add,remove>",metavar="option to this file",default="list")
  (options,args) = parser.parse_args()
  if options.opt in functionList:
    f = getattr(OptList(),options.opt)
    f(args)
  else:
    print "error option"

class OptList():

    def list(self,args):
        pass

    def add(self,args):
        pass

    def remove(self,args):
        pass

    def _run_shell(self,cmd):
        return os.popen(cmd).read()


if __name__ == "__main__" :
    init_options()

