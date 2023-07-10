import unittest

from alarm import Alarm

class AlarmTest(unittest.TestCase):

    def test_alarm_is_off_by_default(self):
        alarm = Alarm()
        # Tire pressure values are unpredictable, so we cannot
        # use it deterministically in our test(s)
        # 
        # alarm.check()
        assert not alarm.is_alarm_on