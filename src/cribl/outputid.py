"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from .sdkconfiguration import SDKConfiguration
from cribl import utils
from cribl.models import components, errors, operations
from typing import Optional, Union

class OutputID:
    sdk_configuration: SDKConfiguration

    def __init__(self, sdk_config: SDKConfiguration) -> None:
        self.sdk_configuration = sdk_config
        
    
    def delete(self, id: str) -> operations.DeleteOutputIDResponse:
        r"""Delete Output
        Delete Output
        """
        request = operations.DeleteOutputIDRequest(
            id=id,
        )
        
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.DeleteOutputIDRequest, base_url, '/system/outputs/{id}', request)
        headers = {}
        headers['Accept'] = 'application/json'
        headers['user-agent'] = self.sdk_configuration.user_agent
        
        client = self.sdk_configuration.security_client
        
        http_res = client.request('DELETE', url, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.DeleteOutputIDResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[components.Outputs])
                res.outputs = out
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

    
    def get(self, id: str) -> operations.GetOutputIDResponse:
        r"""Get Output by ID
        Get Output by ID
        """
        request = operations.GetOutputIDRequest(
            id=id,
        )
        
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.GetOutputIDRequest, base_url, '/system/outputs/{id}', request)
        headers = {}
        headers['Accept'] = 'application/json'
        headers['user-agent'] = self.sdk_configuration.user_agent
        
        client = self.sdk_configuration.security_client
        
        http_res = client.request('GET', url, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetOutputIDResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[components.Outputs])
                res.outputs = out
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

    
    def update(self, id: str, output: Optional[Union[components.OutputDefault, components.OutputWebhook, components.OutputDevnull, components.OutputSyslog, components.OutputSplunk, components.OutputSplunkLb, components.OutputSplunkHec, components.OutputTcpjson, components.OutputWavefront, components.OutputSignalfx, components.OutputFilesystem, components.OutputS3, components.OutputAzureBlob, components.OutputAzureLogs, components.OutputKinesis, components.OutputHoneycomb, components.OutputAzureEventhub, components.OutputGoogleChronicle, components.OutputGoogleCloudStorage, components.OutputGoogleCloudLogging, components.OutputGooglePubsub, components.OutputKafka, components.OutputConfluentCloud, components.OutputMsk, components.OutputElastic, components.OutputNewrelic, components.OutputNewrelicEvents, components.OutputInfluxdb, components.OutputCloudwatch, components.OutputMinio, components.OutputStatsd, components.OutputStatsdExt, components.OutputGraphite, components.OutputRouter, components.OutputSns, components.OutputSqs, components.OutputSnmp, components.OutputSumoLogic, components.OutputDatadog, Union[components.OutputGrafanaCloud1, components.OutputGrafanaCloud2], components.OutputLoki, components.OutputPrometheus, components.OutputRing, components.OutputOpenTelemetry, components.OutputDataset, components.OutputCriblTCP, components.OutputCriblHTTP, components.OutputHumioHec, components.OutputDlS3, components.OutputSecurityLake]] = None) -> operations.UpdateOutputIDResponse:
        r"""Update Output
        Update Output
        """
        request = operations.UpdateOutputIDRequest(
            id=id,
            output=output,
        )
        
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.UpdateOutputIDRequest, base_url, '/system/outputs/{id}', request)
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "output", False, True, 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        headers['Accept'] = 'application/json'
        headers['user-agent'] = self.sdk_configuration.user_agent
        
        client = self.sdk_configuration.security_client
        
        http_res = client.request('PATCH', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.UpdateOutputIDResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[components.Outputs])
                res.outputs = out
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

    