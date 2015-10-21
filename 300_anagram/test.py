# -*- coding:utf-8 -*-
from unittest import TestCase
from yourtest import anagram


class AnagramTest(TestCase):
    def test_anagram(self):
        self.assertEqual(True, anagram('python', 'typhon'))
        self.assertEqual(True, anagram('heart', 'earth'))
        self.assertEqual(True, anagram('silent', 'listen'))
        self.assertEqual(True, anagram('William Shakespeare', 'I am a weakish speller'))
        self.assertEqual(True, anagram('Dormitory', 'Dirty room'))
        self.assertEqual(True, anagram('Astronomer', 'Moon starer'))
        self.assertEqual(True, anagram('Conversation', 'Voices rant on'))
