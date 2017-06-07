#!/usr/bin/env python
# coding: utf-8

import ConfigParser

if __name__ == '__main__':
    _conf_parser = ConfigParser()
    _conf_parser.read('conf1.ini')

    print _conf_parser.get("project","name")