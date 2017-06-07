#!/usr/bin/env python
# -*- coding: utf-8 -*-
# P85   actually the book use python3, now here use python2
spam = {'name': 'Pooka', 'age': 5}
spam.setdefault('color', 'black')
print spam
print '======================='
spam.setdefault('color', 'white')
print spam