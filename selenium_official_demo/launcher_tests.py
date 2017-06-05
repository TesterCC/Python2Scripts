#!/usr/bin/env python
# coding:utf-8

import os

import pytest


import os

import pytest


def test_launch(driver):
    assert driver.capabilities['browserName'] == 'safari'


def test_launch_with_invalid_executable_path_raises_exception(driver_class):
    path = '/this/path/should/never/exist'
    assert not os.path.exists(path)
    with pytest.raises(Exception) as e:
        driver_class(executable_path=path)
    assert 'SafariDriver requires Safari 10 on OSX El Capitan' in str(e)


class TestTechnologyPreview(object):

    @pytest.fixture
    def driver_kwargs(self):
        path = '/Applications/Safari Technology Preview.app/Contents/MacOS/safaridriver'
        assert os.path.exists(path), 'Safari Technology Preview required! Download it from https://developer.apple.com/safari/technology-preview/'
        return {'executable_path': path}

    def test_launch(self, driver):
        assert driver.capabilities['browserName'] == 'safari'