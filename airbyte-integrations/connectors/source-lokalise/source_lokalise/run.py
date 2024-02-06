#
# Copyright (c) 2023 Airbyte, Inc., all rights reserved.
#


import sys

from airbyte_cdk.entrypoint import launch
from source_lokalise import SourceLokalise


def run():
    source = SourceLokalise()
    launch(source, sys.argv[1:])