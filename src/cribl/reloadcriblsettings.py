"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from .sdkconfiguration import SDKConfiguration
from cribl import utils
from cribl.models import errors, operations

class ReloadCriblSettings:
    sdk_configuration: SDKConfiguration

    def __init__(self, sdk_config: SDKConfiguration) -> None:
        self.sdk_configuration = sdk_config
        
    
    
    def post(self) -> operations.PostReloadCriblSettingsResponse:
        r"""Reload Cribl settings from the filesystem"""
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = base_url + '/system/settings/reload'
        headers = {}
        headers['Accept'] = '*/*'
        headers['user-agent'] = self.sdk_configuration.user_agent
        
        if callable(self.sdk_configuration.security):
            client = utils.configure_security_client(self.sdk_configuration.client, self.sdk_configuration.security())
        else:
            client = utils.configure_security_client(self.sdk_configuration.client, self.sdk_configuration.security)
        
        http_res = client.request('POST', url, headers=headers)
        content_type = http_res.headers.get('Content-Type')
        
        res = operations.PostReloadCriblSettingsResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            pass
        elif http_res.status_code >= 400 and http_res.status_code < 500 or http_res.status_code == 500 or http_res.status_code >= 500 and http_res.status_code < 600:
            raise errors.SDKError('API error occurred', http_res.status_code, http_res.text, http_res)

        return res

    