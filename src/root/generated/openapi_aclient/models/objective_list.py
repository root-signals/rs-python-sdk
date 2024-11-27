# coding: utf-8

"""
    Root Signals API

    Root Signals JSON API provides a way to access Root Signals using provisioned API token

    The version of the OpenAPI document: 1.0.0 (latest)
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from root.generated.openapi_aclient.models.nested_user_details import NestedUserDetails
from root.generated.openapi_aclient.models.objective_validator import ObjectiveValidator
from root.generated.openapi_aclient.models.status_enum import StatusEnum
from typing import Optional, Set
from typing_extensions import Self

class ObjectiveList(BaseModel):
    """
    ObjectiveList
    """ # noqa: E501
    id: StrictStr
    intent: Optional[Annotated[str, Field(strict=True, max_length=10000)]] = None
    status: Optional[StatusEnum] = None
    owner: NestedUserDetails
    created_at: Optional[datetime]
    validators: List[ObjectiveValidator]
    meta: Dict[str, Any] = Field(alias="_meta")
    __properties: ClassVar[List[str]] = ["id", "intent", "status", "owner", "created_at", "validators", "_meta"]

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
        """Create an instance of ObjectiveList from a JSON string"""
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
        * OpenAPI `readOnly` fields are excluded.
        """
        excluded_fields: Set[str] = set([
            "id",
            "owner",
            "created_at",
            "validators",
            "meta",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of owner
        if self.owner:
            _dict['owner'] = self.owner.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in validators (list)
        _items = []
        if self.validators:
            for _item in self.validators:
                if _item:
                    _items.append(_item.to_dict())
            _dict['validators'] = _items
        # set to None if created_at (nullable) is None
        # and model_fields_set contains the field
        if self.created_at is None and "created_at" in self.model_fields_set:
            _dict['created_at'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ObjectiveList from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "intent": obj.get("intent"),
            "status": obj.get("status"),
            "owner": NestedUserDetails.from_dict(obj["owner"]) if obj.get("owner") is not None else None,
            "created_at": obj.get("created_at"),
            "validators": [ObjectiveValidator.from_dict(_item) for _item in obj["validators"]] if obj.get("validators") is not None else None,
            "_meta": obj.get("_meta")
        })
        return _obj


