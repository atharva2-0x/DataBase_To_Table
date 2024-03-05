
import unittest

from mapping_2 import map_consumer_data

class TestMapConsumerData(unittest.TestCase):
    def test_mapping(self):
       
        mock_consumer_data = [
            (4, 'Rihan maid', 'second Street, new building, pune,maharashatra,  411026', '9445555', 'riha.maid@example.com', '123456789', '1234567890123456789', 'Standard', '[100, 200, 300]', 'Paid')
        ]

        expected_mapped_data = [
            {
                'Consumer ID': 4,
                'First Name': 'Rihan',
                'Last Name': 'maid',
                'Address Line 1': 'second Street',
                'Address Line 2': 'new building',
                'City': 'pune',
                'State': 'maharashatra',
                'Zip Code': '411026',
                'Phone Number': '9445555',
                'Email Address': 'riha.maid@example.com'
            }
        ]

        
        mapped_data = map_consumer_data(mock_consumer_data)

        self.assertEqual(mapped_data, expected_mapped_data)

if __name__ == '__main__':
    unittest.main()
