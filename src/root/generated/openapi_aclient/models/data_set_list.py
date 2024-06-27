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
from datetime import datetime
from typing import Any, ClassVar, Dict, List, Optional, Set

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing_extensions import Self

from root.generated.openapi_aclient.models.data_set_type import DataSetType
from root.generated.openapi_aclient.models.nested_user_details import NestedUserDetails
from root.generated.openapi_aclient.models.status_enum import StatusEnum


class DataSetList(BaseModel):
    """
    DataSetList
    """  # noqa: E501

    id: StrictStr
    name: Optional[StrictStr] = None
    type: Optional[DataSetType] = None
    tags: Optional[List[StrictStr]] = None
    owner: NestedUserDetails
    created_at: datetime
    status: Optional[StatusEnum] = None
    meta: Optional[Any] = Field(alias="_meta")
    __properties: ClassVar[List[str]] = ["id", "name", "type", "tags", "owner", "created_at", "status", "_meta"]

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
        """Create an instance of DataSetList from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        """
        excluded_fields: Set[str] = set(
            [
                "id",
                "owner",
                "created_at",
                "meta",
            ]
        )

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of owner
        if self.owner:
            _dict["owner"] = self.owner.to_dict()
        # set to None if name (nullable) is None
        # and model_fields_set contains the field
        if self.name is None and "name" in self.model_fields_set:
            _dict["name"] = None

        # set to None if meta (nullable) is None
        # and model_fields_set contains the field
        if self.meta is None and "meta" in self.model_fields_set:
            _dict["_meta"] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DataSetList from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "id": obj.get("id"),
                "name": obj.get("name"),
                "type": obj.get("type"),
                "tags": obj.get("tags"),
                "owner": NestedUserDetails.from_dict(obj["owner"]) if obj.get("owner") is not None else None,
                "created_at": obj.get("created_at"),
                "status": obj.get("status"),
                "_meta": obj.get("_meta"),
            }
        )
        return _obj
