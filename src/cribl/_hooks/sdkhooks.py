"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

import requests
from .types import SDKInitHook, BeforeRequestContext, BeforeRequestHook, AfterSuccessContext, AfterSuccessHook, AfterErrorContext, AfterErrorHook, Hooks
from typing import List, Optional, Tuple, Union


class SDKHooks(Hooks):
    sdk_init_hooks: List[SDKInitHook] = []
    before_request_hooks: List[BeforeRequestHook] = []
    after_success_hooks: List[AfterSuccessHook] = []
    after_error_hooks: List[AfterErrorHook] = []

    def __init__(self):
        pass

    def register_sdk_init_hook(self, hook: SDKInitHook) -> None:
        self.sdk_init_hooks.append(hook)

    def register_before_request_hook(self, hook: BeforeRequestHook) -> None:
        self.before_request_hooks.append(hook)

    def register_after_success_hook(self, hook: AfterSuccessHook) -> None:
        self.after_success_hooks.append(hook)

    def register_after_error_hook(self, hook: AfterErrorHook) -> None:
        self.after_error_hooks.append(hook)

    def sdk_init(self, base_url: str, client: requests.Session) -> Tuple[str, requests.Session]:
        for hook in self.sdk_init_hooks:
            base_url, client = hook.sdk_init(base_url, client)
        return base_url, client

    def before_request(self, hook_ctx: BeforeRequestContext, request: requests.PreparedRequest) -> Union[requests.PreparedRequest, Exception]:
        for hook in self.before_request_hooks:
            request = hook.before_request(hook_ctx, request)
            if isinstance(request, Exception):
                raise request

        return request

    def after_success(self, hook_ctx: AfterSuccessContext, response: requests.Response) -> requests.Response:
        for hook in self.after_success_hooks:
            response = hook.after_success(hook_ctx, response)
            if isinstance(response, Exception):
                raise response
        return response

    def after_error(self, hook_ctx: AfterErrorContext, response: Optional[requests.Response], error: Optional[Exception]) -> Tuple[Optional[requests.Response], Optional[Exception]]:
        for hook in self.after_error_hooks:
            result = hook.after_error(hook_ctx, response, error)
            if isinstance(result, Exception):
                raise result
            response, error = result
        return response, error
