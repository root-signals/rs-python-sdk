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
from root.generated.openapi_aclient.models.nested_objective_list import NestedObjectiveList
from root.generated.openapi_aclient.models.nested_user_details import NestedUserDetails
from root.generated.openapi_aclient.models.status_enum import StatusEnum
from typing import Optional, Set
from typing_extensions import Self

class SkillListOutput(BaseModel):
    """
    SkillListOutput
    """ # noqa: E501
    meta: Optional[Any] = Field(alias="_meta")
    created_at: Optional[datetime]
    models: List[StrictStr]
    id: StrictStr
    name: StrictStr
    objective: NestedObjectiveList
    owner: NestedUserDetails
    prompt: StrictStr
    status: StatusEnum
    updated_at: Optional[datetime]
    updated_by: Optional[NestedUserDetails]
    version_id: StrictStr
    last_executed_at: Optional[datetime]
    __properties: ClassVar[List[str]] = ["_meta", "created_at", "models", "id", "name", "objective", "owner", "prompt", "status", "updated_at", "updated_by", "version_id", "last_executed_at"]

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
        """Create an instance of SkillListOutput from a JSON string"""
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
        * OpenAPI `readOnly` fields are excluded.
        """
        excluded_fields: Set[str] = set([
            "meta",
            "created_at",
            "models",
            "id",
            "name",
            "objective",
            "owner",
            "prompt",
            "status",
            "updated_at",
            "updated_by",
            "version_id",
            "last_executed_at",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of objective
        if self.objective:
            _dict['objective'] = self.objective.to_dict()
        # override the default output from pydantic by calling `to_dict()` of owner
        if self.owner:
            _dict['owner'] = self.owner.to_dict()
        # override the default output from pydantic by calling `to_dict()` of updated_by
        if self.updated_by:
            _dict['updated_by'] = self.updated_by.to_dict()
        # set to None if meta (nullable) is None
        # and model_fields_set contains the field
        if self.meta is None and "meta" in self.model_fields_set:
            _dict['_meta'] = None

        # set to None if created_at (nullable) is None
        # and model_fields_set contains the field
        if self.created_at is None and "created_at" in self.model_fields_set:
            _dict['created_at'] = None

        # set to None if updated_at (nullable) is None
        # and model_fields_set contains the field
        if self.updated_at is None and "updated_at" in self.model_fields_set:
            _dict['updated_at'] = None

        # set to None if updated_by (nullable) is None
        # and model_fields_set contains the field
        if self.updated_by is None and "updated_by" in self.model_fields_set:
            _dict['updated_by'] = None

        # set to None if last_executed_at (nullable) is None
        # and model_fields_set contains the field
        if self.last_executed_at is None and "last_executed_at" in self.model_fields_set:
            _dict['last_executed_at'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SkillListOutput from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "_meta": obj.get("_meta"),
            "created_at": obj.get("created_at"),
            "models": obj.get("models"),
            "id": obj.get("id"),
            "name": obj.get("name"),
            "objective": NestedObjectiveList.from_dict(obj["objective"]) if obj.get("objective") is not None else None,
            "owner": NestedUserDetails.from_dict(obj["owner"]) if obj.get("owner") is not None else None,
            "prompt": obj.get("prompt"),
            "status": obj.get("status"),
            "updated_at": obj.get("updated_at"),
            "updated_by": NestedUserDetails.from_dict(obj["updated_by"]) if obj.get("updated_by") is not None else None,
            "version_id": obj.get("version_id"),
            "last_executed_at": obj.get("last_executed_at")
        })
        return _obj


