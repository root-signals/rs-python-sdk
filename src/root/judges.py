from __future__ import annotations

from functools import partial
from typing import AsyncIterator, Iterator, List, Optional, cast

from pydantic import StrictStr

from .generated.openapi_aclient import ApiClient as AApiClient
from .generated.openapi_aclient.api.beta_api import BetaApi as ABetaApi
from .generated.openapi_aclient.models.evaluator_reference_request import (
    EvaluatorReferenceRequest as AEvaluatorReferenceRequest,
)
from .generated.openapi_aclient.models.judge import Judge as AOpenApiJudge
from .generated.openapi_aclient.models.judge_execution_request import (
    JudgeExecutionRequest as AJudgeExecutionRequest,
)
from .generated.openapi_aclient.models.judge_execution_response import (
    JudgeExecutionResponse as AJudgeExecutionResponse,
)
from .generated.openapi_aclient.models.judge_request import JudgeRequest as AJudgeRequest
from .generated.openapi_aclient.models.paginated_judge_list_list import (
    PaginatedJudgeListList as APaginatedJudgeListList,
)
from .generated.openapi_aclient.models.patched_judge_request import (
    PatchedJudgeRequest as APatchedJudgeRequest,
)
from .generated.openapi_client import ApiClient
from .generated.openapi_client.api.beta_api import BetaApi
from .generated.openapi_client.models.evaluator_reference_request import EvaluatorReferenceRequest
from .generated.openapi_client.models.judge import Judge as OpenApiJudge
from .generated.openapi_client.models.judge_execution_request import JudgeExecutionRequest
from .generated.openapi_client.models.judge_execution_response import JudgeExecutionResponse
from .generated.openapi_client.models.judge_request import JudgeRequest
from .generated.openapi_client.models.patched_judge_request import PatchedJudgeRequest
from .utils import ClientContextCallable, iterate_cursor_list, with_async_client, with_sync_client


class Judge(OpenApiJudge):
    """Wrapper for a single Judge.

    For available attributes, please check the (automatically
    generated) superclass documentation.
    """

    client_context: ClientContextCallable

    @classmethod
    def _wrap(cls, apiobj: OpenApiJudge, client_context: ClientContextCallable) -> "Judge":
        if not isinstance(apiobj, OpenApiJudge):
            raise ValueError(f"Wrong instance in _wrap: {apiobj!r}")
        obj = cast(Judge, apiobj)
        obj.__class__ = cls
        obj.client_context = client_context
        return obj

    @with_sync_client
    def run(
        self,
        *,
        response: str,
        request: Optional[str] = None,
        _request_timeout: Optional[int] = None,
        _client: ApiClient,
    ) -> JudgeExecutionResponse:
        """
        Run the judge.

        Args:
          response: LLM output to evaluate
          request: The prompt sent to the LLM. Optional.
        """
        api_instance = BetaApi(_client)
        execution_request = JudgeExecutionRequest(
            request=request,
            response=response,
        )
        return api_instance.beta_judges_execute_create(
            judge_id=self.id,
            judge_execution_request=execution_request,
            _request_timeout=_request_timeout,
        )


class AJudge(AOpenApiJudge):
    """
    Async wrapper for a single Judge.

    For available attributes, please check the (automatically
    generated) superclass documentation.
    """

    client_context: ClientContextCallable

    @classmethod
    async def _awrap(cls, apiobj: AOpenApiJudge, client_context: ClientContextCallable) -> "AJudge":
        if not isinstance(apiobj, AOpenApiJudge):
            raise ValueError(f"Wrong instance in _wrap: {apiobj!r}")
        obj = cast(AJudge, apiobj)
        obj.__class__ = cls
        obj.client_context = client_context
        return obj

    @with_async_client
    async def arun(
        self,
        *,
        response: str,
        request: Optional[str] = None,
        _request_timeout: Optional[int] = None,
        _client: AApiClient,
    ) -> AJudgeExecutionResponse:
        """
        Asynchronously run the judge.

        Args:
          response: LLM output to evaluate
          request: The prompt sent to the LLM. Optional.
        """
        api_instance = ABetaApi(_client)
        execution_request = AJudgeExecutionRequest(
            request=request,
            response=response,
        )
        return await api_instance.beta_judges_execute_create(
            judge_id=self.id,
            judge_execution_request=execution_request,
            _request_timeout=_request_timeout,
        )


class Judges:
    """
    Judges API

    Note:
        The construction of the API instance should be handled by
        accessing an attribute of a :class:`root.client.RootSignals` instance.
    """

    def __init__(self, client_context: ClientContextCallable):
        self.client_context = client_context

    @with_sync_client
    def create(
        self,
        *,
        name: str,
        evaluator_references: Optional[List[EvaluatorReferenceRequest]] = None,
        _request_timeout: Optional[int] = None,
        _client: ApiClient,
    ) -> Judge:
        """
        Create a new judge.

        Args:
          name: Name of the judge
          evaluator_references: Optional list of evaluator references
        """
        api_instance = BetaApi(_client)
        request = JudgeRequest(
            name=name,
            evaluator_references=evaluator_references,
        )
        judge = api_instance.beta_judges_create(judge_request=request)
        return Judge._wrap(judge, client_context=self.client_context)

    @with_async_client
    async def acreate(
        self,
        *,
        name: str,
        evaluator_references: Optional[List[AEvaluatorReferenceRequest]] = None,
        _request_timeout: Optional[int] = None,
        _client: AApiClient,
    ) -> AJudge:
        """
        Asynchronously create a new judge.

        Args:
          name: Name of the judge
          evaluator_references: Optional list of evaluator references
        """
        api_instance = ABetaApi(_client)
        request = AJudgeRequest(
            name=name,
            evaluator_references=evaluator_references,
        )
        judge = await api_instance.beta_judges_create(judge_request=request)
        return await AJudge._awrap(judge, client_context=self.client_context)

    @with_sync_client
    def get(self, judge_id: str, *, _request_timeout: Optional[int] = None, _client: ApiClient) -> Judge:
        """
        Get a judge by ID.

        Args:
          judge_id: The judge to be fetched.
        """
        api_instance = BetaApi(_client)
        return Judge._wrap(
            api_instance.beta_judges_retrieve(id=judge_id, _request_timeout=_request_timeout),
            client_context=self.client_context,
        )

    @with_async_client
    async def aget(self, judge_id: str, *, _request_timeout: Optional[int] = None, _client: AApiClient) -> AJudge:
        """
        Asynchronously get a judge by ID.

        Args:
          judge_id: The judge to be fetched.
        """
        api_instance = ABetaApi(_client)
        return await AJudge._awrap(
            await api_instance.beta_judges_retrieve(id=judge_id, _request_timeout=_request_timeout),
            client_context=self.client_context,
        )

    @with_sync_client
    def delete(self, judge_id: str, *, _request_timeout: Optional[int] = None, _client: ApiClient) -> None:
        """
        Delete the judge.

        Args:
          judge_id: The judge to be deleted.
        """
        api_instance = BetaApi(_client)
        return api_instance.beta_judges_destroy(id=judge_id, _request_timeout=_request_timeout)

    @with_async_client
    async def adelete(self, judge_id: str, *, _request_timeout: Optional[int] = None, _client: AApiClient) -> None:
        """
        Asynchronously delete the judge.

        Args:
          judge_id: The judge to be deleted.
        """
        api_instance = ABetaApi(_client)
        return await api_instance.beta_judges_destroy(id=judge_id, _request_timeout=_request_timeout)

    @with_sync_client
    def list(self, *, limit: int = 100, _client: ApiClient) -> Iterator[Judge]:
        """
        Iterate through the judges.

        Args:
          limit: Number of entries to iterate through at most.
        """
        api_instance = BetaApi(_client)
        for judge_list in iterate_cursor_list(api_instance.beta_judges_list, limit=limit):  # type: ignore
            for judge in judge_list.results:
                yield Judge._wrap(judge, client_context=self.client_context)

    @with_async_client
    async def alist(self, *, limit: int = 100, _client: AApiClient) -> AsyncIterator[AJudge]:
        """
        Asynchronously iterate through the judges.

        Args:
          limit: Number of entries to iterate through at most.
        """
        api_instance = ABetaApi(_client)
        partial_list = partial(api_instance.beta_judges_list)

        cursor: Optional[StrictStr] = None
        while limit > 0:
            result: APaginatedJudgeListList = await partial_list(page_size=limit, cursor=cursor)
            if not result.results:
                return

            used_results = result.results[:limit]
            limit -= len(used_results)
            for judge in used_results:
                yield await AJudge._awrap(cast(AOpenApiJudge, judge), client_context=self.client_context)

            if not (cursor := result.next):
                return

    @with_sync_client
    def update(
        self,
        judge_id: str,
        *,
        name: Optional[str] = None,
        evaluator_references: Optional[List[EvaluatorReferenceRequest]] = None,
        _request_timeout: Optional[int] = None,
        _client: ApiClient,
    ) -> Judge:
        """
        Update an existing judge.

        Args:
          judge_id: The judge to be updated.
          name: New name for the judge
          evaluator_references: New list of evaluator references
        """
        api_instance = BetaApi(_client)
        request = PatchedJudgeRequest(
            name=name,
            evaluator_references=evaluator_references,
        )
        return Judge._wrap(
            api_instance.beta_judges_partial_update(
                id=judge_id,
                patched_judge_request=request,
                _request_timeout=_request_timeout,
            ),
            client_context=self.client_context,
        )

    @with_async_client
    async def aupdate(
        self,
        judge_id: str,
        *,
        name: Optional[str] = None,
        evaluator_references: Optional[List[AEvaluatorReferenceRequest]] = None,
        _request_timeout: Optional[int] = None,
        _client: AApiClient,
    ) -> AJudge:
        """
        Asynchronously update an existing judge.

        Args:
          judge_id: The judge to be updated.
          name: New name for the judge
          evaluator_references: New list of evaluator references
        """
        api_instance = ABetaApi(_client)
        request = APatchedJudgeRequest(
            name=name,
            evaluator_references=evaluator_references,
        )
        return await AJudge._awrap(
            await api_instance.beta_judges_partial_update(
                id=judge_id,
                patched_judge_request=request,
                _request_timeout=_request_timeout,
            ),
            client_context=self.client_context,
        )
