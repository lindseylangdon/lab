import pytest
from classes import*

def test_power(self):
    assert self.tv.__str__() == 'TV status: Is on = False, Channel = 0, Volume = 0'
    self.tv.power()
    assert self.tv.__str__() == 'TV status: Is on = True, Channel = 0, Volume = 0'

def test_channel_up(self):
    assert self.channel_up(2) == 3
    assert self.channel_up(3) == 0

def test_channel_down(self):
    assert self.channel_down(2) == 1
    assert self.channel_down(0) == 3

def test_volume_up(self):
    assert self.volume_up(1) == 2
    assert self.volume_up(2) == 2

def test_volume_down(self):
    assert self.volume_down(1) == 0
    assert self.volume_down(0) == 0