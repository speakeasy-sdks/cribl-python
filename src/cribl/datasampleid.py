"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from .sdkconfiguration import SDKConfiguration
from cribl import utils
from cribl.models import components, errors, operations
from typing import Optional

class DataSampleID:
    sdk_configuration: SDKConfiguration

    def __init__(self, sdk_config: SDKConfiguration) -> None:
        self.sdk_configuration = sdk_config
        
    
    
    def delete(self, id: str) -> operations.DeleteDataSampleIDResponse:
        r"""Delete DataSample
        Delete DataSample
        """
        request = operations.DeleteDataSampleIDRequest(
            id=id,
        )
        
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.DeleteDataSampleIDRequest, base_url, '/system/samples/{id}', request)
        headers = {}
        headers['Accept'] = 'application/json'
        headers['user-agent'] = self.sdk_configuration.user_agent
        
        if callable(self.sdk_configuration.security):
            client = utils.configure_security_client(self.sdk_configuration.client, self.sdk_configuration.security())
        else:
            client = utils.configure_security_client(self.sdk_configuration.client, self.sdk_configuration.security)
        
        http_res = client.request('DELETE', url, headers=headers)
        content_type = http_res.headers.get('Content-Type')
        
        res = operations.DeleteDataSampleIDResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[components.DataSamples])
                res.data_samples = out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code in [401, 500]:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, errors.Error)
                out.raw_response = http_res
                raise out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code >= 400 and http_res.status_code < 500 or http_res.status_code >= 500 and http_res.status_code < 600:
            raise errors.SDKError('API error occurred', http_res.status_code, http_res.text, http_res)

        return res

    
    
    def get(self, id: str) -> operations.GetDataSampleIDResponse:
        r"""Get DataSample by ID
        Get DataSample by ID
        """
        request = operations.GetDataSampleIDRequest(
            id=id,
        )
        
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.GetDataSampleIDRequest, base_url, '/system/samples/{id}', request)
        headers = {}
        headers['Accept'] = 'application/json'
        headers['user-agent'] = self.sdk_configuration.user_agent
        
        if callable(self.sdk_configuration.security):
            client = utils.configure_security_client(self.sdk_configuration.client, self.sdk_configuration.security())
        else:
            client = utils.configure_security_client(self.sdk_configuration.client, self.sdk_configuration.security)
        
        http_res = client.request('GET', url, headers=headers)
        content_type = http_res.headers.get('Content-Type')
        
        res = operations.GetDataSampleIDResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[components.DataSamples])
                res.data_samples = out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code in [401, 500]:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, errors.Error)
                out.raw_response = http_res
                raise out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code >= 400 and http_res.status_code < 500 or http_res.status_code >= 500 and http_res.status_code < 600:
            raise errors.SDKError('API error occurred', http_res.status_code, http_res.text, http_res)

        return res

    
    
    def update(self, id: str, data_sample: Optional[components.DataSample] = None) -> operations.UpdateDataSampleIDResponse:
        r"""Update DataSample
        Update DataSample
        """
        request = operations.UpdateDataSampleIDRequest(
            id=id,
            data_sample=data_sample,
        )
        
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.UpdateDataSampleIDRequest, base_url, '/system/samples/{id}', request)
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "data_sample", False, True, 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        headers['Accept'] = 'application/json'
        headers['user-agent'] = self.sdk_configuration.user_agent
        
        if callable(self.sdk_configuration.security):
            client = utils.configure_security_client(self.sdk_configuration.client, self.sdk_configuration.security())
        else:
            client = utils.configure_security_client(self.sdk_configuration.client, self.sdk_configuration.security)
        
        http_res = client.request('PATCH', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')
        
        res = operations.UpdateDataSampleIDResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[components.DataSamples])
                res.data_samples = out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code in [401, 500]:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, errors.Error)
                out.raw_response = http_res
                raise out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code >= 400 and http_res.status_code < 500 or http_res.status_code >= 500 and http_res.status_code < 600:
            raise errors.SDKError('API error occurred', http_res.status_code, http_res.text, http_res)

        return res

    