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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing_extensions import Annotated, Self

from root.generated.openapi_aclient.models.data_loader import DataLoader
from root.generated.openapi_aclient.models.evaluator_demonstrations import EvaluatorDemonstrations
from root.generated.openapi_aclient.models.input_variable import InputVariable
from root.generated.openapi_aclient.models.model_params import ModelParams
from root.generated.openapi_aclient.models.nested_user_details import NestedUserDetails
from root.generated.openapi_aclient.models.objective import Objective
from root.generated.openapi_aclient.models.reference_variable import ReferenceVariable
from root.generated.openapi_aclient.models.skill_type_enum import SkillTypeEnum
from root.generated.openapi_aclient.models.status_enum import StatusEnum


class Skill(BaseModel):
    """
    Skill
    """  # noqa: E501

    change_note: Optional[StrictStr] = None
    created_at: Optional[datetime]
    data_loaders: Optional[List[DataLoader]] = None
    evaluator_demonstrations: Optional[List[EvaluatorDemonstrations]] = None
    requires_expected_output: Optional[StrictBool] = Field(
        default=None, description="Expected output to the request from the LLM."
    )
    requires_contexts: Optional[StrictBool] = None
    requires_functions: Optional[StrictBool] = None
    id: StrictStr
    input_variables: Optional[List[InputVariable]] = None
    is_evaluator: Optional[StrictBool] = None
    model_params: Optional[ModelParams] = None
    models: Optional[List[StrictStr]] = None
    name: Optional[Annotated[str, Field(strict=True, max_length=1000)]] = None
    objective: Optional[Objective] = None
    owner: NestedUserDetails
    pii_filter: Optional[StrictBool] = Field(
        default=None, description="Filter out personally identifiable information before sending a prompt to a LLM"
    )
    prompt: Optional[StrictStr] = None
    reference_variables: Optional[List[ReferenceVariable]] = None
    skill_type: SkillTypeEnum
    status: Optional[StatusEnum] = None
    system_message: Optional[StrictStr] = None
    updated_at: Optional[datetime]
    updated_by: Optional[NestedUserDetails]
    version_id: StrictStr
    meta: Optional[Any] = Field(alias="_meta")
    __properties: ClassVar[List[str]] = [
        "change_note",
        "created_at",
        "data_loaders",
        "evaluator_demonstrations",
        "requires_expected_output",
        "requires_contexts",
        "requires_functions",
        "id",
        "input_variables",
        "is_evaluator",
        "model_params",
        "models",
        "name",
        "objective",
        "owner",
        "pii_filter",
        "prompt",
        "reference_variables",
        "skill_type",
        "status",
        "system_message",
        "updated_at",
        "updated_by",
        "version_id",
        "_meta",
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
        """Create an instance of Skill from a JSON string"""
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
        """
        excluded_fields: Set[str] = set(
            [
                "created_at",
                "id",
                "owner",
                "skill_type",
                "updated_at",
                "updated_by",
                "version_id",
                "meta",
            ]
        )

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in data_loaders (list)
        _items = []
        if self.data_loaders:
            for _item in self.data_loaders:
                if _item:
                    _items.append(_item.to_dict())
            _dict["data_loaders"] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in evaluator_demonstrations (list)
        _items = []
        if self.evaluator_demonstrations:
            for _item in self.evaluator_demonstrations:
                if _item:
                    _items.append(_item.to_dict())
            _dict["evaluator_demonstrations"] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in input_variables (list)
        _items = []
        if self.input_variables:
            for _item in self.input_variables:
                if _item:
                    _items.append(_item.to_dict())
            _dict["input_variables"] = _items
        # override the default output from pydantic by calling `to_dict()` of model_params
        if self.model_params:
            _dict["model_params"] = self.model_params.to_dict()
        # override the default output from pydantic by calling `to_dict()` of objective
        if self.objective:
            _dict["objective"] = self.objective.to_dict()
        # override the default output from pydantic by calling `to_dict()` of owner
        if self.owner:
            _dict["owner"] = self.owner.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in reference_variables (list)
        _items = []
        if self.reference_variables:
            for _item in self.reference_variables:
                if _item:
                    _items.append(_item.to_dict())
            _dict["reference_variables"] = _items
        # override the default output from pydantic by calling `to_dict()` of updated_by
        if self.updated_by:
            _dict["updated_by"] = self.updated_by.to_dict()
        # set to None if change_note (nullable) is None
        # and model_fields_set contains the field
        if self.change_note is None and "change_note" in self.model_fields_set:
            _dict["change_note"] = None

        # set to None if created_at (nullable) is None
        # and model_fields_set contains the field
        if self.created_at is None and "created_at" in self.model_fields_set:
            _dict["created_at"] = None

        # set to None if evaluator_demonstrations (nullable) is None
        # and model_fields_set contains the field
        if self.evaluator_demonstrations is None and "evaluator_demonstrations" in self.model_fields_set:
            _dict["evaluator_demonstrations"] = None

        # set to None if model_params (nullable) is None
        # and model_fields_set contains the field
        if self.model_params is None and "model_params" in self.model_fields_set:
            _dict["model_params"] = None

        # set to None if objective (nullable) is None
        # and model_fields_set contains the field
        if self.objective is None and "objective" in self.model_fields_set:
            _dict["objective"] = None

        # set to None if updated_at (nullable) is None
        # and model_fields_set contains the field
        if self.updated_at is None and "updated_at" in self.model_fields_set:
            _dict["updated_at"] = None

        # set to None if updated_by (nullable) is None
        # and model_fields_set contains the field
        if self.updated_by is None and "updated_by" in self.model_fields_set:
            _dict["updated_by"] = None

        # set to None if meta (nullable) is None
        # and model_fields_set contains the field
        if self.meta is None and "meta" in self.model_fields_set:
            _dict["_meta"] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Skill from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "change_note": obj.get("change_note"),
                "created_at": obj.get("created_at"),
                "data_loaders": [DataLoader.from_dict(_item) for _item in obj["data_loaders"]]
                if obj.get("data_loaders") is not None
                else None,
                "evaluator_demonstrations": [
                    EvaluatorDemonstrations.from_dict(_item) for _item in obj["evaluator_demonstrations"]
                ]
                if obj.get("evaluator_demonstrations") is not None
                else None,
                "requires_expected_output": obj.get("requires_expected_output"),
                "requires_contexts": obj.get("requires_contexts"),
                "requires_functions": obj.get("requires_functions"),
                "id": obj.get("id"),
                "input_variables": [InputVariable.from_dict(_item) for _item in obj["input_variables"]]
                if obj.get("input_variables") is not None
                else None,
                "is_evaluator": obj.get("is_evaluator"),
                "model_params": ModelParams.from_dict(obj["model_params"])
                if obj.get("model_params") is not None
                else None,
                "models": obj.get("models"),
                "name": obj.get("name"),
                "objective": Objective.from_dict(obj["objective"]) if obj.get("objective") is not None else None,
                "owner": NestedUserDetails.from_dict(obj["owner"]) if obj.get("owner") is not None else None,
                "pii_filter": obj.get("pii_filter"),
                "prompt": obj.get("prompt"),
                "reference_variables": [ReferenceVariable.from_dict(_item) for _item in obj["reference_variables"]]
                if obj.get("reference_variables") is not None
                else None,
                "skill_type": obj.get("skill_type"),
                "status": obj.get("status"),
                "system_message": obj.get("system_message"),
                "updated_at": obj.get("updated_at"),
                "updated_by": NestedUserDetails.from_dict(obj["updated_by"])
                if obj.get("updated_by") is not None
                else None,
                "version_id": obj.get("version_id"),
                "_meta": obj.get("_meta"),
            }
        )
        return _obj
