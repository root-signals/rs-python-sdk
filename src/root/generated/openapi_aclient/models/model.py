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
import pprint
import re  # noqa: F401
from typing import Any, ClassVar, Dict, List, Optional, Set

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing_extensions import Annotated, Self


class Model(BaseModel):
    """
    Model
    """  # noqa: E501

    default_key: Optional[Annotated[str, Field(strict=True, max_length=4000)]] = None
    id: StrictStr
    max_output_token_count: Optional[Annotated[int, Field(strict=True, ge=800)]] = None
    max_token_count: Optional[Annotated[int, Field(le=2147483647, strict=True, ge=0)]] = None
    model: Optional[StrictStr] = None
    name: Annotated[str, Field(strict=True, max_length=100)]
    url: Optional[Annotated[str, Field(strict=True, max_length=1024)]] = None
    __properties: ClassVar[List[str]] = [
        "default_key",
        "id",
        "max_output_token_count",
        "max_token_count",
        "model",
        "name",
        "url",
    ]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of Model from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * OpenAPI `readOnly` fields are excluded.
        """
        excluded_fields: Set[str] = set(
            [
                "id",
            ]
        )

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # set to None if default_key (nullable) is None
        # and model_fields_set contains the field
        if self.default_key is None and "default_key" in self.model_fields_set:
            _dict["default_key"] = None

        # set to None if max_token_count (nullable) is None
        # and model_fields_set contains the field
        if self.max_token_count is None and "max_token_count" in self.model_fields_set:
            _dict["max_token_count"] = None

        # set to None if url (nullable) is None
        # and model_fields_set contains the field
        if self.url is None and "url" in self.model_fields_set:
            _dict["url"] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Model from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "default_key": obj.get("default_key"),
                "id": obj.get("id"),
                "max_output_token_count": obj.get("max_output_token_count"),
                "max_token_count": obj.get("max_token_count"),
                "model": obj.get("model"),
                "name": obj.get("name"),
                "url": obj.get("url"),
            }
        )
        return _obj
