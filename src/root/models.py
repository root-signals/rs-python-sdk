from functools import partial
from typing import Iterator, Optional

from root.generated.openapi_client.api.models_api import ModelsApi
from root.generated.openapi_client.models.model import Model
from root.generated.openapi_client.models.model_create_request import ModelCreateRequest

from .generated.openapi_client import ApiClient
from .utils import iterate_cursor_list


class Models:
    """Models (sub) API

    Note:

      The construction of the API instance should be handled by
      accesing an attribute of a :class:`root.client.RootSignals` instance.
    """

    def __init__(self, client: ApiClient):
        self.client = client

    def list(self, *, limit: int = 100) -> Iterator[Model]:
        """Iterate through the models.

        Note:

          The call will list only publicly available global models and
          those models available to the organzation(s) of the user.

        Args:
          limit: Number of entries to iterate through at most.

        """
        api_instance = ModelsApi(self.client)
        yield from iterate_cursor_list(partial(api_instance.models_list), limit=limit)

    def create(
        self,
        *,
        name: str,
        model: Optional[str] = None,
        default_key: Optional[str] = None,
        max_output_token_count: Optional[int] = None,
        max_token_count: Optional[int] = None,
        url: Optional[str] = None,
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
        request = ModelCreateRequest(
            name=name,
            model=model,
            default_key=default_key,
            max_output_token_count=max_output_token_count,
            max_token_count=max_token_count,
            is_local=url is not None,
            url=url,
        )

        api_instance = ModelsApi(self.client)
        return api_instance.models_create(model_create_request=request).id

    def delete(self, model_id: str) -> None:
        """
        Delete the model.

        Args:

          model: The model to be deleted.

        """
        api_instance = ModelsApi(self.client)
        return api_instance.models_destroy(id=model_id)
