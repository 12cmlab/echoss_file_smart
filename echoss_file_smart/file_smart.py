"""
    echoss AI Bigdata Center Solution - file smart
"""
import io
import logging
import pandas as pd
from typing import Literal, Optional, Tuple, Union

logger = logging.getLogger(__name__)


def file_extension_check(file_path):
    exts = file_path.rsplit(".")

    if len(exts)>1:
        return exts[-1]
    else:
        return ""


def file_encoding_check(file_path):
    encoding_list = ['utf-8', 'cp949', 'ascii']

    for enc in encoding_list:
        try:
            fp = open(file_path, encoding=enc)
            if fp:
                fp.close()
            return enc
        except:
            logger.debug(f"{file_path} is not {enc} encoding")



