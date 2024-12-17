from functools import partial
from typing import AsyncIterator, Awaitable, Iterator, List, Optional, Union

from pydantic import StrictStr

from .generated.openapi_aclient import ApiClient as AApiClient
from .generated.openapi_aclient.api.models_api import ModelsApi as AModelsApi
from .generated.openapi_aclient.models.model import Model as AModel
from .generated.openapi_aclient.models.model_request import ModelRequest as AModelRequest
from .generated.openapi_aclient.models.paginated_model_list_list import (
    PaginatedModelListList as APaginatedModelListList,
)
from .generated.openapi_client import ApiClient
from .generated.openapi_client.api.models_api import ModelsApi
from .generated.openapi_client.models.model import Model
from .generated.openapi_client.models.model_request import ModelRequest
from .utils import iterate_cursor_list


class Models:
    """Models (sub) API

    Note:

      The construction of the API instance should be handled by
      accesing an attribute of a :class:`root.client.RootSignals` instance.
    """

    def __init__(self, client: Union[Awaitable[AApiClient], ApiClient]):
        self.client = client

    def list(
        self,
        *,
        capable_of: Optional[List[str]] = None,
        limit: int = 100,
    ) -> Iterator[Model]:
        """Iterate through the models.

        Note:

          The call will list only publicly available global models and
          those models available to the organzation(s) of the user.

        Args:
          limit: Number of entries to iterate through at most.

          capable_of: List of capabilities to filter the models by.

        """

        if not isinstance(self.client, ApiClient) and self.client.__name__ == "_aapi_client":  # type: ignore[attr-defined]
            raise Exception("This method is not available in asynchronous mode")

        api_instance = ModelsApi(self.client)
        yield from iterate_cursor_list(partial(api_instance.models_list, capable_of=capable_of), limit=limit)

    async def alist(
        self,
        *,
        capable_of: Optional[List[str]] = None,
        limit: int = 100,
    ) -> AsyncIterator[AModel]:
        """Asynchronously iterate through the models.

        Note:

          The call will list only publicly available global models and
          those models available to the organzation(s) of the user.

        Args:
          limit: Number of entries to iterate through at most.

          capable_of: List of capabilities to filter the models by.

        """

        if isinstance(self.client, ApiClient):
            raise Exception("This method is not available in synchronous mode")

        api_instance = AModelsApi(await self.client())  # type: ignore[operator]
        partial_list = partial(api_instance.models_list, capable_of=capable_of)

        cursor: Optional[StrictStr] = None
        while limit > 0:
            result: APaginatedModelListList = await partial_list(page_size=limit, cursor=cursor)
            if not result.results:
                return

            used_results = result.results[:limit]
            for used_result in used_results:
                yield used_result  # type: ignore[misc]

                limit -= len(used_results)
                if not (cursor := result.next):
                    return

    def create(
        self,
        *,
        name: str,
        model: Optional[str] = None,
        default_key: Optional[str] = None,
        max_output_token_count: Optional[int] = None,
        max_token_count: Optional[int] = None,
        url: Optional[str] = None,
        _request_timeout: Optional[int] = None,
    ) -> str:
        """Create a new model and return its ID.

        Args:

          name: The unique identifier for the model instance  (e.g. "google/gemma-2-9b").

          model: The base model name to be used. Defaults to name.

          default_key: The default API key required for the model, if applicable.

          max_output_token_count: The maximum number of tokens to output.

          max_token_count: The maximum number of tokens to process.

          url: Optional URL pointing to the model's endpoint.

        """

        if not isinstance(self.client, ApiClient) and self.client.__name__ == "_aapi_client":  # type: ignore[attr-defined]
            raise Exception("This method is not available in asynchronous mode")

        request = ModelRequest(
            name=name,
            model=model,
            default_key=default_key,
            max_output_token_count=max_output_token_count,
            max_token_count=max_token_count,
            url=url,
        )

        api_instance = ModelsApi(self.client)
        return api_instance.models_create(model_request=request, _request_timeout=_request_timeout).id

    async def acreate(
        self,
        *,
        name: str,
        model: Optional[str] = None,
        default_key: Optional[str] = None,
        max_output_token_count: Optional[int] = None,
        max_token_count: Optional[int] = None,
        url: Optional[str] = None,
        _request_timeout: Optional[int] = None,
    ) -> str:
        """Asynchronously create a new model and return its ID.

        Args:

          name: The unique identifier for the model instance  (e.g. "google/gemma-2-9b").

          model: The base model name to be used. Defaults to name.

          default_key: The default API key required for the model, if applicable.

          max_output_token_count: The maximum number of tokens to output.

          max_token_count: The maximum number of tokens to process.

          url: Optional URL pointing to the model's endpoint.

        """

        if isinstance(self.client, ApiClient):
            raise Exception("This method is not available in synchronous mode")

        request = AModelRequest(
            name=name,
            model=model,
            default_key=default_key,
            max_output_token_count=max_output_token_count,
            max_token_count=max_token_count,
            url=url,
        )

        api_instance = AModelsApi(await self.client())  # type: ignore[operator]
        created_model = await api_instance.models_create(model_request=request, _request_timeout=_request_timeout)
        return created_model.id

    def delete(
        self,
        model_id: str,
        *,
        _request_timeout: Optional[int] = None,
    ) -> None:
        """
        Delete the model.

        Args:

          model: The model to be deleted.

        """

        if not isinstance(self.client, ApiClient) and self.client.__name__ == "_aapi_client":  # type: ignore[attr-defined]
            raise Exception("This method is not available in asynchronous mode")

        api_instance = ModelsApi(self.client)
        return api_instance.models_destroy(id=model_id, _request_timeout=_request_timeout)

    async def adelete(
        self,
        model_id: str,
        *,
        _request_timeout: Optional[int] = None,
    ) -> None:
        """
        Asynchronously delete the model.

        Args:

          model: The model to be deleted.

        """

        if isinstance(self.client, ApiClient):
            raise Exception("This method is not available in synchronous mode")

        api_instance = AModelsApi(await self.client())  # type: ignore[operator]
        return await api_instance.models_destroy(id=model_id, _request_timeout=_request_timeout)

    # TODO: update
