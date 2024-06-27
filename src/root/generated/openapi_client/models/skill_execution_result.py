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
from typing import Any, ClassVar, Dict, List, Optional, Set, Union

from pydantic import BaseModel, ConfigDict, StrictFloat, StrictInt, StrictStr
from typing_extensions import Self

from root.generated.openapi_client.models.validation import Validation


class SkillExecutionResult(BaseModel):
    """
    SkillExecutionResult
    """  # noqa: E501

    llm_output: StrictStr
    validation: Validation
    model: StrictStr
    execution_log_id: StrictStr
    rendered_prompt: StrictStr
    cost: Optional[Union[StrictFloat, StrictInt]]
    __properties: ClassVar[List[str]] = [
        "llm_output",
        "validation",
        "model",
        "execution_log_id",
        "rendered_prompt",
        "cost",
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
        """Create an instance of SkillExecutionResult from a JSON string"""
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
        """
        excluded_fields: Set[str] = set(
            [
                "model",
                "rendered_prompt",
            ]
        )

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of validation
        if self.validation:
            _dict["validation"] = self.validation.to_dict()
        # set to None if cost (nullable) is None
        # and model_fields_set contains the field
        if self.cost is None and "cost" in self.model_fields_set:
            _dict["cost"] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SkillExecutionResult from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "llm_output": obj.get("llm_output"),
                "validation": Validation.from_dict(obj["validation"]) if obj.get("validation") is not None else None,
                "model": obj.get("model"),
                "execution_log_id": obj.get("execution_log_id"),
                "rendered_prompt": obj.get("rendered_prompt"),
                "cost": obj.get("cost"),
            }
        )
        return _obj
