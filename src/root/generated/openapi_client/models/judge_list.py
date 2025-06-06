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

from root.generated.openapi_client.models.evaluator_inputs_value import EvaluatorInputsValue
from root.generated.openapi_client.models.judge_status_enum import JudgeStatusEnum
from root.generated.openapi_client.models.nested_evaluator import NestedEvaluator


class JudgeList(BaseModel):
    """
    JudgeList
    """  # noqa: E501

    id: StrictStr
    name: StrictStr
    intent: StrictStr
    created_at: Optional[datetime]
    status: JudgeStatusEnum
    inputs: Dict[str, EvaluatorInputsValue] = Field(
        description="Schema defining the input parameters required for execution. The schema consists of variables defined in the prompt template (predicate) and special variables like functions, contexts, and expected output."
    )
    evaluators: List[NestedEvaluator]
    __properties: ClassVar[List[str]] = ["id", "name", "intent", "created_at", "status", "inputs", "evaluators"]

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
        """Create an instance of JudgeList from a JSON string"""
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
                "intent",
                "created_at",
                "status",
                "inputs",
                "evaluators",
            ]
        )

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each value in inputs (dict)
        _field_dict = {}
        if self.inputs:
            for _key in self.inputs:
                if self.inputs[_key]:
                    _field_dict[_key] = self.inputs[_key].to_dict()
            _dict["inputs"] = _field_dict
        # override the default output from pydantic by calling `to_dict()` of each item in evaluators (list)
        _items = []
        if self.evaluators:
            for _item in self.evaluators:
                if _item:
                    _items.append(_item.to_dict())
            _dict["evaluators"] = _items
        # set to None if created_at (nullable) is None
        # and model_fields_set contains the field
        if self.created_at is None and "created_at" in self.model_fields_set:
            _dict["created_at"] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of JudgeList from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "id": obj.get("id"),
                "name": obj.get("name"),
                "intent": obj.get("intent"),
                "created_at": obj.get("created_at"),
                "status": obj.get("status"),
                "inputs": dict((_k, EvaluatorInputsValue.from_dict(_v)) for _k, _v in obj["inputs"].items())
                if obj.get("inputs") is not None
                else None,
                "evaluators": [NestedEvaluator.from_dict(_item) for _item in obj["evaluators"]]
                if obj.get("evaluators") is not None
                else None,
            }
        )
        return _obj
