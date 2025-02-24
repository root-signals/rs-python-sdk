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
from typing import Any, ClassVar, Dict, List, Optional, Set, Union

from pydantic import BaseModel, ConfigDict, StrictFloat, StrictInt, StrictStr
from typing_extensions import Self

from root.generated.openapi_client.models.execution_log_details_judge import ExecutionLogDetailsJudge
from root.generated.openapi_client.models.execution_log_list_skill import ExecutionLogListSkill
from root.generated.openapi_client.models.nested_user_details import NestedUserDetails


class ExecutionLogList(BaseModel):
    """
    ExecutionLogList
    """  # noqa: E501

    cost: Optional[Union[StrictFloat, StrictInt]]
    created_at: Optional[datetime]
    id: StrictStr
    judge: Optional[ExecutionLogDetailsJudge]
    owner: NestedUserDetails
    score: Optional[Union[StrictFloat, StrictInt]]
    skill: ExecutionLogListSkill
    validation_result_average: Optional[Union[StrictFloat, StrictInt]]
    __properties: ClassVar[List[str]] = [
        "cost",
        "created_at",
        "id",
        "judge",
        "owner",
        "score",
        "skill",
        "validation_result_average",
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
        """Create an instance of ExecutionLogList from a JSON string"""
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
                "cost",
                "created_at",
                "id",
                "owner",
                "score",
                "validation_result_average",
            ]
        )

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of judge
        if self.judge:
            _dict["judge"] = self.judge.to_dict()
        # override the default output from pydantic by calling `to_dict()` of owner
        if self.owner:
            _dict["owner"] = self.owner.to_dict()
        # override the default output from pydantic by calling `to_dict()` of skill
        if self.skill:
            _dict["skill"] = self.skill.to_dict()
        # set to None if cost (nullable) is None
        # and model_fields_set contains the field
        if self.cost is None and "cost" in self.model_fields_set:
            _dict["cost"] = None

        # set to None if created_at (nullable) is None
        # and model_fields_set contains the field
        if self.created_at is None and "created_at" in self.model_fields_set:
            _dict["created_at"] = None

        # set to None if judge (nullable) is None
        # and model_fields_set contains the field
        if self.judge is None and "judge" in self.model_fields_set:
            _dict["judge"] = None

        # set to None if score (nullable) is None
        # and model_fields_set contains the field
        if self.score is None and "score" in self.model_fields_set:
            _dict["score"] = None

        # set to None if validation_result_average (nullable) is None
        # and model_fields_set contains the field
        if self.validation_result_average is None and "validation_result_average" in self.model_fields_set:
            _dict["validation_result_average"] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ExecutionLogList from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "cost": obj.get("cost"),
                "created_at": obj.get("created_at"),
                "id": obj.get("id"),
                "judge": ExecutionLogDetailsJudge.from_dict(obj["judge"]) if obj.get("judge") is not None else None,
                "owner": NestedUserDetails.from_dict(obj["owner"]) if obj.get("owner") is not None else None,
                "score": obj.get("score"),
                "skill": ExecutionLogListSkill.from_dict(obj["skill"]) if obj.get("skill") is not None else None,
                "validation_result_average": obj.get("validation_result_average"),
            }
        )
        return _obj
