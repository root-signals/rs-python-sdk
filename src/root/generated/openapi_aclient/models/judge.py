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
from typing_extensions import Annotated, Self

from root.generated.openapi_aclient.models.judge_status_enum import JudgeStatusEnum
from root.generated.openapi_aclient.models.nested_evaluator import NestedEvaluator
from root.generated.openapi_aclient.models.nested_vector_objective import NestedVectorObjective


class Judge(BaseModel):
    """
    Judge
    """  # noqa: E501

    id: StrictStr
    name: Annotated[str, Field(strict=True, max_length=512)]
    evaluators: List[NestedEvaluator]
    prototype: NestedVectorObjective
    created_at: Optional[datetime]
    status: JudgeStatusEnum
    meta: Dict[str, Any] = Field(alias="_meta")
    __properties: ClassVar[List[str]] = ["id", "name", "evaluators", "prototype", "created_at", "status", "_meta"]

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
        """Create an instance of Judge from a JSON string"""
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
        * OpenAPI `readOnly` fields are excluded.
        """
        excluded_fields: Set[str] = set(
            [
                "id",
                "evaluators",
                "prototype",
                "created_at",
                "status",
                "meta",
            ]
        )

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in evaluators (list)
        _items = []
        if self.evaluators:
            for _item in self.evaluators:
                if _item:
                    _items.append(_item.to_dict())
            _dict["evaluators"] = _items
        # override the default output from pydantic by calling `to_dict()` of prototype
        if self.prototype:
            _dict["prototype"] = self.prototype.to_dict()
        # set to None if created_at (nullable) is None
        # and model_fields_set contains the field
        if self.created_at is None and "created_at" in self.model_fields_set:
            _dict["created_at"] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Judge from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "id": obj.get("id"),
                "name": obj.get("name"),
                "evaluators": [NestedEvaluator.from_dict(_item) for _item in obj["evaluators"]]
                if obj.get("evaluators") is not None
                else None,
                "prototype": NestedVectorObjective.from_dict(obj["prototype"])
                if obj.get("prototype") is not None
                else None,
                "created_at": obj.get("created_at"),
                "status": obj.get("status"),
                "_meta": obj.get("_meta"),
            }
        )
        return _obj
