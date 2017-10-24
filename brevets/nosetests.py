"""
Nose tests for acp_times.py
"""

from acp_times import open_time, close_time
import arrow
from flask.tools import assert_raises


def first_section_open():
    start_time = arrow.now()
    assert open_time(60, 200, start_time) == start_time.shift(hours=1, minutes=46).isoformat()
    assert open_time(120, 200, start_time) == start_time.shift(hours=3,minutes=32).isoformat()
    assert open_time(200, 200, start_time) == start_time.shift(hours= 5, minutes=53).isoformat()

def first_section_close():
    start_time = arrow.now()
    assert close_time(60, 200, start_time) == start_time.shift(hours=4).isoformat()
    assert close_time(120, 200, start_time) == start_time.shift(hours=8).isoformat()

def second_section_open():
    start_time = arrow.now()
    assert open_time(200, 400, start_time) == start_time.shift(hours=5, minutes=53).isoformat()
    assert open_time(350, 400, start_time) == start_time.shift(hours=10, minutes=34).isoformat()
    assert open_time(400, 400, start_time) == start_time.shift(hours=12, minutes=8).isoformat()

def second_section_close():
    start_time = arrow.now()
    assert close_time(200, 400, start_time) == start_time.shift(hours=13, minutes=20).isoformat()
    assert close_time(350, 400, start_time) == start_time.shift(hours=23, minutes=20).isoformat()


def third_section_open():
    start_time = arrow.now()
    assert open_time(400, 600, start_time) == start_time.shift(hours=12, minutes=8).isoformat()
    assert open_time(550, 600, start_time) == start_time.shift(hours=17, minutes=8).isoformat()
    assert open_time(600, 600, start_time) == start_time.shift(hours=18, minutes=48).isoformat()


def third_section_close():
    start_time = arrow.now()
    assert close_time(400, 600, start_time) == start_time.shift(hours=26, minutes=40).isoformat()
    assert close_time(550, 600, start_time) == start_time.shift(hours=36, minutes=40).isoformat()

def test_fourth_section_time():
    start_time = arrow.now()
    assert open_time(600, 1000, start_time) == start_time.shift(hours=18, minutes=48).isoformat()
    assert open_time(800, 1000, start_time) == start_time.shift(hours=25, minutes=57).isoformat()
    assert close_time(600, 1000, start_time) == start_time.shift(hours=40).isoformat()
    assert close_time(800, 1000, start_time) == start_time.shift(hours=57, minutes=30).isoformat()


def fifth_section_open():
    start_time = arrow.now()
    assert open_time(1000, 1000, start_time) == start_time.shift(hours=33, minutes=5).isoformat()
    assert open_time(1150, 1000, start_time) == start_time.shift(hours=33, minutes=5).isoformat()
    assert open_time(1200, 1000, start_time) == start_time.shift(hours=33, minutes=5).isoformat()


def open_edge_cases():
    start_time = arrow.now()
    assert open_time(0, 200, start_time) == start_time.shift(hours=0, minutes=0).isoformat()


def close_edge_cases():
    start_time = arrow.now()
    assert close_time(0, 200, start_time) == start_time.shift(hours=1).isoformat()
    assert close_time(200, 200, start_time) == start_time.shift(hours=13, minutes=30).isoformat()
    assert close_time(205, 200, start_time) == start_time.shift(hours=13, minutes=30).isoformat()
    assert close_time(300, 300, start_time) == start_time.shift(hours=20).isoformat()
    assert close_time(305, 300, start_time) == start_time.shift(hours=20).isoformat()
    assert close_time(400, 400, start_time) == start_time.shift(hours=27).isoformat()
    assert close_time(410, 400, start_time) == start_time.shift(hours=27).isoformat()
    assert close_time(600, 600, start_time) == start_time.shift(hours=40).isoformat()
    assert close_time(620, 600, start_time) == start_time.shift(hours=40).isoformat()
    assert close_time(1000, 1000, start_time) == start_time.shift(hours=75).isoformat()
    assert close_time(1100, 1000, start_time) == start_time.shift(hours=75).isoformat()


def open_too_far():
    start_time = arrow.now()
    assert_raise(ValueError, open_time, 300, 200, start_time)
    assert_raise(ValueError, open_time, 1300, 1000, start_time)
    assert_raise(ValueError, open_time, 1300, 1000, start_time)
    assert_raise(ValueError, open_time, 500, 400, start_time)
    assert_raise(ValueError, open_time, 800, 600, start_time)
    assert_raise(ValueError, open_time, 1300, 1000, start_time)

def close_too_far():
    start_time = arrow.now()
    assert_raise(ValueError, close_time, 300, 200, start_time)
    assert_raise(ValueError, close_time, 500, 400, start_time)
    assert_raise(ValueError, close_time, 800, 600, start_time)
    assert_raise(ValueError, close_time, 1300, 1000, start_time)