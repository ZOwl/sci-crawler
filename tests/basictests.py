#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

"""

import re

from testify import *

class BasicTestCase(TestCase):

    @class_setup
    def init_the_variable(self):
        self.variable = 0

    @setup
    def increment_the_variable(self):
        self.variable += 1

    def test_the_variable(self):
        assert_equal(self.variable, 1)

    def test_extract_sid(self):
        url = "http://apps.webofknowledge.com/WOS_GeneralSearch_input.do?product=WOS&SID=AAS1234123S&search_mode=GeneralSearch"
        m = re.search('SID=(.+)&', url)
        assert_equal("AAS1234123S", m.group(1))

    def test_replace_cr(self):
        s = "abc\n\ndef\nghi\n\njk'View Journal Information'l\n\nm'View Journal Information'n\nnopq"
        assert_equal(
                "abc\ndef ghi\njkl\nmn nopq",
                re.sub("'View Journal Information'", '',
                    re.sub('\n{2}', '\n',
                        re.sub('([^\n])(\n)([^\n])', r'\1 \3', s)
                        )
                    )
                )


    @teardown
    def decrement_the_variable(self):
        self.variable -= 1

    @class_teardown
    def get_rid_of_the_variable(self):
        self.variable = None

if __name__ == "__main__":
    run()

# vi: ft=python:tw=0:ts=4:sw=4

