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

<!-- Start SDK Installation -->
## SDK Installation

This is SDK is not yet published to PYPI so please clone repo and then run

```bash
pip install -e /path/to/clone/cribl-python
```
<!-- End SDK Installation -->

## SDK Example Usage
<!-- Start SDK Example Usage -->


```python
import cribl
from cribl.models import shared

s = cribl.Cribl(
    security=shared.Security(
        bearer_auth="",
    ),
)


res = s.appscope_lib_entries.get()

if res.app_scope_lib_entries is not None:
    # handle response
```
<!-- End SDK Example Usage -->

<!-- Start SDK Available Operations -->
## Available Resources and Operations


### [appscope_lib_entries](docs/sdks/appscopelibentries/README.md)

* [get](docs/sdks/appscopelibentries/README.md#get) - Get a list of AppscopeLibEntry objects

### [appscope_lib_entry](docs/sdks/appscopelibentry/README.md)

* [create](docs/sdks/appscopelibentry/README.md#create) - Create AppscopeLibEntry
* [delete](docs/sdks/appscopelibentry/README.md#delete) - Delete AppscopeLibEntry
* [get](docs/sdks/appscopelibentry/README.md#get) - Get AppscopeLibEntry by ID
* [update](docs/sdks/appscopelibentry/README.md#update) - Update AppscopeLibEntry

### [auth_token](docs/sdks/authtoken/README.md)

* [login](docs/sdks/authtoken/README.md#login) - Log in and obtain Auth token

### [authentication_settings](docs/sdks/authenticationsettings/README.md)

* [get](docs/sdks/authenticationsettings/README.md#get) - Get authentication settings
* [update](docs/sdks/authenticationsettings/README.md#update) - Update authentication settings

### [authorizations](docs/sdks/authorizations/README.md)

* [get](docs/sdks/authorizations/README.md#get) - get the client's authorization policy

### [branches](docs/sdks/branches/README.md)

* [get](docs/sdks/branches/README.md#get) - get the list of branches

### [bulletin_message](docs/sdks/bulletinmessage/README.md)

* [create](docs/sdks/bulletinmessage/README.md#create) - Create BulletinMessage
* [delete](docs/sdks/bulletinmessage/README.md#delete) - Delete BulletinMessage
* [get](docs/sdks/bulletinmessage/README.md#get) - Get BulletinMessage by ID

### [bulletin_messages](docs/sdks/bulletinmessages/README.md)

* [get](docs/sdks/bulletinmessages/README.md#get) - Get a list of BulletinMessage objects

### [bytes](docs/sdks/bytes/README.md)

* [get](docs/sdks/bytes/README.md#get) - Get some number of bytes from the file at the given path

### [cancel_running_group](docs/sdks/cancelrunninggroup/README.md)

* [post](docs/sdks/cancelrunninggroup/README.md#post) - Cancel a running group upgrade

### [certificate](docs/sdks/certificate/README.md)

* [create](docs/sdks/certificate/README.md#create) - Create Certificate
* [delete](docs/sdks/certificate/README.md#delete) - Delete Certificate
* [get](docs/sdks/certificate/README.md#get) - Get Certificate by ID
* [update](docs/sdks/certificate/README.md#update) - Update Certificate

### [certificates](docs/sdks/certificates/README.md)

* [get](docs/sdks/certificates/README.md#get) - Get a list of Certificate objects

### [changed_files](docs/sdks/changedfiles/README.md)

* [get](docs/sdks/changedfiles/README.md#get) - get the files changed

### [changelog_view_state](docs/sdks/changelogviewstate/README.md)

* [update](docs/sdks/changelogviewstate/README.md#update) - Update changelog viewed state

### [changelogs](docs/sdks/changelogs/README.md)

* [get](docs/sdks/changelogs/README.md#get) - Get changelog viewed state

### [client_roles](docs/sdks/clientroles/README.md)

* [get](docs/sdks/clientroles/README.md#get) - get the client's roles

### [cluis](docs/sdks/cluis/README.md)

* [get](docs/sdks/cluis/README.md#get) - Get CLUI search results

### [collector](docs/sdks/collector/README.md)

* [get](docs/sdks/collector/README.md#get) - Get Collector by ID

### [collector_object](docs/sdks/collectorobject/README.md)

* [get](docs/sdks/collectorobject/README.md#get) - Get a list of Collector objects

### [commit](docs/sdks/commit/README.md)

* [create](docs/sdks/commit/README.md#create) - create a new commit containing the current configs the given log message describing the changes.

### [condition](docs/sdks/condition/README.md)

* [get](docs/sdks/condition/README.md#get) - Get Condition by ID

### [conditions](docs/sdks/conditions/README.md)

* [get](docs/sdks/conditions/README.md#get) - Get a list of Condition objects

### [config_group](docs/sdks/configgroup/README.md)

* [create](docs/sdks/configgroup/README.md#create) - Create ConfigGroup
* [delete](docs/sdks/configgroup/README.md#delete) - Delete ConfigGroup
* [get](docs/sdks/configgroup/README.md#get) - Get a specific ConfigGroup object
* [update](docs/sdks/configgroup/README.md#update) - Update ConfigGroup

### [configured_collectors](docs/sdks/configuredcollectors/README.md)

* [get](docs/sdks/configuredcollectors/README.md#get) - Get list of configured collectors

### [container](docs/sdks/container/README.md)

* [get](docs/sdks/container/README.md#get) - Get details for a single container on the edge host. Add stream=true to get a stream instead.

### [count_file](docs/sdks/countfile/README.md)

* [get](docs/sdks/countfile/README.md#get) - get the count of files of changed

### [create_pipeline](docs/sdks/createpipeline/README.md)

* [post](docs/sdks/createpipeline/README.md#post) - Create Pipeline

### [cribl_metadata](docs/sdks/criblmetadata/README.md)

* [get](docs/sdks/criblmetadata/README.md#get) - Obtain metadata which Cribl Stream/Edge uses when acting as a Service Provider

### [cribl_system_settings](docs/sdks/criblsystemsettings/README.md)

* [get](docs/sdks/criblsystemsettings/README.md#get) - Get Cribl system settings
* [update](docs/sdks/criblsystemsettings/README.md#update) - Update Cribl system settings

### [cribls_settings](docs/sdks/criblssettings/README.md)

* [~~get~~](docs/sdks/criblssettings/README.md#get) - Get Cribl system settings. Deprecated: use specific endpoints /system/limits, /system/job-limits, /system/redis-cache-limits, /system/services-limits, /system/settings/git-settings, and /system/settings/conf respectively :warning: **Deprecated**
* [~~update~~](docs/sdks/criblssettings/README.md#update) - Update Cribl system settings. Deprecated: use specific endpoints /system/limits, /system/job-limits, /system/settings/git-settings, /system/settings/auth and /system/settings/conf respectively :warning: **Deprecated**

### [current_config](docs/sdks/currentconfig/README.md)

* [push](docs/sdks/currentconfig/README.md#push) - push the current configs to the remote repository.

### [data_sample](docs/sdks/datasample/README.md)

* [post](docs/sdks/datasample/README.md#post) - Create DataSample

### [data_sample_id](docs/sdks/datasampleid/README.md)

* [delete](docs/sdks/datasampleid/README.md#delete) - Delete DataSample
* [get](docs/sdks/datasampleid/README.md#get) - Get DataSample by ID
* [update](docs/sdks/datasampleid/README.md#update) - Update DataSample

### [database_connection](docs/sdks/databaseconnection/README.md)

* [post](docs/sdks/databaseconnection/README.md#post) - Create DatabaseConnectionConfig

### [database_connection_config_id](docs/sdks/databaseconnectionconfigid/README.md)

* [delete](docs/sdks/databaseconnectionconfigid/README.md#delete) - Delete DatabaseConnectionConfig
* [get](docs/sdks/databaseconnectionconfigid/README.md#get) - Get DatabaseConnectionConfig by ID
* [update](docs/sdks/databaseconnectionconfigid/README.md#update) - Update DatabaseConnectionConfig

### [dataset](docs/sdks/dataset/README.md)

* [create](docs/sdks/dataset/README.md#create) - Create DatasetProviderType
* [delete](docs/sdks/dataset/README.md#delete) - Delete DatasetProviderType
* [get](docs/sdks/dataset/README.md#get) - Get DatasetProviderType by ID
* [update](docs/sdks/dataset/README.md#update) - Update DatasetProviderType

### [dataset_object](docs/sdks/datasetobject/README.md)

* [create](docs/sdks/datasetobject/README.md#create) - Create Dataset
* [delete](docs/sdks/datasetobject/README.md#delete) - Delete Dataset
* [get](docs/sdks/datasetobject/README.md#get) - Get Dataset by ID
* [update](docs/sdks/datasetobject/README.md#update) - Update Dataset

### [dataset_objects](docs/sdks/datasetobjects/README.md)

* [get](docs/sdks/datasetobjects/README.md#get) - Get a list of Dataset objects

### [datasets](docs/sdks/datasets/README.md)

* [get](docs/sdks/datasets/README.md#get) - Get a list of DatasetProviderType objects

### [destination_queue](docs/sdks/destinationqueue/README.md)

* [delete](docs/sdks/destinationqueue/README.md#delete) - Delete destination persistent queue

### [diag_bundle](docs/sdks/diagbundle/README.md)

* [delete](docs/sdks/diagbundle/README.md#delete) - Remove diag bundle
* [get](docs/sdks/diagbundle/README.md#get) - Returns a diag bundle as a tar.gz archive
* [send](docs/sdks/diagbundle/README.md#send) - Send a diag bundle (tar.gz archive) to Cribl

### [diag_bundles](docs/sdks/diagbundles/README.md)

* [get](docs/sdks/diagbundles/README.md#get) - Get list of existing diag bundles

### [distributed_deployment](docs/sdks/distributeddeployment/README.md)

* [get](docs/sdks/distributeddeployment/README.md#get) - Get summary of Distributed deployment

### [edge_host_files](docs/sdks/edgehostfiles/README.md)

* [get](docs/sdks/edgehostfiles/README.md#get) - Get details about a file on the edge host.

### [edge_listing](docs/sdks/edgelisting/README.md)

* [get](docs/sdks/edgelisting/README.md#get) - Get a directory listing of the given path

### [event_breaker](docs/sdks/eventbreaker/README.md)

* [delete](docs/sdks/eventbreaker/README.md#delete) - Delete Event Breaker Ruleset
* [post](docs/sdks/eventbreaker/README.md#post) - Create Event Breaker Ruleset
* [update](docs/sdks/eventbreaker/README.md#update) - Update Event Breaker Ruleset

### [event_breaker_id](docs/sdks/eventbreakerid/README.md)

* [get](docs/sdks/eventbreakerid/README.md#get) - Get Event Breaker Ruleset by ID

### [event_breaker_on_data](docs/sdks/eventbreakerondata/README.md)

* [post](docs/sdks/eventbreakerondata/README.md#post) - Runs an event breaker rule on the specified data

### [events](docs/sdks/events/README.md)

* [get](docs/sdks/events/README.md#get) - Get events generated by a specified source

### [execute_distributed_upgrade](docs/sdks/executedistributedupgrade/README.md)

* [post](docs/sdks/executedistributedupgrade/README.md#post) - Execute distributed group upgrade

### [executor_id](docs/sdks/executorid/README.md)

* [get](docs/sdks/executorid/README.md#get) - Get Executor by ID

### [executor_object](docs/sdks/executorobject/README.md)

* [get](docs/sdks/executorobject/README.md#get) - Get a list of Executor objects

### [existing_diag_bundles](docs/sdks/existingdiagbundles/README.md)

* [get](docs/sdks/existingdiagbundles/README.md#get) - Get list of existing diag bundles

### [feature](docs/sdks/feature/README.md)

* [get](docs/sdks/feature/README.md#get) - Get feature by Id

### [features](docs/sdks/features/README.md)

* [get](docs/sdks/features/README.md#get) - List all features

### [field_summaries](docs/sdks/fieldsummaries/README.md)

* [get](docs/sdks/fieldsummaries/README.md#get) - List field summaries

### [fleet_mapping](docs/sdks/fleetmapping/README.md)

* [create](docs/sdks/fleetmapping/README.md#create) - Create MappingRuleset

### [fleet_mappings](docs/sdks/fleetmappings/README.md)

* [get](docs/sdks/fleetmappings/README.md#get) - Get a list of MappingRuleset objects

### [fleet_or_worker_group](docs/sdks/fleetorworkergroup/README.md)

* [deploy](docs/sdks/fleetorworkergroup/README.md#deploy) - Deploy commits for a Fleet or Worker Group

### [function_id](docs/sdks/functionid/README.md)

* [get](docs/sdks/functionid/README.md#get) - Get Function by ID

### [git_settings](docs/sdks/gitsettings/README.md)

* [get](docs/sdks/gitsettings/README.md#get) - Get git settings
* [update](docs/sdks/gitsettings/README.md#update) - Update git settings

### [give_cribl_version](docs/sdks/givecriblversion/README.md)

* [post](docs/sdks/givecriblversion/README.md#post) - Upgrade Cribl to a given version

### [global_variable](docs/sdks/globalvariable/README.md)

* [post](docs/sdks/globalvariable/README.md#post) - Create Global Variable

### [global_variable_id](docs/sdks/globalvariableid/README.md)

* [delete](docs/sdks/globalvariableid/README.md#delete) - Delete Global Variable
* [get](docs/sdks/globalvariableid/README.md#get) - Get Global Variable by ID
* [update](docs/sdks/globalvariableid/README.md#update) - Update Global Variable

### [grok_file](docs/sdks/grokfile/README.md)

* [create](docs/sdks/grokfile/README.md#create) - Create GrokFile
* [delete](docs/sdks/grokfile/README.md#delete) - Delete GrokFile
* [get](docs/sdks/grokfile/README.md#get) - Get GrokFile by ID
* [update](docs/sdks/grokfile/README.md#update) - Update GrokFile

### [grok_files](docs/sdks/grokfiles/README.md)

* [get](docs/sdks/grokfiles/README.md#get) - Get a list of GrokFile objects

### [group_bundle](docs/sdks/groupbundle/README.md)

* [get](docs/sdks/groupbundle/README.md#get) - Get effective bundle version for given Group

### [groups](docs/sdks/groups/README.md)

* [get](docs/sdks/groups/README.md#get) - Get a list of ConfigGroup objects

### [health_info](docs/sdks/healthinfo/README.md)

* [get](docs/sdks/healthinfo/README.md#get) - Provides health info for REST server

### [host_metadata_structure](docs/sdks/hostmetadatastructure/README.md)

* [get](docs/sdks/hostmetadatastructure/README.md#get) - Get the host's metadata structure

### [idp_auth](docs/sdks/idpauth/README.md)

* [get](docs/sdks/idpauth/README.md#get) - Get IDP used for an authorization code callback

### [idp_user_auth](docs/sdks/idpuserauth/README.md)

* [logout](docs/sdks/idpuserauth/README.md#logout) - Accepts a logout request from an IDP and logs out the user

### [internal_system_metrics](docs/sdks/internalsystemmetrics/README.md)

* [post](docs/sdks/internalsystemmetrics/README.md#post) - Aggregate raw internal system metrics

### [javascript_expression](docs/sdks/javascriptexpression/README.md)

* [post](docs/sdks/javascriptexpression/README.md#post) - Evaluate JavaScript expression

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

### [job_result](docs/sdks/jobresult/README.md)

* [get](docs/sdks/jobresult/README.md#get) - Get results for a discover job by instance id

### [job_results](docs/sdks/jobresults/README.md)

* [get](docs/sdks/jobresults/README.md#get) - Get results for a discover job by instance id

### [job_status](docs/sdks/jobstatus/README.md)

* [get](docs/sdks/jobstatus/README.md#get) - Get job status

### [kms_config](docs/sdks/kmsconfig/README.md)

* [get](docs/sdks/kmsconfig/README.md#get) - Get Cribl KMS config
* [update](docs/sdks/kmsconfig/README.md#update) - Update Cribl KMS config

### [kms_health](docs/sdks/kmshealth/README.md)

* [get](docs/sdks/kmshealth/README.md#get) - Get Cribl KMS health

### [key_metadata_entities](docs/sdks/keymetadataentities/README.md)

* [get](docs/sdks/keymetadataentities/README.md#get) - Get a list of KeyMetadataEntity objects

### [key_metadata_entity](docs/sdks/keymetadataentity/README.md)

* [create](docs/sdks/keymetadataentity/README.md#create) - Create KeyMetadataEntity
* [delete](docs/sdks/keymetadataentity/README.md#delete) - Delete KeyMetadataEntity
* [get](docs/sdks/keymetadataentity/README.md#get) - Get KeyMetadataEntity by ID
* [update](docs/sdks/keymetadataentity/README.md#update) - Update KeyMetadataEntity

### [latest_pq](docs/sdks/latestpq/README.md)

* [get](docs/sdks/latestpq/README.md#get) - Get status of latest clear PQ job for an output

### [license](docs/sdks/license/README.md)

* [create](docs/sdks/license/README.md#create) - Create License
* [delete](docs/sdks/license/README.md#delete) - Delete License
* [get](docs/sdks/license/README.md#get) - Get License by ID

### [license_usage_metrics](docs/sdks/licenseusagemetrics/README.md)

* [get](docs/sdks/licenseusagemetrics/README.md#get) - Get license usage metrics, aggregated by day, up to last 90 days

### [licenses](docs/sdks/licenses/README.md)

* [get](docs/sdks/licenses/README.md#get) - Get a list of License objects

### [list_auth_group](docs/sdks/listauthgroup/README.md)

* [get](docs/sdks/listauthgroup/README.md#get) - List the external authentication system's groups

### [list_container_detail](docs/sdks/listcontainerdetail/README.md)

* [get](docs/sdks/listcontainerdetail/README.md#get) - Get a detailed list of containers running on the edge host.

### [list_cribl_version](docs/sdks/listcriblversion/README.md)

* [get](docs/sdks/listcriblversion/README.md#get) - Get a list of Cribl versions available for upgrade

### [list_data_sample](docs/sdks/listdatasample/README.md)

* [get](docs/sdks/listdatasample/README.md#get) - Get a list of DataSample objects

### [list_database_connection](docs/sdks/listdatabaseconnection/README.md)

* [get](docs/sdks/listdatabaseconnection/README.md#get) - Get a list of DatabaseConnection objects

### [list_event_breaker](docs/sdks/listeventbreaker/README.md)

* [get](docs/sdks/listeventbreaker/README.md#get) - Get a list of Event Breaker Ruleset objects

### [list_global_variable](docs/sdks/listglobalvariable/README.md)

* [get](docs/sdks/listglobalvariable/README.md#get) - Get a list of Global Variable objects

### [list_parser](docs/sdks/listparser/README.md)

* [get](docs/sdks/listparser/README.md#get) - Get a list of Parser objects

### [list_process_running_detail](docs/sdks/listprocessrunningdetail/README.md)

* [get](docs/sdks/listprocessrunningdetail/README.md#get) - Get a detailed list of processes running on the edge host

### [list_schema](docs/sdks/listschema/README.md)

* [get](docs/sdks/listschema/README.md#get) - Get a list of Schema objects

### [live_data](docs/sdks/livedata/README.md)

* [post](docs/sdks/livedata/README.md#post) - Capture live incoming data

### [log_file_content](docs/sdks/logfilecontent/README.md)

* [get](docs/sdks/logfilecontent/README.md#get) - Get contents of the log file

### [log_file_contents](docs/sdks/logfilecontents/README.md)

* [get](docs/sdks/logfilecontents/README.md#get) - Get contents of the log file

### [log_file_list](docs/sdks/logfilelist/README.md)

* [get](docs/sdks/logfilelist/README.md#get) - list log files

### [log_files](docs/sdks/logfiles/README.md)

* [get](docs/sdks/logfiles/README.md#get) - Get a list of log files

### [log_files_content](docs/sdks/logfilescontent/README.md)

* [get](docs/sdks/logfilescontent/README.md#get) - Get contents of the log file

### [logand_textual](docs/sdks/logandtextual/README.md)

* [get](docs/sdks/logandtextual/README.md#get) - get the log message and textual diff for given commit

### [logger_config](docs/sdks/loggerconfig/README.md)

* [delete](docs/sdks/loggerconfig/README.md#delete) - Delete LoggerConfig
* [get](docs/sdks/loggerconfig/README.md#get) - Get LoggerConfig by ID
* [update](docs/sdks/loggerconfig/README.md#update) - Update LoggerConfig

### [logger_configs](docs/sdks/loggerconfigs/README.md)

* [get](docs/sdks/loggerconfigs/README.md#get) - Get a list of LoggerConfig objects

### [lookup](docs/sdks/lookup/README.md)

* [create](docs/sdks/lookup/README.md#create) - Create LookupFile
* [delete](docs/sdks/lookup/README.md#delete) - Delete LookupFile
* [get](docs/sdks/lookup/README.md#get) - Get LookupFile by ID
* [update](docs/sdks/lookup/README.md#update) - Update LookupFile
* [upload](docs/sdks/lookup/README.md#upload) - Upload LookupFile

### [lookups](docs/sdks/lookups/README.md)

* [get](docs/sdks/lookups/README.md#get) - Get a list of LookupFile objects

### [mapping_ruleset](docs/sdks/mappingruleset/README.md)

* [create](docs/sdks/mappingruleset/README.md#create) - Create MappingRuleset
* [delete](docs/sdks/mappingruleset/README.md#delete) - Delete MappingRuleset
* [get](docs/sdks/mappingruleset/README.md#get) - Get MappingRuleset by ID
* [update](docs/sdks/mappingruleset/README.md#update) - Update MappingRuleset

### [mapping_ruleset_id](docs/sdks/mappingrulesetid/README.md)

* [get](docs/sdks/mappingrulesetid/README.md#get) - Get MappingRuleset by ID

### [mapping_rulesets](docs/sdks/mappingrulesets/README.md)

* [delete](docs/sdks/mappingrulesets/README.md#delete) - Delete MappingRuleset
* [get](docs/sdks/mappingrulesets/README.md#get) - Get a list of MappingRuleset objects
* [update](docs/sdks/mappingrulesets/README.md#update) - Update MappingRuleset

### [master_node_package](docs/sdks/masternodepackage/README.md)

* [post](docs/sdks/masternodepackage/README.md#post) - Upgrade master node with the provided package

### [metrics](docs/sdks/metrics/README.md)

* [post](docs/sdks/metrics/README.md#post) - Enumerate all internal system metrics
* [query](docs/sdks/metrics/README.md#query) - Query raw internal system metrics

### [notification_target](docs/sdks/notificationtarget/README.md)

* [create](docs/sdks/notificationtarget/README.md#create) - Create NotificationTarget
* [delete](docs/sdks/notificationtarget/README.md#delete) - Delete NotificationTarget
* [get](docs/sdks/notificationtarget/README.md#get) - Get NotificationTarget by ID
* [update](docs/sdks/notificationtarget/README.md#update) - Update NotificationTarget

### [notification_targets](docs/sdks/notificationtargets/README.md)

* [get](docs/sdks/notificationtargets/README.md#get) - Get a list of NotificationTarget objects

### [object_function](docs/sdks/objectfunction/README.md)

* [get](docs/sdks/objectfunction/README.md#get) - Get a list of Function objects

### [output_id](docs/sdks/outputid/README.md)

* [delete](docs/sdks/outputid/README.md#delete) - Delete Output
* [get](docs/sdks/outputid/README.md#get) - Get Output by ID
* [update](docs/sdks/outputid/README.md#update) - Update Output

### [output_object](docs/sdks/outputobject/README.md)

* [create](docs/sdks/outputobject/README.md#create) - Create Output

### [output_objects](docs/sdks/outputobjects/README.md)

* [get](docs/sdks/outputobjects/README.md#get) - Get a list of Output objects

### [output_status](docs/sdks/outputstatus/README.md)

* [get](docs/sdks/outputstatus/README.md#get) - Get a list of OutputStatus objects

### [output_status_id](docs/sdks/outputstatusid/README.md)

* [get](docs/sdks/outputstatusid/README.md#get) - Get OutputStatus by ID

### [pack](docs/sdks/pack/README.md)

* [clone](docs/sdks/pack/README.md#clone) - Clone Pack
* [export](docs/sdks/pack/README.md#export) - Export Pack
* [install](docs/sdks/pack/README.md#install) - Install Pack
* [uninstall](docs/sdks/pack/README.md#uninstall) - Uninstall Pack from the system
* [upgrade](docs/sdks/pack/README.md#upgrade) - Upgrade Pack
* [upload](docs/sdks/pack/README.md#upload) - Upload Pack

### [packs](docs/sdks/packs/README.md)

* [get](docs/sdks/packs/README.md#get) - Get info on packs

### [parser_id](docs/sdks/parserid/README.md)

* [delete](docs/sdks/parserid/README.md#delete) - Delete Parser
* [get](docs/sdks/parserid/README.md#get) - Get Parser by ID
* [update](docs/sdks/parserid/README.md#update) - Update Parser

### [parser_object](docs/sdks/parserobject/README.md)

* [post](docs/sdks/parserobject/README.md#post) - Create Parser

### [pipeline_id](docs/sdks/pipelineid/README.md)

* [delete](docs/sdks/pipelineid/README.md#delete) - Delete Pipeline
* [get](docs/sdks/pipelineid/README.md#get) - Get Pipeline by ID
* [update](docs/sdks/pipelineid/README.md#update) - Update Pipeline

### [pipeline_object](docs/sdks/pipelineobject/README.md)

* [get](docs/sdks/pipelineobject/README.md#get) - Get a list of Pipeline objects

### [policy_rule](docs/sdks/policyrule/README.md)

* [create](docs/sdks/policyrule/README.md#create) - Create PolicyRule
* [delete](docs/sdks/policyrule/README.md#delete) - Delete PolicyRule
* [get](docs/sdks/policyrule/README.md#get) - Get PolicyRule by ID
* [update](docs/sdks/policyrule/README.md#update) - Update PolicyRule

### [policy_rules](docs/sdks/policyrules/README.md)

* [get](docs/sdks/policyrules/README.md#get) - Get a list of PolicyRule objects

### [previous_cribl_package](docs/sdks/previouscriblpackage/README.md)

* [get](docs/sdks/previouscriblpackage/README.md#get) - Get the previously downloaded Cribl package

### [process_running_detail](docs/sdks/processrunningdetail/README.md)

* [get](docs/sdks/processrunningdetail/README.md#get) - Get details of a process running on the edge host

### [processes](docs/sdks/processes/README.md)

* [get](docs/sdks/processes/README.md#get) - Get a list of processes under management

### [profiler](docs/sdks/profiler/README.md)

* [create](docs/sdks/profiler/README.md#create) - Create ProfilerItem
* [delete](docs/sdks/profiler/README.md#delete) - Delete ProfilerItem
* [get](docs/sdks/profiler/README.md#get) - Get ProfilerItem by ID
* [update](docs/sdks/profiler/README.md#update) - Update ProfilerItem

### [profilers](docs/sdks/profilers/README.md)

* [get](docs/sdks/profilers/README.md#get) - Get a list of ProfilerItem objects

### [query_snippet](docs/sdks/querysnippet/README.md)

* [apply](docs/sdks/querysnippet/README.md#apply) - Applies a query snippet on a set of input events for preview

### [redirect_info](docs/sdks/redirectinfo/README.md)

* [get](docs/sdks/redirectinfo/README.md#get) - Obtain redirect information

### [redirect_user_auth](docs/sdks/redirectuserauth/README.md)

* [logout](docs/sdks/redirectuserauth/README.md#logout) - Redirect user to IDP with logout request

### [regex_lib_entry](docs/sdks/regexlibentry/README.md)

* [delete](docs/sdks/regexlibentry/README.md#delete) - Delete RegexLibEntry
* [post](docs/sdks/regexlibentry/README.md#post) - Create RegexLibEntry
* [update](docs/sdks/regexlibentry/README.md#update) - Update RegexLibEntry

### [regex_lib_entry_id](docs/sdks/regexlibentryid/README.md)

* [get](docs/sdks/regexlibentryid/README.md#get) - Get RegexLibEntry by ID

### [regex_lib_entry_object](docs/sdks/regexlibentryobject/README.md)

* [get](docs/sdks/regexlibentryobject/README.md#get) - Get a list of RegexLibEntry objects

### [reload_cribl_settings](docs/sdks/reloadcriblsettings/README.md)

* [post](docs/sdks/reloadcriblsettings/README.md#post) - Reload Cribl settings from the filesystem

### [remote_repo](docs/sdks/remoterepo/README.md)

* [sync](docs/sdks/remoterepo/README.md#sync) - syncs with remote repo via POST requests

### [request_auth](docs/sdks/requestauth/README.md)

* [get](docs/sdks/requestauth/README.md#get) - Accepts an authentication request from an IDP and authenticates the user
* [post](docs/sdks/requestauth/README.md#post) - API call that the IDP should use for an authentication request

### [request_user_auth](docs/sdks/requestuserauth/README.md)

* [logout](docs/sdks/requestuserauth/README.md#logout) - API call that the IDP should use for a logout request

### [rest_secret](docs/sdks/restsecret/README.md)

* [create](docs/sdks/restsecret/README.md#create) - Create RestSecret
* [delete](docs/sdks/restsecret/README.md#delete) - Delete RestSecret
* [get](docs/sdks/restsecret/README.md#get) - Get RestSecret by ID
* [update](docs/sdks/restsecret/README.md#update) - Update RestSecret

### [rest_secrets](docs/sdks/restsecrets/README.md)

* [get](docs/sdks/restsecrets/README.md#get) - Get a list of RestSecret objects

### [restart_cribl_settings](docs/sdks/restartcriblsettings/README.md)

* [post](docs/sdks/restartcriblsettings/README.md#post) - Restart Cribl server

### [role](docs/sdks/role/README.md)

* [create](docs/sdks/role/README.md#create) - Create Role
* [delete](docs/sdks/role/README.md#delete) - Delete Role
* [get](docs/sdks/role/README.md#get) - Get Role by ID
* [update](docs/sdks/role/README.md#update) - Update Role

### [roles](docs/sdks/roles/README.md)

* [get](docs/sdks/roles/README.md#get) - Get a list of Role objects

### [route_list_id](docs/sdks/routelistid/README.md)

* [get](docs/sdks/routelistid/README.md#get) - List all routes by id

### [route_lists](docs/sdks/routelists/README.md)

* [get](docs/sdks/routelists/README.md#get) - List all routes

### [route_object](docs/sdks/routeobject/README.md)

* [update](docs/sdks/routeobject/README.md#update) - Add, delete or update the routes with the required content.

### [sample_content](docs/sdks/samplecontent/README.md)

* [get](docs/sdks/samplecontent/README.md#get) - Get sample content by ID

### [sample_events](docs/sdks/sampleevents/README.md)

* [post](docs/sdks/sampleevents/README.md#post) - Sends sample events through a pipeline and returns the results

### [sample_output](docs/sdks/sampleoutput/README.md)

* [post](docs/sdks/sampleoutput/README.md#post) - Send sample data to an output to validate configuration or test connectivity

### [saved_job](docs/sdks/savedjob/README.md)

* [delete](docs/sdks/savedjob/README.md#delete) - Delete SavedJob
* [get](docs/sdks/savedjob/README.md#get) - Get SavedJob by ID
* [update](docs/sdks/savedjob/README.md#update) - Update SavedJob

### [saved_jobs](docs/sdks/savedjobs/README.md)

* [create](docs/sdks/savedjobs/README.md#create) - Create SavedJob
* [get](docs/sdks/savedjobs/README.md#get) - Get a list of SavedJob objects

### [saved_queries](docs/sdks/savedqueries/README.md)

* [create](docs/sdks/savedqueries/README.md#create) - Create SavedQuery
* [delete](docs/sdks/savedqueries/README.md#delete) - Delete SavedQuery
* [get](docs/sdks/savedqueries/README.md#get) - Get a list of SavedQuery objects
* [update](docs/sdks/savedqueries/README.md#update) - Update SavedQuery

### [saved_query](docs/sdks/savedquery/README.md)

* [get](docs/sdks/savedquery/README.md#get) - Get SavedQuery by ID

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

### [schemas](docs/sdks/schemas/README.md)

* [get](docs/sdks/schemas/README.md#get) - Get a list of Schema objects

### [script](docs/sdks/script/README.md)

* [create](docs/sdks/script/README.md#create) - Create Script
* [delete](docs/sdks/script/README.md#delete) - Delete Script
* [get](docs/sdks/script/README.md#get) - Get Script by ID
* [update](docs/sdks/script/README.md#update) - Update Script

### [scripts](docs/sdks/scripts/README.md)

* [get](docs/sdks/scripts/README.md#get) - Get a list of Script objects

### [search](docs/sdks/search/README.md)

* [dispatch_search](docs/sdks/search/README.md#dispatch_search) - Dispatch search *id* to worker nodes filtered by worker node filter using RPC

### [search_doc](docs/sdks/searchdoc/README.md)

* [get](docs/sdks/searchdoc/README.md#get) - Get Search documentation

### [search_job](docs/sdks/searchjob/README.md)

* [create](docs/sdks/searchjob/README.md#create) - Create SearchJob
* [delete](docs/sdks/searchjob/README.md#delete) - Delete SearchJob
* [get](docs/sdks/searchjob/README.md#get) - Get SearchJob by ID
* [update](docs/sdks/searchjob/README.md#update) - Update SearchJob

### [search_job_metrics](docs/sdks/searchjobmetrics/README.md)

* [get](docs/sdks/searchjobmetrics/README.md#get) - Get search job metrics

### [search_jobs](docs/sdks/searchjobs/README.md)

* [get](docs/sdks/searchjobs/README.md#get) - Get a list of SearchJob objects

### [search_limits](docs/sdks/searchlimits/README.md)

* [get](docs/sdks/searchlimits/README.md#get) - Get search limits

### [search_logs](docs/sdks/searchlogs/README.md)

* [get](docs/sdks/searchlogs/README.md#get) - Get search logs

### [search_timeline](docs/sdks/searchtimeline/README.md)

* [get](docs/sdks/searchtimeline/README.md#get) - Get search timeline

### [specified_output](docs/sdks/specifiedoutput/README.md)

* [get](docs/sdks/specifiedoutput/README.md#get) - Get samples data for the specified output. Used to get sample data for the test action.

### [stage_distributed_package](docs/sdks/stagedistributedpackage/README.md)

* [post](docs/sdks/stagedistributedpackage/README.md#post) - Stage distributed group upgrade

### [system_info](docs/sdks/systeminfo/README.md)

* [get](docs/sdks/systeminfo/README.md#get) - Get basic system information

### [task_error](docs/sdks/taskerror/README.md)

* [get](docs/sdks/taskerror/README.md#get) - Get Task errors for a job by id

### [task_errors](docs/sdks/taskerrors/README.md)

* [get](docs/sdks/taskerrors/README.md#get) - Get Task errors for a job by id

### [test_database_connection](docs/sdks/testdatabaseconnection/README.md)

* [post](docs/sdks/testdatabaseconnection/README.md#post) - Test a database connection given a type and connectionString

### [textual_diff](docs/sdks/textualdiff/README.md)

* [get](docs/sdks/textualdiff/README.md#get) - get the textual diff for given commit

### [trust_policies](docs/sdks/trustpolicies/README.md)

* [get](docs/sdks/trustpolicies/README.md#get) - Get a list of TrustPolicy objects

### [ui_state](docs/sdks/uistate/README.md)

* [get](docs/sdks/uistate/README.md#get) - Get UI state by key
* [update](docs/sdks/uistate/README.md#update) - Update UI state by key

### [user](docs/sdks/user/README.md)

* [create_user](docs/sdks/user/README.md#create_user) - Create User

### [user_auth](docs/sdks/userauth/README.md)

* [logout](docs/sdks/userauth/README.md#logout) - Log current user out

### [user_id](docs/sdks/userid/README.md)

* [delete](docs/sdks/userid/README.md#delete) - Delete User
* [get](docs/sdks/userid/README.md#get) - Get User by ID

### [user_object](docs/sdks/userobject/README.md)

* [get](docs/sdks/userobject/README.md#get) - Get a list of User objects
* [update](docs/sdks/userobject/README.md#update) - Update User except for their roles

### [user_properties](docs/sdks/userproperties/README.md)

* [update](docs/sdks/userproperties/README.md#update) - Update User properties – admin use only

### [versioning](docs/sdks/versioning/README.md)

* [get](docs/sdks/versioning/README.md#get) - Get info about versioning availability

### [worker_edge_nodes](docs/sdks/workeredgenodes/README.md)

* [get](docs/sdks/workeredgenodes/README.md#get) - get worker and edge nodes
* [restarts](docs/sdks/workeredgenodes/README.md#restarts) - restarts worker nodes

### [worker_edge_nodes_count](docs/sdks/workeredgenodescount/README.md)

* [get](docs/sdks/workeredgenodescount/README.md#get) - get worker and edge nodes count

### [working_tree](docs/sdks/workingtree/README.md)

* [get](docs/sdks/workingtree/README.md#get) - get the the working tree status
<!-- End SDK Available Operations -->

### Maturity

This SDK is in beta, and there may be breaking changes between versions without a major version update. Therefore, we recommend pinning usage
to a specific package version. This way, you can install the same version each time without breaking changes unless you are intentionally
looking for the latest version.

### Contributions

While we value open-source contributions to this SDK, this library is generated programmatically.
Feel free to open a PR or a Github issue as a proof of concept and we'll do our best to include it in a future release!

### SDK Created by [Speakeasy](https://docs.speakeasyapi.dev/docs/using-speakeasy/client-sdks)
