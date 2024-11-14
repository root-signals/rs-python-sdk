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

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing_extensions import Annotated, Self


class ChatCreateRequest(BaseModel):
    """
    ChatCreateRequest
    """  # noqa: E501

    chat_id: Optional[Annotated[str, Field(min_length=1, strict=True, max_length=255)]] = None
    skill_id: StrictStr
    name: Optional[StrictStr] = None
    assistant_welcome_messages: Optional[List[Any]] = None
    history_from_chat_id: Optional[Annotated[str, Field(min_length=1, strict=True)]] = Field(
        default=None, description="Chat to copy the message history from."
    )
    __properties: ClassVar[List[str]] = [
        "chat_id",
        "skill_id",
        "name",
        "assistant_welcome_messages",
        "history_from_chat_id",
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
        """Create an instance of ChatCreateRequest from a JSON string"""
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
        # set to None if assistant_welcome_messages (nullable) is None
        # and model_fields_set contains the field
        if self.assistant_welcome_messages is None and "assistant_welcome_messages" in self.model_fields_set:
            _dict["assistant_welcome_messages"] = None

        # set to None if history_from_chat_id (nullable) is None
        # and model_fields_set contains the field
        if self.history_from_chat_id is None and "history_from_chat_id" in self.model_fields_set:
            _dict["history_from_chat_id"] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ChatCreateRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "chat_id": obj.get("chat_id"),
                "skill_id": obj.get("skill_id"),
                "name": obj.get("name"),
                "assistant_welcome_messages": obj.get("assistant_welcome_messages"),
                "history_from_chat_id": obj.get("history_from_chat_id"),
            }
        )
        return _obj
