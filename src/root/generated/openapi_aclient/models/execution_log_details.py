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

from root.generated.openapi_aclient.models.execution_log_details_judge import ExecutionLogDetailsJudge
from root.generated.openapi_aclient.models.execution_log_details_objective import ExecutionLogDetailsObjective
from root.generated.openapi_aclient.models.execution_log_details_skill import ExecutionLogDetailsSkill
from root.generated.openapi_aclient.models.model_params import ModelParams
from root.generated.openapi_aclient.models.nested_user_details import NestedUserDetails
from root.generated.openapi_aclient.models.skill_execution_validator_result import SkillExecutionValidatorResult


class ExecutionLogDetails(BaseModel):
    """
    ExecutionLogDetails
    """  # noqa: E501

    chat_id: Optional[StrictStr]
    cost: Optional[Union[StrictFloat, StrictInt]]
    created_at: Optional[datetime]
    id: StrictStr
    judge: Optional[ExecutionLogDetailsJudge]
    justification: StrictStr
    llm_output: StrictStr
    model_call_duration: Union[StrictFloat, StrictInt]
    model_params: Optional[ModelParams] = None
    model: StrictStr
    objective: ExecutionLogDetailsObjective
    owner: NestedUserDetails
    rendered_prompt: StrictStr
    score: Optional[Union[StrictFloat, StrictInt]]
    skill: ExecutionLogDetailsSkill
    validation_results: List[SkillExecutionValidatorResult]
    variables: Optional[Any]
    __properties: ClassVar[List[str]] = [
        "chat_id",
        "cost",
        "created_at",
        "id",
        "judge",
        "justification",
        "llm_output",
        "model_call_duration",
        "model_params",
        "model",
        "objective",
        "owner",
        "rendered_prompt",
        "score",
        "skill",
        "validation_results",
        "variables",
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
        """Create an instance of ExecutionLogDetails from a JSON string"""
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
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        """
        excluded_fields: Set[str] = set(
            [
                "chat_id",
                "cost",
                "created_at",
                "id",
                "justification",
                "llm_output",
                "model",
                "owner",
                "rendered_prompt",
                "score",
                "validation_results",
                "variables",
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
        # override the default output from pydantic by calling `to_dict()` of model_params
        if self.model_params:
            _dict["model_params"] = self.model_params.to_dict()
        # override the default output from pydantic by calling `to_dict()` of objective
        if self.objective:
            _dict["objective"] = self.objective.to_dict()
        # override the default output from pydantic by calling `to_dict()` of owner
        if self.owner:
            _dict["owner"] = self.owner.to_dict()
        # override the default output from pydantic by calling `to_dict()` of skill
        if self.skill:
            _dict["skill"] = self.skill.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in validation_results (list)
        _items = []
        if self.validation_results:
            for _item in self.validation_results:
                if _item:
                    _items.append(_item.to_dict())
            _dict["validation_results"] = _items
        # set to None if chat_id (nullable) is None
        # and model_fields_set contains the field
        if self.chat_id is None and "chat_id" in self.model_fields_set:
            _dict["chat_id"] = None

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

        # set to None if model_params (nullable) is None
        # and model_fields_set contains the field
        if self.model_params is None and "model_params" in self.model_fields_set:
            _dict["model_params"] = None

        # set to None if score (nullable) is None
        # and model_fields_set contains the field
        if self.score is None and "score" in self.model_fields_set:
            _dict["score"] = None

        # set to None if variables (nullable) is None
        # and model_fields_set contains the field
        if self.variables is None and "variables" in self.model_fields_set:
            _dict["variables"] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ExecutionLogDetails from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "chat_id": obj.get("chat_id"),
                "cost": obj.get("cost"),
                "created_at": obj.get("created_at"),
                "id": obj.get("id"),
                "judge": ExecutionLogDetailsJudge.from_dict(obj["judge"]) if obj.get("judge") is not None else None,
                "justification": obj.get("justification"),
                "llm_output": obj.get("llm_output"),
                "model_call_duration": obj.get("model_call_duration"),
                "model_params": ModelParams.from_dict(obj["model_params"])
                if obj.get("model_params") is not None
                else None,
                "model": obj.get("model"),
                "objective": ExecutionLogDetailsObjective.from_dict(obj["objective"])
                if obj.get("objective") is not None
                else None,
                "owner": NestedUserDetails.from_dict(obj["owner"]) if obj.get("owner") is not None else None,
                "rendered_prompt": obj.get("rendered_prompt"),
                "score": obj.get("score"),
                "skill": ExecutionLogDetailsSkill.from_dict(obj["skill"]) if obj.get("skill") is not None else None,
                "validation_results": [
                    SkillExecutionValidatorResult.from_dict(_item) for _item in obj["validation_results"]
                ]
                if obj.get("validation_results") is not None
                else None,
                "variables": obj.get("variables"),
            }
        )
        return _obj
