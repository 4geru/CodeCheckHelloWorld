#!/usr/bin/env python
# -*- coding: utf-8 -*-

def main(argv):
  # このコードは引数と標準出力を用いたサンプルコードです。
  # このコードは好きなように編集・削除してもらって構いません。
  # ---
  # This is a sample code to use arguments and outputs.
  # Edit and remove this code as you like.
  if len(argv) != 0 :
    print("Hello {0}!".format(argv[0]))
  else :
    print("Hello!")
