import unittest
from datetime import datetime

from run import calculate_overall
from schema.schema import RequestSchema


class TestOverallCalculation(unittest.TestCase):
    def setUp(self) -> None:
        self.test_data = RequestSchema().load({
            "rate": {
                "energy": 0.3,
                "time": 2,
                "transaction": 1
            },
            "cdr": {
                "meterStart": 1204307,
                "timestampStart": "2021-04-05T10:04:00Z",
                "meterStop": 1215230,
                "timestampStop": "2021-04-05T11:27:00Z"
            }
        })

    def test_overall_calculation(self):
        energy_fee, time, service_fee, overall = calculate_overall(self.test_data)
        self.assertEqual(round(overall, 2), 7.04)
        self.assertEqual(round(energy_fee, 3), 3.277)
        self.assertEqual(round(time, 3), 2.767)
        self.assertEqual(service_fee, 1)


if __name__ == '__main__':
    unittest.main()
