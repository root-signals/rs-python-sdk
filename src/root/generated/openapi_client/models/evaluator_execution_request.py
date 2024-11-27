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

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from root.generated.openapi_client.models.evaluator_execution_functions_request import EvaluatorExecutionFunctionsRequest
from typing import Optional, Set
from typing_extensions import Self

class EvaluatorExecutionRequest(BaseModel):
    """
    EvaluatorExecutionRequest
    """ # noqa: E501
    skill_version_id: Optional[Annotated[str, Field(min_length=1, strict=True)]] = None
    request: Optional[Annotated[str, Field(strict=True, max_length=1000000)]] = ''
    response: Annotated[str, Field(min_length=1, strict=True, max_length=1000000)]
    contexts: Optional[List[Annotated[str, Field(min_length=1, strict=True)]]] = None
    functions: Optional[List[EvaluatorExecutionFunctionsRequest]] = None
    expected_output: Optional[Annotated[str, Field(strict=True, max_length=1000000)]] = None
    variables: Optional[Dict[str, Annotated[str, Field(min_length=1, strict=True)]]] = Field(default=None, description="Extra variables to be used in the execution of the evaluator. Optional.")
    __properties: ClassVar[List[str]] = ["skill_version_id", "request", "response", "contexts", "functions", "expected_output", "variables"]

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
        """Create an instance of EvaluatorExecutionRequest from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in functions (list)
        _items = []
        if self.functions:
            for _item in self.functions:
                if _item:
                    _items.append(_item.to_dict())
            _dict['functions'] = _items
        # set to None if skill_version_id (nullable) is None
        # and model_fields_set contains the field
        if self.skill_version_id is None and "skill_version_id" in self.model_fields_set:
            _dict['skill_version_id'] = None

        # set to None if expected_output (nullable) is None
        # and model_fields_set contains the field
        if self.expected_output is None and "expected_output" in self.model_fields_set:
            _dict['expected_output'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of EvaluatorExecutionRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "skill_version_id": obj.get("skill_version_id"),
            "request": obj.get("request") if obj.get("request") is not None else '',
            "response": obj.get("response"),
            "contexts": obj.get("contexts"),
            "functions": [EvaluatorExecutionFunctionsRequest.from_dict(_item) for _item in obj["functions"]] if obj.get("functions") is not None else None,
            "expected_output": obj.get("expected_output"),
            "variables": obj.get("variables")
        })
        return _obj


