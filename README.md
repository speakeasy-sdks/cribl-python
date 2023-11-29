<div align="center">
    <img src="https://github.com/speakeasy-sdks/cribl-demo-go/assets/68016351/3c85f178-5ab2-4679-b0a7-c31ecdcce367" width="350px">
    <h1>Cribl Python SDK</h1>
   <p></p>
   <a href="https://docs.cribl.io/api/"><img src="https://img.shields.io/static/v1?label=Docs&message=API Ref&color=000&style=for-the-badge" /></a>
<!--    <a href="https://github.com/speakeasy-sdks/cribl-python/actions"><img src="https://img.shields.io/github/actions/workflow/status/speakeasy-sdks/cribl-python/speakeasy_sdk_generation.yml?style=for-the-badge" /></a> -->
  <a href="https://opensource.org/licenses/MIT"><img src="https://img.shields.io/badge/License-MIT-blue.svg?style=for-the-badge" /></a>
  <a href="https://github.com/speakeasy-sdks/cribl-python/releases"><img src="https://img.shields.io/github/v/release/speakeasy-sdks/cribl-demo-go?sort=semver&style=for-the-badge" /></a>
</div>

## Authentication
Please fetch a Bearer token for the Cribl Cloud free tier [here](https://docs.cribl.io/stream/api-tutorials/#criblcloud-free-tier)

<!-- Start SDK Installation [installation] -->
## SDK Installation

```bash
pip install cribl
```
<!-- End SDK Installation [installation] -->

<!-- Start SDK Example Usage [usage] -->
## SDK Example Usage

### Example

```python
import cribl
from cribl.models import operations

s = cribl.Cribl(
    bearer_auth="",
)


res = s.idp_auth.get(code='string', state='string')

if res.success is not None:
    # handle response
    pass
```
<!-- End SDK Example Usage [usage] -->

<!-- Start Available Resources and Operations [operations] -->
## Available Resources and Operations

### [idp_auth](docs/sdks/idpauth/README.md)

* [get](docs/sdks/idpauth/README.md#get) - Get IDP used for an authorization code callback

### [list_auth_group](docs/sdks/listauthgroup/README.md)

* [get](docs/sdks/listauthgroup/README.md#get) - List the external authentication system's groups

### [auth_token](docs/sdks/authtoken/README.md)

* [login](docs/sdks/authtoken/README.md#login) - Log in and obtain Auth token

### [user_auth](docs/sdks/userauth/README.md)

* [logout](docs/sdks/userauth/README.md#logout) - Log current user out

### [cribl_metadata](docs/sdks/criblmetadata/README.md)

* [get](docs/sdks/criblmetadata/README.md#get) - Obtain metadata which Cribl Stream/Edge uses when acting as a Service Provider

### [redirect_user_auth](docs/sdks/redirectuserauth/README.md)

* [logout](docs/sdks/redirectuserauth/README.md#logout) - Redirect user to IDP with logout request

### [request_user_auth](docs/sdks/requestuserauth/README.md)

* [logout](docs/sdks/requestuserauth/README.md#logout) - API call that the IDP should use for a logout request

### [idp_user_auth](docs/sdks/idpuserauth/README.md)

* [logout](docs/sdks/idpuserauth/README.md#logout) - Accepts a logout request from an IDP and logs out the user

### [redirect_info](docs/sdks/redirectinfo/README.md)

* [get](docs/sdks/redirectinfo/README.md#get) - Obtain redirect information

### [request_auth](docs/sdks/requestauth/README.md)

* [get](docs/sdks/requestauth/README.md#get) - Accepts an authentication request from an IDP and authenticates the user
* [post](docs/sdks/requestauth/README.md#post) - API call that the IDP should use for an authentication request

### [authorizations](docs/sdks/authorizations/README.md)

* [get](docs/sdks/authorizations/README.md#get) - get the client's authorization policy

### [client_roles](docs/sdks/clientroles/README.md)

* [get](docs/sdks/clientroles/README.md#get) - get the client's roles

### [changelogs](docs/sdks/changelogs/README.md)

* [get](docs/sdks/changelogs/README.md#get) - Get changelog viewed state

### [changelog_view_state](docs/sdks/changelogviewstate/README.md)

* [update](docs/sdks/changelogviewstate/README.md#update) - Update changelog viewed state

### [cluis](docs/sdks/cluis/README.md)

* [get](docs/sdks/cluis/README.md#get) - Get CLUI search results

### [collector_object](docs/sdks/collectorobject/README.md)

* [get](docs/sdks/collectorobject/README.md#get) - Get a list of Collector objects

### [collector](docs/sdks/collector/README.md)

* [get](docs/sdks/collector/README.md#get) - Get Collector by ID

### [conditions](docs/sdks/conditions/README.md)

* [get](docs/sdks/conditions/README.md#get) - Get a list of Condition objects

### [condition](docs/sdks/condition/README.md)

* [get](docs/sdks/condition/README.md#get) - Get Condition by ID

### [list_container_detail](docs/sdks/listcontainerdetail/README.md)

* [get](docs/sdks/listcontainerdetail/README.md#get) - Get a detailed list of containers running on the edge host.

### [container](docs/sdks/container/README.md)

* [get](docs/sdks/container/README.md#get) - Get details for a single container on the edge host. Add stream=true to get a stream instead.

### [configured_collectors](docs/sdks/configuredcollectors/README.md)

* [get](docs/sdks/configuredcollectors/README.md#get) - Get list of configured collectors

### [events](docs/sdks/events/README.md)

* [get](docs/sdks/events/README.md#get) - Get events generated by a specified source

### [bytes](docs/sdks/bytes/README.md)

* [get](docs/sdks/bytes/README.md#get) - Get some number of bytes from the file at the given path

### [edge_host_files](docs/sdks/edgehostfiles/README.md)

* [get](docs/sdks/edgehostfiles/README.md#get) - Get details about a file on the edge host.

### [log_file_list](docs/sdks/logfilelist/README.md)

* [get](docs/sdks/logfilelist/README.md#get) - list log files

### [edge_listing](docs/sdks/edgelisting/README.md)

* [get](docs/sdks/edgelisting/README.md#get) - Get a directory listing of the given path

### [host_metadata_structure](docs/sdks/hostmetadatastructure/README.md)

* [get](docs/sdks/hostmetadatastructure/README.md#get) - Get the host's metadata structure

### [list_process_running_detail](docs/sdks/listprocessrunningdetail/README.md)

* [get](docs/sdks/listprocessrunningdetail/README.md#get) - Get a detailed list of processes running on the edge host

### [process_running_detail](docs/sdks/processrunningdetail/README.md)

* [get](docs/sdks/processrunningdetail/README.md#get) - Get details of a process running on the edge host

### [executor_object](docs/sdks/executorobject/README.md)

* [get](docs/sdks/executorobject/README.md#get) - Get a list of Executor objects

### [executor_id](docs/sdks/executorid/README.md)

* [get](docs/sdks/executorid/README.md#get) - Get Executor by ID

### [fleet_mappings](docs/sdks/fleetmappings/README.md)

* [get](docs/sdks/fleetmappings/README.md#get) - Get a list of MappingRuleset objects

### [fleet_mapping](docs/sdks/fleetmapping/README.md)

* [create](docs/sdks/fleetmapping/README.md#create) - Create MappingRuleset

### [mapping_ruleset](docs/sdks/mappingruleset/README.md)

* [create](docs/sdks/mappingruleset/README.md#create) - Create MappingRuleset
* [delete](docs/sdks/mappingruleset/README.md#delete) - Delete MappingRuleset
* [get](docs/sdks/mappingruleset/README.md#get) - Get MappingRuleset by ID
* [update](docs/sdks/mappingruleset/README.md#update) - Update MappingRuleset

### [mapping_rulesets](docs/sdks/mappingrulesets/README.md)

* [delete](docs/sdks/mappingrulesets/README.md#delete) - Delete MappingRuleset
* [get](docs/sdks/mappingrulesets/README.md#get) - Get a list of MappingRuleset objects
* [update](docs/sdks/mappingrulesets/README.md#update) - Update MappingRuleset

### [object_function](docs/sdks/objectfunction/README.md)

* [get](docs/sdks/objectfunction/README.md#get) - Get a list of Function objects

### [function_id](docs/sdks/functionid/README.md)

* [get](docs/sdks/functionid/README.md#get) - Get Function by ID

### [health_info](docs/sdks/healthinfo/README.md)

* [get](docs/sdks/healthinfo/README.md#get) - Provides health info for REST server

### [job](docs/sdks/job/README.md)

* [cancel](docs/sdks/job/README.md#cancel) - Cancel a job by instance id
* [delete](docs/sdks/job/README.md#delete) - Remove job from job inspector by instance id
* [get](docs/sdks/job/README.md#get) - Get job info by instance id
* [pause_job](docs/sdks/job/README.md#pause_job) - Pause a job by instance id
* [prevent](docs/sdks/job/README.md#prevent) - prevent job from being deleted automatically
* [resume](docs/sdks/job/README.md#resume) - Resume a job by instance id
* [run_job](docs/sdks/job/README.md#run_job) - Run or schedule a job

### [job_infos](docs/sdks/jobinfos/README.md)

* [get](docs/sdks/jobinfos/README.md#get) - Get info on jobs

### [task_error](docs/sdks/taskerror/README.md)

* [get](docs/sdks/taskerror/README.md#get) - Get Task errors for a job by id

### [task_errors](docs/sdks/taskerrors/README.md)

* [get](docs/sdks/taskerrors/README.md#get) - Get Task errors for a job by id

### [job_results](docs/sdks/jobresults/README.md)

* [get](docs/sdks/jobresults/README.md#get) - Get results for a discover job by instance id

### [job_result](docs/sdks/jobresult/README.md)

* [get](docs/sdks/jobresult/README.md#get) - Get results for a discover job by instance id

### [appscope_lib_entries](docs/sdks/appscopelibentries/README.md)

* [get](docs/sdks/appscopelibentries/README.md#get) - Get a list of AppscopeLibEntry objects

### [appscope_lib_entry](docs/sdks/appscopelibentry/README.md)

* [create](docs/sdks/appscopelibentry/README.md#create) - Create AppscopeLibEntry
* [delete](docs/sdks/appscopelibentry/README.md#delete) - Delete AppscopeLibEntry
* [get](docs/sdks/appscopelibentry/README.md#get) - Get AppscopeLibEntry by ID
* [update](docs/sdks/appscopelibentry/README.md#update) - Update AppscopeLibEntry

### [list_event_breaker](docs/sdks/listeventbreaker/README.md)

* [get](docs/sdks/listeventbreaker/README.md#get) - Get a list of Event Breaker Ruleset objects

### [event_breaker](docs/sdks/eventbreaker/README.md)

* [delete](docs/sdks/eventbreaker/README.md#delete) - Delete Event Breaker Ruleset
* [post](docs/sdks/eventbreaker/README.md#post) - Create Event Breaker Ruleset
* [update](docs/sdks/eventbreaker/README.md#update) - Update Event Breaker Ruleset

### [event_breaker_id](docs/sdks/eventbreakerid/README.md)

* [get](docs/sdks/eventbreakerid/README.md#get) - Get Event Breaker Ruleset by ID

### [list_database_connection](docs/sdks/listdatabaseconnection/README.md)

* [get](docs/sdks/listdatabaseconnection/README.md#get) - Get a list of DatabaseConnection objects

### [database_connection](docs/sdks/databaseconnection/README.md)

* [post](docs/sdks/databaseconnection/README.md#post) - Create DatabaseConnectionConfig

### [test_database_connection](docs/sdks/testdatabaseconnection/README.md)

* [post](docs/sdks/testdatabaseconnection/README.md#post) - Test a database connection given a type and connectionString

### [database_connection_config_id](docs/sdks/databaseconnectionconfigid/README.md)

* [delete](docs/sdks/databaseconnectionconfigid/README.md#delete) - Delete DatabaseConnectionConfig
* [get](docs/sdks/databaseconnectionconfigid/README.md#get) - Get DatabaseConnectionConfig by ID
* [update](docs/sdks/databaseconnectionconfigid/README.md#update) - Update DatabaseConnectionConfig

### [javascript_expression](docs/sdks/javascriptexpression/README.md)

* [post](docs/sdks/javascriptexpression/README.md#post) - Evaluate JavaScript expression

### [grok_files](docs/sdks/grokfiles/README.md)

* [get](docs/sdks/grokfiles/README.md#get) - Get a list of GrokFile objects

### [grok_file](docs/sdks/grokfile/README.md)

* [create](docs/sdks/grokfile/README.md#create) - Create GrokFile
* [delete](docs/sdks/grokfile/README.md#delete) - Delete GrokFile
* [get](docs/sdks/grokfile/README.md#get) - Get GrokFile by ID
* [update](docs/sdks/grokfile/README.md#update) - Update GrokFile

### [saved_jobs](docs/sdks/savedjobs/README.md)

* [create](docs/sdks/savedjobs/README.md#create) - Create SavedJob
* [get](docs/sdks/savedjobs/README.md#get) - Get a list of SavedJob objects

### [saved_job](docs/sdks/savedjob/README.md)

* [delete](docs/sdks/savedjob/README.md#delete) - Delete SavedJob
* [get](docs/sdks/savedjob/README.md#get) - Get SavedJob by ID
* [update](docs/sdks/savedjob/README.md#update) - Update SavedJob

### [list_schema](docs/sdks/listschema/README.md)

* [get](docs/sdks/listschema/README.md#get) - Get a list of Schema objects

### [schema](docs/sdks/schema/README.md)

* [create](docs/sdks/schema/README.md#create) - Create Schema
* [delete](docs/sdks/schema/README.md#delete) - Delete Schema
* [get](docs/sdks/schema/README.md#get) - Get Schema by ID
* [post](docs/sdks/schema/README.md#post) - Create Schema
* [update](docs/sdks/schema/README.md#update) - Update Schema

### [schema_id](docs/sdks/schemaid/README.md)

* [delete](docs/sdks/schemaid/README.md#delete) - Delete Schema
* [get](docs/sdks/schemaid/README.md#get) - Get Schema by ID
* [update](docs/sdks/schemaid/README.md#update) - Update Schema

### [list_parser](docs/sdks/listparser/README.md)

* [get](docs/sdks/listparser/README.md#get) - Get a list of Parser objects

### [parser_object](docs/sdks/parserobject/README.md)

* [post](docs/sdks/parserobject/README.md#post) - Create Parser

### [parser_id](docs/sdks/parserid/README.md)

* [delete](docs/sdks/parserid/README.md#delete) - Delete Parser
* [get](docs/sdks/parserid/README.md#get) - Get Parser by ID
* [update](docs/sdks/parserid/README.md#update) - Update Parser

### [regex_lib_entry_object](docs/sdks/regexlibentryobject/README.md)

* [get](docs/sdks/regexlibentryobject/README.md#get) - Get a list of RegexLibEntry objects

### [regex_lib_entry](docs/sdks/regexlibentry/README.md)

* [delete](docs/sdks/regexlibentry/README.md#delete) - Delete RegexLibEntry
* [post](docs/sdks/regexlibentry/README.md#post) - Create RegexLibEntry
* [update](docs/sdks/regexlibentry/README.md#update) - Update RegexLibEntry

### [regex_lib_entry_id](docs/sdks/regexlibentryid/README.md)

* [get](docs/sdks/regexlibentryid/README.md#get) - Get RegexLibEntry by ID

### [schemas](docs/sdks/schemas/README.md)

* [get](docs/sdks/schemas/README.md#get) - Get a list of Schema objects

### [list_global_variable](docs/sdks/listglobalvariable/README.md)

* [get](docs/sdks/listglobalvariable/README.md#get) - Get a list of Global Variable objects

### [global_variable](docs/sdks/globalvariable/README.md)

* [post](docs/sdks/globalvariable/README.md#post) - Create Global Variable

### [global_variable_id](docs/sdks/globalvariableid/README.md)

* [delete](docs/sdks/globalvariableid/README.md#delete) - Delete Global Variable
* [get](docs/sdks/globalvariableid/README.md#get) - Get Global Variable by ID
* [update](docs/sdks/globalvariableid/README.md#update) - Update Global Variable

### [mapping_ruleset_id](docs/sdks/mappingrulesetid/README.md)

* [get](docs/sdks/mappingrulesetid/README.md#get) - Get MappingRuleset by ID

### [diag_bundles](docs/sdks/diagbundles/README.md)

* [get](docs/sdks/diagbundles/README.md#get) - Get list of existing diag bundles

### [groups](docs/sdks/groups/README.md)

* [get](docs/sdks/groups/README.md#get) - Get a list of ConfigGroup objects

### [config_group](docs/sdks/configgroup/README.md)

* [create](docs/sdks/configgroup/README.md#create) - Create ConfigGroup
* [delete](docs/sdks/configgroup/README.md#delete) - Delete ConfigGroup
* [get](docs/sdks/configgroup/README.md#get) - Get a specific ConfigGroup object
* [update](docs/sdks/configgroup/README.md#update) - Update ConfigGroup

### [group_bundle](docs/sdks/groupbundle/README.md)

* [get](docs/sdks/groupbundle/README.md#get) - Get effective bundle version for given Group

### [fleet_or_worker_group](docs/sdks/fleetorworkergroup/README.md)

* [deploy](docs/sdks/fleetorworkergroup/README.md#deploy) - Deploy commits for a Fleet or Worker Group

### [distributed_deployment](docs/sdks/distributeddeployment/README.md)

* [get](docs/sdks/distributeddeployment/README.md#get) - Get summary of Distributed deployment

### [worker_edge_nodes_count](docs/sdks/workeredgenodescount/README.md)

* [get](docs/sdks/workeredgenodescount/README.md#get) - get worker and edge nodes count

### [worker_edge_nodes](docs/sdks/workeredgenodes/README.md)

* [get](docs/sdks/workeredgenodes/README.md#get) - get worker and edge nodes
* [restarts](docs/sdks/workeredgenodes/README.md#restarts) - restarts worker nodes

### [notification_targets](docs/sdks/notificationtargets/README.md)

* [get](docs/sdks/notificationtargets/README.md#get) - Get a list of NotificationTarget objects

### [notification_target](docs/sdks/notificationtarget/README.md)

* [create](docs/sdks/notificationtarget/README.md#create) - Create NotificationTarget
* [delete](docs/sdks/notificationtarget/README.md#delete) - Delete NotificationTarget
* [get](docs/sdks/notificationtarget/README.md#get) - Get NotificationTarget by ID
* [update](docs/sdks/notificationtarget/README.md#update) - Update NotificationTarget

### [pack](docs/sdks/pack/README.md)

* [clone](docs/sdks/pack/README.md#clone) - Clone Pack
* [export](docs/sdks/pack/README.md#export) - Export Pack
* [install](docs/sdks/pack/README.md#install) - Install Pack
* [uninstall](docs/sdks/pack/README.md#uninstall) - Uninstall Pack from the system
* [upgrade](docs/sdks/pack/README.md#upgrade) - Upgrade Pack
* [upload](docs/sdks/pack/README.md#upload) - Upload Pack

### [packs](docs/sdks/packs/README.md)

* [get](docs/sdks/packs/README.md#get) - Get info on packs

### [pipeline_object](docs/sdks/pipelineobject/README.md)

* [get](docs/sdks/pipelineobject/README.md#get) - Get a list of Pipeline objects

### [create_pipeline](docs/sdks/createpipeline/README.md)

* [post](docs/sdks/createpipeline/README.md#post) - Create Pipeline

### [pipeline_id](docs/sdks/pipelineid/README.md)

* [delete](docs/sdks/pipelineid/README.md#delete) - Delete Pipeline
* [get](docs/sdks/pipelineid/README.md#get) - Get Pipeline by ID
* [update](docs/sdks/pipelineid/README.md#update) - Update Pipeline

### [sample_events](docs/sdks/sampleevents/README.md)

* [post](docs/sdks/sampleevents/README.md#post) - Sends sample events through a pipeline and returns the results

### [route_lists](docs/sdks/routelists/README.md)

* [get](docs/sdks/routelists/README.md#get) - List all routes

### [route_list_id](docs/sdks/routelistid/README.md)

* [get](docs/sdks/routelistid/README.md#get) - List all routes by id

### [route_object](docs/sdks/routeobject/README.md)

* [update](docs/sdks/routeobject/README.md#update) - Add, delete or update the routes with the required content.

### [datasets](docs/sdks/datasets/README.md)

* [get](docs/sdks/datasets/README.md#get) - Get a list of DatasetProviderType objects

### [dataset](docs/sdks/dataset/README.md)

* [create](docs/sdks/dataset/README.md#create) - Create DatasetProviderType
* [delete](docs/sdks/dataset/README.md#delete) - Delete DatasetProviderType
* [get](docs/sdks/dataset/README.md#get) - Get DatasetProviderType by ID
* [update](docs/sdks/dataset/README.md#update) - Update DatasetProviderType

### [dataset_objects](docs/sdks/datasetobjects/README.md)

* [get](docs/sdks/datasetobjects/README.md#get) - Get a list of Dataset objects

### [dataset_object](docs/sdks/datasetobject/README.md)

* [create](docs/sdks/datasetobject/README.md#create) - Create Dataset
* [delete](docs/sdks/datasetobject/README.md#delete) - Delete Dataset
* [get](docs/sdks/datasetobject/README.md#get) - Get Dataset by ID
* [update](docs/sdks/datasetobject/README.md#update) - Update Dataset

### [search_doc](docs/sdks/searchdoc/README.md)

* [get](docs/sdks/searchdoc/README.md#get) - Get Search documentation

### [event_breaker_on_data](docs/sdks/eventbreakerondata/README.md)

* [post](docs/sdks/eventbreakerondata/README.md#post) - Runs an event breaker rule on the specified data

### [search_jobs](docs/sdks/searchjobs/README.md)

* [get](docs/sdks/searchjobs/README.md#get) - Get a list of SearchJob objects

### [search_job](docs/sdks/searchjob/README.md)

* [create](docs/sdks/searchjob/README.md#create) - Create SearchJob
* [delete](docs/sdks/searchjob/README.md#delete) - Delete SearchJob
* [get](docs/sdks/searchjob/README.md#get) - Get SearchJob by ID
* [update](docs/sdks/searchjob/README.md#update) - Update SearchJob

### [search](docs/sdks/search/README.md)

* [dispatch_search](docs/sdks/search/README.md#dispatch_search) - Dispatch search *id* to worker nodes filtered by worker node filter using RPC

### [field_summaries](docs/sdks/fieldsummaries/README.md)

* [get](docs/sdks/fieldsummaries/README.md#get) - List field summaries

### [search_logs](docs/sdks/searchlogs/README.md)

* [get](docs/sdks/searchlogs/README.md#get) - Get search logs

### [search_job_metrics](docs/sdks/searchjobmetrics/README.md)

* [get](docs/sdks/searchjobmetrics/README.md#get) - Get search job metrics

### [job_status](docs/sdks/jobstatus/README.md)

* [get](docs/sdks/jobstatus/README.md#get) - Get job status

### [search_timeline](docs/sdks/searchtimeline/README.md)

* [get](docs/sdks/searchtimeline/README.md#get) - Get search timeline

### [query_snippet](docs/sdks/querysnippet/README.md)

* [apply](docs/sdks/querysnippet/README.md#apply) - Applies a query snippet on a set of input events for preview

### [saved_queries](docs/sdks/savedqueries/README.md)

* [create](docs/sdks/savedqueries/README.md#create) - Create SavedQuery
* [delete](docs/sdks/savedqueries/README.md#delete) - Delete SavedQuery
* [get](docs/sdks/savedqueries/README.md#get) - Get a list of SavedQuery objects
* [update](docs/sdks/savedqueries/README.md#update) - Update SavedQuery

### [saved_query](docs/sdks/savedquery/README.md)

* [get](docs/sdks/savedquery/README.md#get) - Get SavedQuery by ID

### [trust_policies](docs/sdks/trustpolicies/README.md)

* [get](docs/sdks/trustpolicies/README.md#get) - Get a list of TrustPolicy objects

### [kms_config](docs/sdks/kmsconfig/README.md)

* [get](docs/sdks/kmsconfig/README.md#get) - Get Cribl KMS config
* [update](docs/sdks/kmsconfig/README.md#update) - Update Cribl KMS config

### [kms_health](docs/sdks/kmshealth/README.md)

* [get](docs/sdks/kmshealth/README.md#get) - Get Cribl KMS health

### [features](docs/sdks/features/README.md)

* [get](docs/sdks/features/README.md#get) - List all features

### [feature](docs/sdks/feature/README.md)

* [get](docs/sdks/feature/README.md#get) - Get feature by Id

### [live_data](docs/sdks/livedata/README.md)

* [post](docs/sdks/livedata/README.md#post) - Capture live incoming data

### [certificates](docs/sdks/certificates/README.md)

* [get](docs/sdks/certificates/README.md#get) - Get a list of Certificate objects

### [certificate](docs/sdks/certificate/README.md)

* [create](docs/sdks/certificate/README.md#create) - Create Certificate
* [delete](docs/sdks/certificate/README.md#delete) - Delete Certificate
* [get](docs/sdks/certificate/README.md#get) - Get Certificate by ID
* [update](docs/sdks/certificate/README.md#update) - Update Certificate

### [existing_diag_bundles](docs/sdks/existingdiagbundles/README.md)

* [get](docs/sdks/existingdiagbundles/README.md#get) - Get list of existing diag bundles

### [diag_bundle](docs/sdks/diagbundle/README.md)

* [delete](docs/sdks/diagbundle/README.md#delete) - Remove diag bundle
* [get](docs/sdks/diagbundle/README.md#get) - Returns a diag bundle as a tar.gz archive
* [send](docs/sdks/diagbundle/README.md#send) - Send a diag bundle (tar.gz archive) to Cribl

### [cancel_running_group](docs/sdks/cancelrunninggroup/README.md)

* [post](docs/sdks/cancelrunninggroup/README.md#post) - Cancel a running group upgrade

### [previous_cribl_package](docs/sdks/previouscriblpackage/README.md)

* [get](docs/sdks/previouscriblpackage/README.md#get) - Get the previously downloaded Cribl package

### [stage_distributed_package](docs/sdks/stagedistributedpackage/README.md)

* [post](docs/sdks/stagedistributedpackage/README.md#post) - Stage distributed group upgrade

### [execute_distributed_upgrade](docs/sdks/executedistributedupgrade/README.md)

* [post](docs/sdks/executedistributedupgrade/README.md#post) - Execute distributed group upgrade

### [system_info](docs/sdks/systeminfo/README.md)

* [get](docs/sdks/systeminfo/README.md#get) - Get basic system information

### [log_file_contents](docs/sdks/logfilecontents/README.md)

* [get](docs/sdks/logfilecontents/README.md#get) - Get contents of the log file

### [key_metadata_entities](docs/sdks/keymetadataentities/README.md)

* [get](docs/sdks/keymetadataentities/README.md#get) - Get a list of KeyMetadataEntity objects

### [key_metadata_entity](docs/sdks/keymetadataentity/README.md)

* [create](docs/sdks/keymetadataentity/README.md#create) - Create KeyMetadataEntity
* [delete](docs/sdks/keymetadataentity/README.md#delete) - Delete KeyMetadataEntity
* [get](docs/sdks/keymetadataentity/README.md#get) - Get KeyMetadataEntity by ID
* [update](docs/sdks/keymetadataentity/README.md#update) - Update KeyMetadataEntity

### [licenses](docs/sdks/licenses/README.md)

* [get](docs/sdks/licenses/README.md#get) - Get a list of License objects

### [license](docs/sdks/license/README.md)

* [create](docs/sdks/license/README.md#create) - Create License
* [delete](docs/sdks/license/README.md#delete) - Delete License
* [get](docs/sdks/license/README.md#get) - Get License by ID

### [license_usage_metrics](docs/sdks/licenseusagemetrics/README.md)

* [get](docs/sdks/licenseusagemetrics/README.md#get) - Get license usage metrics, aggregated by day, up to last 90 days

### [logger_configs](docs/sdks/loggerconfigs/README.md)

* [get](docs/sdks/loggerconfigs/README.md#get) - Get a list of LoggerConfig objects

### [logger_config](docs/sdks/loggerconfig/README.md)

* [delete](docs/sdks/loggerconfig/README.md#delete) - Delete LoggerConfig
* [get](docs/sdks/loggerconfig/README.md#get) - Get LoggerConfig by ID
* [update](docs/sdks/loggerconfig/README.md#update) - Update LoggerConfig

### [log_files](docs/sdks/logfiles/README.md)

* [get](docs/sdks/logfiles/README.md#get) - Get a list of log files

### [log_files_content](docs/sdks/logfilescontent/README.md)

* [get](docs/sdks/logfilescontent/README.md#get) - Get contents of the log file

### [log_file_content](docs/sdks/logfilecontent/README.md)

* [get](docs/sdks/logfilecontent/README.md#get) - Get contents of the log file

### [lookups](docs/sdks/lookups/README.md)

* [get](docs/sdks/lookups/README.md#get) - Get a list of LookupFile objects

### [lookup](docs/sdks/lookup/README.md)

* [create](docs/sdks/lookup/README.md#create) - Create LookupFile
* [delete](docs/sdks/lookup/README.md#delete) - Delete LookupFile
* [get](docs/sdks/lookup/README.md#get) - Get LookupFile by ID
* [update](docs/sdks/lookup/README.md#update) - Update LookupFile
* [upload](docs/sdks/lookup/README.md#upload) - Upload LookupFile

### [bulletin_messages](docs/sdks/bulletinmessages/README.md)

* [get](docs/sdks/bulletinmessages/README.md#get) - Get a list of BulletinMessage objects

### [bulletin_message](docs/sdks/bulletinmessage/README.md)

* [create](docs/sdks/bulletinmessage/README.md#create) - Create BulletinMessage
* [delete](docs/sdks/bulletinmessage/README.md#delete) - Delete BulletinMessage
* [get](docs/sdks/bulletinmessage/README.md#get) - Get BulletinMessage by ID

### [metrics](docs/sdks/metrics/README.md)

* [post](docs/sdks/metrics/README.md#post) - Enumerate all internal system metrics
* [query](docs/sdks/metrics/README.md#query) - Query raw internal system metrics

### [internal_system_metrics](docs/sdks/internalsystemmetrics/README.md)

* [post](docs/sdks/internalsystemmetrics/README.md#post) - Aggregate raw internal system metrics

### [output_objects](docs/sdks/outputobjects/README.md)

* [get](docs/sdks/outputobjects/README.md#get) - Get a list of Output objects

### [output_object](docs/sdks/outputobject/README.md)

* [create](docs/sdks/outputobject/README.md#create) - Create Output

### [output_id](docs/sdks/outputid/README.md)

* [delete](docs/sdks/outputid/README.md#delete) - Delete Output
* [get](docs/sdks/outputid/README.md#get) - Get Output by ID
* [update](docs/sdks/outputid/README.md#update) - Update Output

### [destination_queue](docs/sdks/destinationqueue/README.md)

* [delete](docs/sdks/destinationqueue/README.md#delete) - Delete destination persistent queue

### [latest_pq](docs/sdks/latestpq/README.md)

* [get](docs/sdks/latestpq/README.md#get) - Get status of latest clear PQ job for an output

### [specified_output](docs/sdks/specifiedoutput/README.md)

* [get](docs/sdks/specifiedoutput/README.md#get) - Get samples data for the specified output. Used to get sample data for the test action.

### [sample_output](docs/sdks/sampleoutput/README.md)

* [post](docs/sdks/sampleoutput/README.md#post) - Send sample data to an output to validate configuration or test connectivity

### [policy_rules](docs/sdks/policyrules/README.md)

* [get](docs/sdks/policyrules/README.md#get) - Get a list of PolicyRule objects

### [policy_rule](docs/sdks/policyrule/README.md)

* [create](docs/sdks/policyrule/README.md#create) - Create PolicyRule
* [delete](docs/sdks/policyrule/README.md#delete) - Delete PolicyRule
* [get](docs/sdks/policyrule/README.md#get) - Get PolicyRule by ID
* [update](docs/sdks/policyrule/README.md#update) - Update PolicyRule

### [processes](docs/sdks/processes/README.md)

* [get](docs/sdks/processes/README.md#get) - Get a list of processes under management

### [profilers](docs/sdks/profilers/README.md)

* [get](docs/sdks/profilers/README.md#get) - Get a list of ProfilerItem objects

### [profiler](docs/sdks/profiler/README.md)

* [create](docs/sdks/profiler/README.md#create) - Create ProfilerItem
* [delete](docs/sdks/profiler/README.md#delete) - Delete ProfilerItem
* [get](docs/sdks/profiler/README.md#get) - Get ProfilerItem by ID
* [update](docs/sdks/profiler/README.md#update) - Update ProfilerItem

### [roles](docs/sdks/roles/README.md)

* [get](docs/sdks/roles/README.md#get) - Get a list of Role objects

### [role](docs/sdks/role/README.md)

* [create](docs/sdks/role/README.md#create) - Create Role
* [delete](docs/sdks/role/README.md#delete) - Delete Role
* [get](docs/sdks/role/README.md#get) - Get Role by ID
* [update](docs/sdks/role/README.md#update) - Update Role

### [list_data_sample](docs/sdks/listdatasample/README.md)

* [get](docs/sdks/listdatasample/README.md#get) - Get a list of DataSample objects

### [data_sample](docs/sdks/datasample/README.md)

* [post](docs/sdks/datasample/README.md#post) - Create DataSample

### [data_sample_id](docs/sdks/datasampleid/README.md)

* [delete](docs/sdks/datasampleid/README.md#delete) - Delete DataSample
* [get](docs/sdks/datasampleid/README.md#get) - Get DataSample by ID
* [update](docs/sdks/datasampleid/README.md#update) - Update DataSample

### [sample_content](docs/sdks/samplecontent/README.md)

* [get](docs/sdks/samplecontent/README.md#get) - Get sample content by ID

### [scripts](docs/sdks/scripts/README.md)

* [get](docs/sdks/scripts/README.md#get) - Get a list of Script objects

### [script](docs/sdks/script/README.md)

* [create](docs/sdks/script/README.md#create) - Create Script
* [delete](docs/sdks/script/README.md#delete) - Delete Script
* [get](docs/sdks/script/README.md#get) - Get Script by ID
* [update](docs/sdks/script/README.md#update) - Update Script

### [rest_secrets](docs/sdks/restsecrets/README.md)

* [get](docs/sdks/restsecrets/README.md#get) - Get a list of RestSecret objects

### [rest_secret](docs/sdks/restsecret/README.md)

* [create](docs/sdks/restsecret/README.md#create) - Create RestSecret
* [delete](docs/sdks/restsecret/README.md#delete) - Delete RestSecret
* [get](docs/sdks/restsecret/README.md#get) - Get RestSecret by ID
* [update](docs/sdks/restsecret/README.md#update) - Update RestSecret

### [cribls_settings](docs/sdks/criblssettings/README.md)

* [~~get~~](docs/sdks/criblssettings/README.md#get) - Get Cribl system settings. Deprecated: use specific endpoints /system/limits, /system/job-limits, /system/redis-cache-limits, /system/services-limits, /system/settings/git-settings, and /system/settings/conf respectively :warning: **Deprecated**
* [~~update~~](docs/sdks/criblssettings/README.md#update) - Update Cribl system settings. Deprecated: use specific endpoints /system/limits, /system/job-limits, /system/settings/git-settings, /system/settings/auth and /system/settings/conf respectively :warning: **Deprecated**

### [authentication_settings](docs/sdks/authenticationsettings/README.md)

* [get](docs/sdks/authenticationsettings/README.md#get) - Get authentication settings
* [update](docs/sdks/authenticationsettings/README.md#update) - Update authentication settings

### [cribl_system_settings](docs/sdks/criblsystemsettings/README.md)

* [get](docs/sdks/criblsystemsettings/README.md#get) - Get Cribl system settings
* [update](docs/sdks/criblsystemsettings/README.md#update) - Update Cribl system settings

### [git_settings](docs/sdks/gitsettings/README.md)

* [get](docs/sdks/gitsettings/README.md#get) - Get git settings
* [update](docs/sdks/gitsettings/README.md#update) - Update git settings

### [reload_cribl_settings](docs/sdks/reloadcriblsettings/README.md)

* [post](docs/sdks/reloadcriblsettings/README.md#post) - Reload Cribl settings from the filesystem

### [restart_cribl_settings](docs/sdks/restartcriblsettings/README.md)

* [post](docs/sdks/restartcriblsettings/README.md#post) - Restart Cribl server

### [search_limits](docs/sdks/searchlimits/README.md)

* [get](docs/sdks/searchlimits/README.md#get) - Get search limits

### [list_cribl_version](docs/sdks/listcriblversion/README.md)

* [get](docs/sdks/listcriblversion/README.md#get) - Get a list of Cribl versions available for upgrade

### [master_node_package](docs/sdks/masternodepackage/README.md)

* [post](docs/sdks/masternodepackage/README.md#post) - Upgrade master node with the provided package

### [give_cribl_version](docs/sdks/givecriblversion/README.md)

* [post](docs/sdks/givecriblversion/README.md#post) - Upgrade Cribl to a given version

### [output_status](docs/sdks/outputstatus/README.md)

* [get](docs/sdks/outputstatus/README.md#get) - Get a list of OutputStatus objects

### [output_status_id](docs/sdks/outputstatusid/README.md)

* [get](docs/sdks/outputstatusid/README.md#get) - Get OutputStatus by ID

### [user_object](docs/sdks/userobject/README.md)

* [get](docs/sdks/userobject/README.md#get) - Get a list of User objects
* [update](docs/sdks/userobject/README.md#update) - Update User except for their roles

### [user](docs/sdks/user/README.md)

* [create_user](docs/sdks/user/README.md#create_user) - Create User

### [user_id](docs/sdks/userid/README.md)

* [delete](docs/sdks/userid/README.md#delete) - Delete User
* [get](docs/sdks/userid/README.md#get) - Get User by ID

### [user_properties](docs/sdks/userproperties/README.md)

* [update](docs/sdks/userproperties/README.md#update) - Update User properties – admin use only

### [ui_state](docs/sdks/uistate/README.md)

* [get](docs/sdks/uistate/README.md#get) - Get UI state by key
* [update](docs/sdks/uistate/README.md#update) - Update UI state by key

### [branches](docs/sdks/branches/README.md)

* [get](docs/sdks/branches/README.md#get) - get the list of branches

### [commit](docs/sdks/commit/README.md)

* [create](docs/sdks/commit/README.md#create) - create a new commit containing the current configs the given log message describing the changes.

### [count_file](docs/sdks/countfile/README.md)

* [get](docs/sdks/countfile/README.md#get) - get the count of files of changed

### [textual_diff](docs/sdks/textualdiff/README.md)

* [get](docs/sdks/textualdiff/README.md#get) - get the textual diff for given commit

### [changed_files](docs/sdks/changedfiles/README.md)

* [get](docs/sdks/changedfiles/README.md#get) - get the files changed

### [versioning](docs/sdks/versioning/README.md)

* [get](docs/sdks/versioning/README.md#get) - Get info about versioning availability

### [current_config](docs/sdks/currentconfig/README.md)

* [push](docs/sdks/currentconfig/README.md#push) - push the current configs to the remote repository.

### [logand_textual](docs/sdks/logandtextual/README.md)

* [get](docs/sdks/logandtextual/README.md#get) - get the log message and textual diff for given commit

### [working_tree](docs/sdks/workingtree/README.md)

* [get](docs/sdks/workingtree/README.md#get) - get the the working tree status

### [remote_repo](docs/sdks/remoterepo/README.md)

* [sync](docs/sdks/remoterepo/README.md#sync) - syncs with remote repo via POST requests
<!-- End Available Resources and Operations [operations] -->

<!-- Start Error Handling [errors] -->
## Error Handling

Handling errors in this SDK should largely match your expectations.  All operations return a response object or raise an error.  If Error objects are specified in your OpenAPI Spec, the SDK will raise the appropriate Error type.

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 401              | application/json |
| errors.SDKError  | 400-600          | */*              |

### Example

```python
import cribl
from cribl.models import operations

s = cribl.Cribl(
    bearer_auth="",
)


res = None
try:
    res = s.idp_auth.get(code='string', state='string')
except (errors.Error) as e:
    print(e) # handle exception

except (errors.SDKError) as e:
    print(e) # handle exception


if res.success is not None:
    # handle response
    pass
```
<!-- End Error Handling [errors] --><!-- Start Server Selection [server] -->
## Server Selection

### Select Server by Index

You can override the default server globally by passing a server index to the `server_idx: int` optional parameter when initializing the SDK client instance. The selected server will then be used as the default on the operations that use it. This table lists the indexes associated with the available servers:

| # | Server | Variables |
| - | ------ | --------- |
| 0 | `https://logstream.{organizationID}.cribl.cloud/` | `organizationID` (default is `api`) |

#### Example

```python
import cribl
from cribl.models import operations

s = cribl.Cribl(
    server_idx=0,
    bearer_auth="",
)


res = s.idp_auth.get(code='string', state='string')

if res.success is not None:
    # handle response
    pass
```

#### Variables

Some of the server options above contain variables. If you want to set the values of those variables, the following optional parameters are available when initializing the SDK client instance:
 * `organization_id: str`

### Override Server URL Per-Client

The default server can also be overridden globally by passing a URL to the `server_url: str` optional parameter when initializing the SDK client instance. For example:
```python
import cribl
from cribl.models import operations

s = cribl.Cribl(
    server_url="https://logstream.{organizationID}.cribl.cloud/",
    bearer_auth="",
)


res = s.idp_auth.get(code='string', state='string')

if res.success is not None:
    # handle response
    pass
```
<!-- End Server Selection [server] --><!-- Start Custom HTTP Client [http-client] -->
## Custom HTTP Client

The Python SDK makes API calls using the (requests)[https://pypi.org/project/requests/] HTTP library.  In order to provide a convenient way to configure timeouts, cookies, proxies, custom headers, and other low-level configuration, you can initialize the SDK client with a custom `requests.Session` object.

For example, you could specify a header for every request that this sdk makes as follows:
```python
import cribl
import requests

http_client = requests.Session()
http_client.headers.update({'x-custom-header': 'someValue'})
s = cribl.Cribl(client: http_client)
```
<!-- End Custom HTTP Client [http-client] --><!-- Start Authentication [security] -->
## Authentication

### Per-Client Security Schemes

This SDK supports the following security scheme globally:

| Name          | Type          | Scheme        |
| ------------- | ------------- | ------------- |
| `bearer_auth` | http          | HTTP Bearer   |

To authenticate with the API the `bearer_auth` parameter must be set when initializing the SDK client instance. For example:
```python
import cribl
from cribl.models import operations

s = cribl.Cribl(
    bearer_auth="",
)


res = s.idp_auth.get(code='string', state='string')

if res.success is not None:
    # handle response
    pass
```
<!-- End Authentication [security] --><!-- Placeholder for Future Speakeasy SDK Sections -->



### Maturity

This SDK is in beta, and there may be breaking changes between versions without a major version update. Therefore, we recommend pinning usage
to a specific package version. This way, you can install the same version each time without breaking changes unless you are intentionally
looking for the latest version.

### Contributions

While we value open-source contributions to this SDK, this library is generated programmatically.
Feel free to open a PR or a Github issue as a proof of concept and we'll do our best to include it in a future release!

### SDK Created by [Speakeasy](https://docs.speakeasyapi.dev/docs/using-speakeasy/client-sdks)
