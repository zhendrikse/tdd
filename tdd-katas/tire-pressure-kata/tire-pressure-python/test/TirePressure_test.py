import unittest

from alarm import Alarm
from sensor import Sensor

def get_too_high_tire_pressure(self):
  return 21

Sensor.pop_next_pressure_psi_value = get_too_high_tire_pressure

class AlarmTest(unittest.TestCase):

    def test_alarm_is_off_by_default(self):
        alarm = Alarm()
        # alarm._sensor.pop_next_pressure_psi_value = get_too_high_tire_pressure
        alarm.check()
        assert alarm.is_alarm_on