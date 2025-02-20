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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing_extensions import Annotated, Self

from root.generated.openapi_client.models.evaluator_demonstrations_request import EvaluatorDemonstrationsRequest
from root.generated.openapi_client.models.input_variable_request import InputVariableRequest
from root.generated.openapi_client.models.model_params_request import ModelParamsRequest
from root.generated.openapi_client.models.objective_request import ObjectiveRequest
from root.generated.openapi_client.models.reference_variable_request import ReferenceVariableRequest
from root.generated.openapi_client.models.status_enum import StatusEnum


class EvaluatorRequest(BaseModel):
    """
    EvaluatorRequest
    """  # noqa: E501

    change_note: Optional[StrictStr] = None
    evaluator_demonstrations: Optional[List[EvaluatorDemonstrationsRequest]] = None
    evaluator_only_offline: Optional[StrictBool] = Field(
        default=None, description="Do not run the evaluator if used as an Objective validator."
    )
    evaluator_require_reference_variables: Optional[StrictBool] = None
    input_variables: Optional[List[InputVariableRequest]] = None
    model_params: Optional[ModelParamsRequest] = None
    models: Optional[List[Annotated[str, Field(min_length=1, strict=True)]]] = None
    name: Optional[Annotated[str, Field(min_length=1, strict=True, max_length=1000)]] = None
    objective: Optional[ObjectiveRequest] = None
    objective_id: Optional[StrictStr] = None
    objective_version_id: Optional[StrictStr] = Field(
        default=None,
        description="Optionally pin the Skill to a specific version of an Objective. If not provided, the latest version of the objective will be used and followed.",
    )
    overwrite: Optional[StrictBool] = Field(
        default=False, description="Overwrite existing skill with the same name. Only for POST requests."
    )
    prompt: Optional[StrictStr] = None
    reference_variables: Optional[List[ReferenceVariableRequest]] = None
    status: Optional[StatusEnum] = None
    system_message: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = [
        "change_note",
        "evaluator_demonstrations",
        "evaluator_only_offline",
        "evaluator_require_reference_variables",
        "input_variables",
        "model_params",
        "models",
        "name",
        "objective",
        "objective_id",
        "objective_version_id",
        "overwrite",
        "prompt",
        "reference_variables",
        "status",
        "system_message",
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
        """Create an instance of EvaluatorRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
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
        # override the default output from pydantic by calling `to_dict()` of each item in reference_variables (list)
        _items = []
        if self.reference_variables:
            for _item in self.reference_variables:
                if _item:
                    _items.append(_item.to_dict())
            _dict["reference_variables"] = _items
        # set to None if change_note (nullable) is None
        # and model_fields_set contains the field
        if self.change_note is None and "change_note" in self.model_fields_set:
            _dict["change_note"] = None

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

        # set to None if objective_id (nullable) is None
        # and model_fields_set contains the field
        if self.objective_id is None and "objective_id" in self.model_fields_set:
            _dict["objective_id"] = None

        # set to None if objective_version_id (nullable) is None
        # and model_fields_set contains the field
        if self.objective_version_id is None and "objective_version_id" in self.model_fields_set:
            _dict["objective_version_id"] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of EvaluatorRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "change_note": obj.get("change_note"),
                "evaluator_demonstrations": [
                    EvaluatorDemonstrationsRequest.from_dict(_item) for _item in obj["evaluator_demonstrations"]
                ]
                if obj.get("evaluator_demonstrations") is not None
                else None,
                "evaluator_only_offline": obj.get("evaluator_only_offline"),
                "evaluator_require_reference_variables": obj.get("evaluator_require_reference_variables"),
                "input_variables": [InputVariableRequest.from_dict(_item) for _item in obj["input_variables"]]
                if obj.get("input_variables") is not None
                else None,
                "model_params": ModelParamsRequest.from_dict(obj["model_params"])
                if obj.get("model_params") is not None
                else None,
                "models": obj.get("models"),
                "name": obj.get("name"),
                "objective": ObjectiveRequest.from_dict(obj["objective"]) if obj.get("objective") is not None else None,
                "objective_id": obj.get("objective_id"),
                "objective_version_id": obj.get("objective_version_id"),
                "overwrite": obj.get("overwrite") if obj.get("overwrite") is not None else False,
                "prompt": obj.get("prompt"),
                "reference_variables": [
                    ReferenceVariableRequest.from_dict(_item) for _item in obj["reference_variables"]
                ]
                if obj.get("reference_variables") is not None
                else None,
                "status": obj.get("status"),
                "system_message": obj.get("system_message"),
            }
        )
        return _obj
