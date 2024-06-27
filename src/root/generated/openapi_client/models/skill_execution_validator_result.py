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

from root.generated.openapi_client.models.validation_result_status import ValidationResultStatus


class SkillExecutionValidatorResult(BaseModel):
    """
    SkillExecutionValidatorResult
    """  # noqa: E501

    evaluator_id: Optional[StrictStr]
    evaluator_name: StrictStr
    result: Optional[Union[StrictFloat, StrictInt]]
    threshold: Union[StrictFloat, StrictInt]
    status: ValidationResultStatus
    justification: StrictStr
    __properties: ClassVar[List[str]] = [
        "evaluator_id",
        "evaluator_name",
        "result",
        "threshold",
        "status",
        "justification",
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
        """Create an instance of SkillExecutionValidatorResult from a JSON string"""
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
                "evaluator_id",
                "evaluator_name",
                "result",
                "threshold",
                "status",
                "justification",
            ]
        )

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # set to None if evaluator_id (nullable) is None
        # and model_fields_set contains the field
        if self.evaluator_id is None and "evaluator_id" in self.model_fields_set:
            _dict["evaluator_id"] = None

        # set to None if result (nullable) is None
        # and model_fields_set contains the field
        if self.result is None and "result" in self.model_fields_set:
            _dict["result"] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SkillExecutionValidatorResult from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "evaluator_id": obj.get("evaluator_id"),
                "evaluator_name": obj.get("evaluator_name"),
                "result": obj.get("result"),
                "threshold": obj.get("threshold"),
                "status": obj.get("status"),
                "justification": obj.get("justification"),
            }
        )
        return _obj
