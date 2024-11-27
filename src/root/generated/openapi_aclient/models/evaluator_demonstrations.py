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

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self

class EvaluatorDemonstrations(BaseModel):
    """
    EvaluatorDemonstrations
    """ # noqa: E501
    prompt: Optional[StrictStr] = None
    output: StrictStr
    score: Union[Annotated[float, Field(le=1, strict=True, ge=0)], Annotated[int, Field(le=1, strict=True, ge=0)]]
    justification: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["prompt", "output", "score", "justification"]

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
        """Create an instance of EvaluatorDemonstrations from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # set to None if prompt (nullable) is None
        # and model_fields_set contains the field
        if self.prompt is None and "prompt" in self.model_fields_set:
            _dict['prompt'] = None

        # set to None if justification (nullable) is None
        # and model_fields_set contains the field
        if self.justification is None and "justification" in self.model_fields_set:
            _dict['justification'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of EvaluatorDemonstrations from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "prompt": obj.get("prompt"),
            "output": obj.get("output"),
            "score": obj.get("score"),
            "justification": obj.get("justification")
        })
        return _obj


