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
from typing import Any, ClassVar, Dict, List
from typing_extensions import Annotated
from root.generated.openapi_aclient.models.document_type_enum import DocumentTypeEnum
from root.generated.openapi_aclient.models.response_format_enum import ResponseFormatEnum
from typing import Optional, Set
from typing_extensions import Self

class DocumentParseRequestRequest(BaseModel):
    """
    DocumentParseRequestRequest
    """ # noqa: E501
    id: Annotated[str, Field(min_length=32, strict=True, max_length=36)] = Field(description="An arbitrary string between 32 and 36 characters for version tracking. Will be auto generated if not provided.")
    document_content: Annotated[str, Field(min_length=1, strict=True)] = Field(description="The content of the document to parse, encoded as base64 string")
    document_type: DocumentTypeEnum = Field(description="The type of the document to parse  * `csv` - CSV * `pdf` - PDF * `html` - HTML * `docx` - DOCX * `doc` - DOC * `txt` - TXT * `md` - MD * `pptx` - PPTX * `ppt` - PPT * `xlsx` - XLSX * `xls` - XLS * `odt` - ODT * `rtf` - RTF * `xml` - XML * `eml` - EML * `epub` - EPUB")
    document_language: Annotated[str, Field(min_length=1, strict=True)] = Field(description="The language of the document to parse, using ISO 639-2 three-letter language code")
    response_format: ResponseFormatEnum = Field(description="'plain' returns concatenated text and is fast. 'structured' will return a json object with chunks and metadata that needs post-processing  * `plain` - plain * `structured` - structured")
    __properties: ClassVar[List[str]] = ["id", "document_content", "document_type", "document_language", "response_format"]

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
        """Create an instance of DocumentParseRequestRequest from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DocumentParseRequestRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "document_content": obj.get("document_content"),
            "document_type": obj.get("document_type"),
            "document_language": obj.get("document_language"),
            "response_format": obj.get("response_format")
        })
        return _obj


