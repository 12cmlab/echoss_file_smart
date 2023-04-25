import io
import unittest
import logging
import os
import time
from echoss_file_smart.file_smart import file_extension_check, file_encoding_check

# configure the logger
LOG_FORMAT = "%(asctime)s %(name)s %(levelname)s - %(message)s"
logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)
logger = logging.getLogger(__name__)
# use the logger


class FileformatHandlerTestCase(unittest.TestCase):
    """
        테스트 설정
    """
    def setUp(self):
        ids = self.id().split('.')
        self.str_id = f"{ids[-2]}: {ids[-1]}"
        self.start_time = time.perf_counter()
        logger.info(f"setting up test [{self.str_id}] ")

    def tearDown(self):
        self.end_time = time.perf_counter()
        logger.info(f" tear down test [{self.str_id}] elapsed time {(self.end_time-self.start_time)*1000: .3f}ms \n")

    """
    유닛 테스트 
    """
    filenames = [
        'test_data/complex_build.xml',
        'test_data/complex_one_object.json',
        'test_data/complex_one_object.xml',
        'test_data/SIN_MATNR.csv',
        'test_data/multiheader_table.xlsx',
        'test_data/simple_config.xml',
        'test_data/simple_multiline_object.json',
        'test_data/simple_pom.xml',
        'test_data/simple_standard.csv',
        'test_data/simple_table.xlsx',
        'test_data/채널지수평가 샘플_v0.1.xlsx',
    ]

    def test_file_extension_check(self):

        for f in self.filenames:
            ext = file_extension_check(f)
            print(f"{f} ext = {ext}")


        #    self.assertTrue(filename in str(e))

    def test_file_encoding_check(self):
        for f in self.filenames:
            enc = file_encoding_check(f)
            print(f"{f} ext = {enc}")
        pass


if __name__ == '__main__':
    unittest.main(verbosity=2)
