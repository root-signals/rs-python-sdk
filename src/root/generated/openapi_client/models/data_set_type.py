# coding: utf-8

"""
    Root Signals API

    Root Signals JSON API provides a way to access Root Signals using provisioned API token

    The version of the OpenAPI document: 1.0.0 (latest)
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class DataSetType(str, Enum):
    """
    * `reference` - REFERENCE * `test` - TEST
    """

    """
    allowed enum values
    """
    REFERENCE = 'reference'
    TEST = 'test'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of DataSetType from a JSON string"""
        return cls(json.loads(json_str))


