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

```bash
pip install cribl
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


### [AppscopeLibEntries](docs/sdks/appscopelibentries/README.md)

* [get](docs/sdks/appscopelibentries/README.md#get) - Get a list of AppscopeLibEntry objects

### [AppscopeLibEntry](docs/sdks/appscopelibentry/README.md)

* [create](docs/sdks/appscopelibentry/README.md#create) - Create AppscopeLibEntry
* [delete](docs/sdks/appscopelibentry/README.md#delete) - Delete AppscopeLibEntry
* [get](docs/sdks/appscopelibentry/README.md#get) - Get AppscopeLibEntry by ID
* [update](docs/sdks/appscopelibentry/README.md#update) - Update AppscopeLibEntry

### [AuthToken](docs/sdks/authtoken/README.md)

* [login](docs/sdks/authtoken/README.md#login) - Log in and obtain Auth token

### [AuthenticationSettings](docs/sdks/authenticationsettings/README.md)

* [get](docs/sdks/authenticationsettings/README.md#get) - Get authentication settings
* [update](docs/sdks/authenticationsettings/README.md#update) - Update authentication settings

### [Authorizations](docs/sdks/authorizations/README.md)

* [get](docs/sdks/authorizations/README.md#get) - get the client's authorization policy

### [Branches](docs/sdks/branches/README.md)

* [get](docs/sdks/branches/README.md#get) - get the list of branches

### [BulletinMessage](docs/sdks/bulletinmessage/README.md)

* [create](docs/sdks/bulletinmessage/README.md#create) - Create BulletinMessage
* [delete](docs/sdks/bulletinmessage/README.md#delete) - Delete BulletinMessage
* [get](docs/sdks/bulletinmessage/README.md#get) - Get BulletinMessage by ID

### [BulletinMessages](docs/sdks/bulletinmessages/README.md)

* [get](docs/sdks/bulletinmessages/README.md#get) - Get a list of BulletinMessage objects

### [Bytes](docs/sdks/bytes/README.md)

* [get](docs/sdks/bytes/README.md#get) - Get some number of bytes from the file at the given path

### [CancelRunningGroup](docs/sdks/cancelrunninggroup/README.md)

* [post](docs/sdks/cancelrunninggroup/README.md#post) - Cancel a running group upgrade

### [Certificate](docs/sdks/certificate/README.md)

* [create](docs/sdks/certificate/README.md#create) - Create Certificate
* [delete](docs/sdks/certificate/README.md#delete) - Delete Certificate
* [get](docs/sdks/certificate/README.md#get) - Get Certificate by ID
* [update](docs/sdks/certificate/README.md#update) - Update Certificate

### [Certificates](docs/sdks/certificates/README.md)

* [get](docs/sdks/certificates/README.md#get) - Get a list of Certificate objects

### [ChangedFiles](docs/sdks/changedfiles/README.md)

* [get](docs/sdks/changedfiles/README.md#get) - get the files changed

### [ChangelogViewState](docs/sdks/changelogviewstate/README.md)

* [update](docs/sdks/changelogviewstate/README.md#update) - Update changelog viewed state

### [Changelogs](docs/sdks/changelogs/README.md)

* [get](docs/sdks/changelogs/README.md#get) - Get changelog viewed state

### [ClientRoles](docs/sdks/clientroles/README.md)

* [get](docs/sdks/clientroles/README.md#get) - get the client's roles

### [Cluis](docs/sdks/cluis/README.md)

* [get](docs/sdks/cluis/README.md#get) - Get CLUI search results

### [Collector](docs/sdks/collector/README.md)

* [get](docs/sdks/collector/README.md#get) - Get Collector by ID

### [CollectorObject](docs/sdks/collectorobject/README.md)

* [get](docs/sdks/collectorobject/README.md#get) - Get a list of Collector objects

### [Commit](docs/sdks/commit/README.md)

* [create](docs/sdks/commit/README.md#create) - create a new commit containing the current configs the given log message describing the changes.

### [Condition](docs/sdks/condition/README.md)

* [get](docs/sdks/condition/README.md#get) - Get Condition by ID

### [Conditions](docs/sdks/conditions/README.md)

* [get](docs/sdks/conditions/README.md#get) - Get a list of Condition objects

### [ConfigGroup](docs/sdks/configgroup/README.md)

* [create](docs/sdks/configgroup/README.md#create) - Create ConfigGroup
* [delete](docs/sdks/configgroup/README.md#delete) - Delete ConfigGroup
* [get](docs/sdks/configgroup/README.md#get) - Get a specific ConfigGroup object
* [update](docs/sdks/configgroup/README.md#update) - Update ConfigGroup

### [ConfiguredCollectors](docs/sdks/configuredcollectors/README.md)

* [get](docs/sdks/configuredcollectors/README.md#get) - Get list of configured collectors

### [Container](docs/sdks/container/README.md)

* [get](docs/sdks/container/README.md#get) - Get details for a single container on the edge host. Add stream=true to get a stream instead.

### [CountFile](docs/sdks/countfile/README.md)

* [get](docs/sdks/countfile/README.md#get) - get the count of files of changed

### [CreatePipeline](docs/sdks/createpipeline/README.md)

* [post](docs/sdks/createpipeline/README.md#post) - Create Pipeline

### [CriblMetadata](docs/sdks/criblmetadata/README.md)

* [get](docs/sdks/criblmetadata/README.md#get) - Obtain metadata which Cribl Stream/Edge uses when acting as a Service Provider

### [CriblSystemSettings](docs/sdks/criblsystemsettings/README.md)

* [get](docs/sdks/criblsystemsettings/README.md#get) - Get Cribl system settings
* [update](docs/sdks/criblsystemsettings/README.md#update) - Update Cribl system settings

### [CriblsSettings](docs/sdks/criblssettings/README.md)

* [~~get~~](docs/sdks/criblssettings/README.md#get) - Get Cribl system settings. Deprecated: use specific endpoints /system/limits, /system/job-limits, /system/redis-cache-limits, /system/services-limits, /system/settings/git-settings, and /system/settings/conf respectively :warning: **Deprecated**
* [~~update~~](docs/sdks/criblssettings/README.md#update) - Update Cribl system settings. Deprecated: use specific endpoints /system/limits, /system/job-limits, /system/settings/git-settings, /system/settings/auth and /system/settings/conf respectively :warning: **Deprecated**

### [CurrentConfig](docs/sdks/currentconfig/README.md)

* [push](docs/sdks/currentconfig/README.md#push) - push the current configs to the remote repository.

### [DataSample](docs/sdks/datasample/README.md)

* [post](docs/sdks/datasample/README.md#post) - Create DataSample

### [DataSampleID](docs/sdks/datasampleid/README.md)

* [delete](docs/sdks/datasampleid/README.md#delete) - Delete DataSample
* [get](docs/sdks/datasampleid/README.md#get) - Get DataSample by ID
* [update](docs/sdks/datasampleid/README.md#update) - Update DataSample

### [DatabaseConnection](docs/sdks/databaseconnection/README.md)

* [post](docs/sdks/databaseconnection/README.md#post) - Create DatabaseConnectionConfig

### [DatabaseConnectionConfigID](docs/sdks/databaseconnectionconfigid/README.md)

* [delete](docs/sdks/databaseconnectionconfigid/README.md#delete) - Delete DatabaseConnectionConfig
* [get](docs/sdks/databaseconnectionconfigid/README.md#get) - Get DatabaseConnectionConfig by ID
* [update](docs/sdks/databaseconnectionconfigid/README.md#update) - Update DatabaseConnectionConfig

### [Dataset](docs/sdks/dataset/README.md)

* [create](docs/sdks/dataset/README.md#create) - Create DatasetProviderType
* [delete](docs/sdks/dataset/README.md#delete) - Delete DatasetProviderType
* [get](docs/sdks/dataset/README.md#get) - Get DatasetProviderType by ID
* [update](docs/sdks/dataset/README.md#update) - Update DatasetProviderType

### [DatasetObject](docs/sdks/datasetobject/README.md)

* [create](docs/sdks/datasetobject/README.md#create) - Create Dataset
* [delete](docs/sdks/datasetobject/README.md#delete) - Delete Dataset
* [get](docs/sdks/datasetobject/README.md#get) - Get Dataset by ID
* [update](docs/sdks/datasetobject/README.md#update) - Update Dataset

### [DatasetObjects](docs/sdks/datasetobjects/README.md)

* [get](docs/sdks/datasetobjects/README.md#get) - Get a list of Dataset objects

### [Datasets](docs/sdks/datasets/README.md)

* [get](docs/sdks/datasets/README.md#get) - Get a list of DatasetProviderType objects

### [DestinationQueue](docs/sdks/destinationqueue/README.md)

* [delete](docs/sdks/destinationqueue/README.md#delete) - Delete destination persistent queue

### [DiagBundle](docs/sdks/diagbundle/README.md)

* [delete](docs/sdks/diagbundle/README.md#delete) - Remove diag bundle
* [get](docs/sdks/diagbundle/README.md#get) - Returns a diag bundle as a tar.gz archive
* [send](docs/sdks/diagbundle/README.md#send) - Send a diag bundle (tar.gz archive) to Cribl

### [DiagBundles](docs/sdks/diagbundles/README.md)

* [get](docs/sdks/diagbundles/README.md#get) - Get list of existing diag bundles

### [DistributedDeployment](docs/sdks/distributeddeployment/README.md)

* [get](docs/sdks/distributeddeployment/README.md#get) - Get summary of Distributed deployment

### [EdgeHostFiles](docs/sdks/edgehostfiles/README.md)

* [get](docs/sdks/edgehostfiles/README.md#get) - Get details about a file on the edge host.

### [EdgeListing](docs/sdks/edgelisting/README.md)

* [get](docs/sdks/edgelisting/README.md#get) - Get a directory listing of the given path

### [EventBreaker](docs/sdks/eventbreaker/README.md)

* [delete](docs/sdks/eventbreaker/README.md#delete) - Delete Event Breaker Ruleset
* [post](docs/sdks/eventbreaker/README.md#post) - Create Event Breaker Ruleset
* [update](docs/sdks/eventbreaker/README.md#update) - Update Event Breaker Ruleset

### [EventBreakerID](docs/sdks/eventbreakerid/README.md)

* [get](docs/sdks/eventbreakerid/README.md#get) - Get Event Breaker Ruleset by ID

### [EventBreakerOnData](docs/sdks/eventbreakerondata/README.md)

* [post](docs/sdks/eventbreakerondata/README.md#post) - Runs an event breaker rule on the specified data

### [Events](docs/sdks/events/README.md)

* [get](docs/sdks/events/README.md#get) - Get events generated by a specified source

### [ExecuteDistributedUpgrade](docs/sdks/executedistributedupgrade/README.md)

* [post](docs/sdks/executedistributedupgrade/README.md#post) - Execute distributed group upgrade

### [ExecutorID](docs/sdks/executorid/README.md)

* [get](docs/sdks/executorid/README.md#get) - Get Executor by ID

### [ExecutorObject](docs/sdks/executorobject/README.md)

* [get](docs/sdks/executorobject/README.md#get) - Get a list of Executor objects

### [ExistingDiagBundles](docs/sdks/existingdiagbundles/README.md)

* [get](docs/sdks/existingdiagbundles/README.md#get) - Get list of existing diag bundles

### [Feature](docs/sdks/feature/README.md)

* [get](docs/sdks/feature/README.md#get) - Get feature by Id

### [Features](docs/sdks/features/README.md)

* [get](docs/sdks/features/README.md#get) - List all features

### [FieldSummaries](docs/sdks/fieldsummaries/README.md)

* [get](docs/sdks/fieldsummaries/README.md#get) - List field summaries

### [FleetMapping](docs/sdks/fleetmapping/README.md)

* [create](docs/sdks/fleetmapping/README.md#create) - Create MappingRuleset

### [FleetMappings](docs/sdks/fleetmappings/README.md)

* [get](docs/sdks/fleetmappings/README.md#get) - Get a list of MappingRuleset objects

### [FleetOrWorkerGroup](docs/sdks/fleetorworkergroup/README.md)

* [deploy](docs/sdks/fleetorworkergroup/README.md#deploy) - Deploy commits for a Fleet or Worker Group

### [FunctionID](docs/sdks/functionid/README.md)

* [get](docs/sdks/functionid/README.md#get) - Get Function by ID

### [GitSettings](docs/sdks/gitsettings/README.md)

* [get](docs/sdks/gitsettings/README.md#get) - Get git settings
* [update](docs/sdks/gitsettings/README.md#update) - Update git settings

### [GiveCriblVersion](docs/sdks/givecriblversion/README.md)

* [post](docs/sdks/givecriblversion/README.md#post) - Upgrade Cribl to a given version

### [GlobalVariable](docs/sdks/globalvariable/README.md)

* [post](docs/sdks/globalvariable/README.md#post) - Create Global Variable

### [GlobalVariableID](docs/sdks/globalvariableid/README.md)

* [delete](docs/sdks/globalvariableid/README.md#delete) - Delete Global Variable
* [get](docs/sdks/globalvariableid/README.md#get) - Get Global Variable by ID
* [update](docs/sdks/globalvariableid/README.md#update) - Update Global Variable

### [GrokFile](docs/sdks/grokfile/README.md)

* [create](docs/sdks/grokfile/README.md#create) - Create GrokFile
* [delete](docs/sdks/grokfile/README.md#delete) - Delete GrokFile
* [get](docs/sdks/grokfile/README.md#get) - Get GrokFile by ID
* [update](docs/sdks/grokfile/README.md#update) - Update GrokFile

### [GrokFiles](docs/sdks/grokfiles/README.md)

* [get](docs/sdks/grokfiles/README.md#get) - Get a list of GrokFile objects

### [GroupBundle](docs/sdks/groupbundle/README.md)

* [get](docs/sdks/groupbundle/README.md#get) - Get effective bundle version for given Group

### [Groups](docs/sdks/groups/README.md)

* [get](docs/sdks/groups/README.md#get) - Get a list of ConfigGroup objects

### [HealthInfo](docs/sdks/healthinfo/README.md)

* [get](docs/sdks/healthinfo/README.md#get) - Provides health info for REST server

### [HostMetadataStructure](docs/sdks/hostmetadatastructure/README.md)

* [get](docs/sdks/hostmetadatastructure/README.md#get) - Get the host's metadata structure

### [IDPAuth](docs/sdks/idpauth/README.md)

* [get](docs/sdks/idpauth/README.md#get) - Get IDP used for an authorization code callback

### [IDPUserAuth](docs/sdks/idpuserauth/README.md)

* [logout](docs/sdks/idpuserauth/README.md#logout) - Accepts a logout request from an IDP and logs out the user

### [InternalSystemMetrics](docs/sdks/internalsystemmetrics/README.md)

* [post](docs/sdks/internalsystemmetrics/README.md#post) - Aggregate raw internal system metrics

### [JavascriptExpression](docs/sdks/javascriptexpression/README.md)

* [post](docs/sdks/javascriptexpression/README.md#post) - Evaluate JavaScript expression

### [Job](docs/sdks/job/README.md)

* [cancel](docs/sdks/job/README.md#cancel) - Cancel a job by instance id
* [delete](docs/sdks/job/README.md#delete) - Remove job from job inspector by instance id
* [get](docs/sdks/job/README.md#get) - Get job info by instance id
* [pause_job](docs/sdks/job/README.md#pause_job) - Pause a job by instance id
* [prevent](docs/sdks/job/README.md#prevent) - prevent job from being deleted automatically
* [resume](docs/sdks/job/README.md#resume) - Resume a job by instance id
* [run_job](docs/sdks/job/README.md#run_job) - Run or schedule a job

### [JobInfos](docs/sdks/jobinfos/README.md)

* [get](docs/sdks/jobinfos/README.md#get) - Get info on jobs

### [JobResult](docs/sdks/jobresult/README.md)

* [get](docs/sdks/jobresult/README.md#get) - Get results for a discover job by instance id

### [JobResults](docs/sdks/jobresults/README.md)

* [get](docs/sdks/jobresults/README.md#get) - Get results for a discover job by instance id

### [JobStatus](docs/sdks/jobstatus/README.md)

* [get](docs/sdks/jobstatus/README.md#get) - Get job status

### [KMSConfig](docs/sdks/kmsconfig/README.md)

* [get](docs/sdks/kmsconfig/README.md#get) - Get Cribl KMS config
* [update](docs/sdks/kmsconfig/README.md#update) - Update Cribl KMS config

### [KMSHealth](docs/sdks/kmshealth/README.md)

* [get](docs/sdks/kmshealth/README.md#get) - Get Cribl KMS health

### [KeyMetadataEntities](docs/sdks/keymetadataentities/README.md)

* [get](docs/sdks/keymetadataentities/README.md#get) - Get a list of KeyMetadataEntity objects

### [KeyMetadataEntity](docs/sdks/keymetadataentity/README.md)

* [create](docs/sdks/keymetadataentity/README.md#create) - Create KeyMetadataEntity
* [delete](docs/sdks/keymetadataentity/README.md#delete) - Delete KeyMetadataEntity
* [get](docs/sdks/keymetadataentity/README.md#get) - Get KeyMetadataEntity by ID
* [update](docs/sdks/keymetadataentity/README.md#update) - Update KeyMetadataEntity

### [LatestPQ](docs/sdks/latestpq/README.md)

* [get](docs/sdks/latestpq/README.md#get) - Get status of latest clear PQ job for an output

### [License](docs/sdks/license/README.md)

* [create](docs/sdks/license/README.md#create) - Create License
* [delete](docs/sdks/license/README.md#delete) - Delete License
* [get](docs/sdks/license/README.md#get) - Get License by ID

### [LicenseUsageMetrics](docs/sdks/licenseusagemetrics/README.md)

* [get](docs/sdks/licenseusagemetrics/README.md#get) - Get license usage metrics, aggregated by day, up to last 90 days

### [Licenses](docs/sdks/licenses/README.md)

* [get](docs/sdks/licenses/README.md#get) - Get a list of License objects

### [ListAuthGroup](docs/sdks/listauthgroup/README.md)

* [get](docs/sdks/listauthgroup/README.md#get) - List the external authentication system's groups

### [ListContainerDetail](docs/sdks/listcontainerdetail/README.md)

* [get](docs/sdks/listcontainerdetail/README.md#get) - Get a detailed list of containers running on the edge host.

### [ListCriblVersion](docs/sdks/listcriblversion/README.md)

* [get](docs/sdks/listcriblversion/README.md#get) - Get a list of Cribl versions available for upgrade

### [ListDataSample](docs/sdks/listdatasample/README.md)

* [get](docs/sdks/listdatasample/README.md#get) - Get a list of DataSample objects

### [ListDatabaseConnection](docs/sdks/listdatabaseconnection/README.md)

* [get](docs/sdks/listdatabaseconnection/README.md#get) - Get a list of DatabaseConnection objects

### [ListEventBreaker](docs/sdks/listeventbreaker/README.md)

* [get](docs/sdks/listeventbreaker/README.md#get) - Get a list of Event Breaker Ruleset objects

### [ListGlobalVariable](docs/sdks/listglobalvariable/README.md)

* [get](docs/sdks/listglobalvariable/README.md#get) - Get a list of Global Variable objects

### [ListParser](docs/sdks/listparser/README.md)

* [get](docs/sdks/listparser/README.md#get) - Get a list of Parser objects

### [ListProcessRunningDetail](docs/sdks/listprocessrunningdetail/README.md)

* [get](docs/sdks/listprocessrunningdetail/README.md#get) - Get a detailed list of processes running on the edge host

### [ListSchema](docs/sdks/listschema/README.md)

* [get](docs/sdks/listschema/README.md#get) - Get a list of Schema objects

### [LiveData](docs/sdks/livedata/README.md)

* [post](docs/sdks/livedata/README.md#post) - Capture live incoming data

### [LogFileContent](docs/sdks/logfilecontent/README.md)

* [get](docs/sdks/logfilecontent/README.md#get) - Get contents of the log file

### [LogFileContents](docs/sdks/logfilecontents/README.md)

* [get](docs/sdks/logfilecontents/README.md#get) - Get contents of the log file

### [LogFileList](docs/sdks/logfilelist/README.md)

* [get](docs/sdks/logfilelist/README.md#get) - list log files

### [LogFiles](docs/sdks/logfiles/README.md)

* [get](docs/sdks/logfiles/README.md#get) - Get a list of log files

### [LogFilesContent](docs/sdks/logfilescontent/README.md)

* [get](docs/sdks/logfilescontent/README.md#get) - Get contents of the log file

### [LogandTextual](docs/sdks/logandtextual/README.md)

* [get](docs/sdks/logandtextual/README.md#get) - get the log message and textual diff for given commit

### [LoggerConfig](docs/sdks/loggerconfig/README.md)

* [delete](docs/sdks/loggerconfig/README.md#delete) - Delete LoggerConfig
* [get](docs/sdks/loggerconfig/README.md#get) - Get LoggerConfig by ID
* [update](docs/sdks/loggerconfig/README.md#update) - Update LoggerConfig

### [LoggerConfigs](docs/sdks/loggerconfigs/README.md)

* [get](docs/sdks/loggerconfigs/README.md#get) - Get a list of LoggerConfig objects

### [Lookup](docs/sdks/lookup/README.md)

* [create](docs/sdks/lookup/README.md#create) - Create LookupFile
* [delete](docs/sdks/lookup/README.md#delete) - Delete LookupFile
* [get](docs/sdks/lookup/README.md#get) - Get LookupFile by ID
* [update](docs/sdks/lookup/README.md#update) - Update LookupFile
* [upload](docs/sdks/lookup/README.md#upload) - Upload LookupFile

### [Lookups](docs/sdks/lookups/README.md)

* [get](docs/sdks/lookups/README.md#get) - Get a list of LookupFile objects

### [MappingRuleset](docs/sdks/mappingruleset/README.md)

* [create](docs/sdks/mappingruleset/README.md#create) - Create MappingRuleset
* [delete](docs/sdks/mappingruleset/README.md#delete) - Delete MappingRuleset
* [get](docs/sdks/mappingruleset/README.md#get) - Get MappingRuleset by ID
* [update](docs/sdks/mappingruleset/README.md#update) - Update MappingRuleset

### [MappingRulesetID](docs/sdks/mappingrulesetid/README.md)

* [get](docs/sdks/mappingrulesetid/README.md#get) - Get MappingRuleset by ID

### [MappingRulesets](docs/sdks/mappingrulesets/README.md)

* [delete](docs/sdks/mappingrulesets/README.md#delete) - Delete MappingRuleset
* [get](docs/sdks/mappingrulesets/README.md#get) - Get a list of MappingRuleset objects
* [update](docs/sdks/mappingrulesets/README.md#update) - Update MappingRuleset

### [MasterNodePackage](docs/sdks/masternodepackage/README.md)

* [post](docs/sdks/masternodepackage/README.md#post) - Upgrade master node with the provided package

### [Metrics](docs/sdks/metrics/README.md)

* [post](docs/sdks/metrics/README.md#post) - Enumerate all internal system metrics
* [query](docs/sdks/metrics/README.md#query) - Query raw internal system metrics

### [NotificationTarget](docs/sdks/notificationtarget/README.md)

* [create](docs/sdks/notificationtarget/README.md#create) - Create NotificationTarget
* [delete](docs/sdks/notificationtarget/README.md#delete) - Delete NotificationTarget
* [get](docs/sdks/notificationtarget/README.md#get) - Get NotificationTarget by ID
* [update](docs/sdks/notificationtarget/README.md#update) - Update NotificationTarget

### [NotificationTargets](docs/sdks/notificationtargets/README.md)

* [get](docs/sdks/notificationtargets/README.md#get) - Get a list of NotificationTarget objects

### [ObjectFunction](docs/sdks/objectfunction/README.md)

* [get](docs/sdks/objectfunction/README.md#get) - Get a list of Function objects

### [OutputID](docs/sdks/outputid/README.md)

* [delete](docs/sdks/outputid/README.md#delete) - Delete Output
* [get](docs/sdks/outputid/README.md#get) - Get Output by ID
* [update](docs/sdks/outputid/README.md#update) - Update Output

### [OutputObject](docs/sdks/outputobject/README.md)

* [create](docs/sdks/outputobject/README.md#create) - Create Output

### [OutputObjects](docs/sdks/outputobjects/README.md)

* [get](docs/sdks/outputobjects/README.md#get) - Get a list of Output objects

### [OutputStatus](docs/sdks/outputstatus/README.md)

* [get](docs/sdks/outputstatus/README.md#get) - Get a list of OutputStatus objects

### [OutputStatusID](docs/sdks/outputstatusid/README.md)

* [get](docs/sdks/outputstatusid/README.md#get) - Get OutputStatus by ID

### [Pack](docs/sdks/pack/README.md)

* [clone](docs/sdks/pack/README.md#clone) - Clone Pack
* [export](docs/sdks/pack/README.md#export) - Export Pack
* [install](docs/sdks/pack/README.md#install) - Install Pack
* [uninstall](docs/sdks/pack/README.md#uninstall) - Uninstall Pack from the system
* [upgrade](docs/sdks/pack/README.md#upgrade) - Upgrade Pack
* [upload](docs/sdks/pack/README.md#upload) - Upload Pack

### [Packs](docs/sdks/packs/README.md)

* [get](docs/sdks/packs/README.md#get) - Get info on packs

### [ParserID](docs/sdks/parserid/README.md)

* [delete](docs/sdks/parserid/README.md#delete) - Delete Parser
* [get](docs/sdks/parserid/README.md#get) - Get Parser by ID
* [update](docs/sdks/parserid/README.md#update) - Update Parser

### [ParserObject](docs/sdks/parserobject/README.md)

* [post](docs/sdks/parserobject/README.md#post) - Create Parser

### [PipelineID](docs/sdks/pipelineid/README.md)

* [delete](docs/sdks/pipelineid/README.md#delete) - Delete Pipeline
* [get](docs/sdks/pipelineid/README.md#get) - Get Pipeline by ID
* [update](docs/sdks/pipelineid/README.md#update) - Update Pipeline

### [PipelineObject](docs/sdks/pipelineobject/README.md)

* [get](docs/sdks/pipelineobject/README.md#get) - Get a list of Pipeline objects

### [PolicyRule](docs/sdks/policyrule/README.md)

* [create](docs/sdks/policyrule/README.md#create) - Create PolicyRule
* [delete](docs/sdks/policyrule/README.md#delete) - Delete PolicyRule
* [get](docs/sdks/policyrule/README.md#get) - Get PolicyRule by ID
* [update](docs/sdks/policyrule/README.md#update) - Update PolicyRule

### [PolicyRules](docs/sdks/policyrules/README.md)

* [get](docs/sdks/policyrules/README.md#get) - Get a list of PolicyRule objects

### [PreviousCriblPackage](docs/sdks/previouscriblpackage/README.md)

* [get](docs/sdks/previouscriblpackage/README.md#get) - Get the previously downloaded Cribl package

### [ProcessRunningDetail](docs/sdks/processrunningdetail/README.md)

* [get](docs/sdks/processrunningdetail/README.md#get) - Get details of a process running on the edge host

### [Processes](docs/sdks/processes/README.md)

* [get](docs/sdks/processes/README.md#get) - Get a list of processes under management

### [Profiler](docs/sdks/profiler/README.md)

* [create](docs/sdks/profiler/README.md#create) - Create ProfilerItem
* [delete](docs/sdks/profiler/README.md#delete) - Delete ProfilerItem
* [get](docs/sdks/profiler/README.md#get) - Get ProfilerItem by ID
* [update](docs/sdks/profiler/README.md#update) - Update ProfilerItem

### [Profilers](docs/sdks/profilers/README.md)

* [get](docs/sdks/profilers/README.md#get) - Get a list of ProfilerItem objects

### [QuerySnippet](docs/sdks/querysnippet/README.md)

* [apply](docs/sdks/querysnippet/README.md#apply) - Applies a query snippet on a set of input events for preview

### [RedirectInfo](docs/sdks/redirectinfo/README.md)

* [get](docs/sdks/redirectinfo/README.md#get) - Obtain redirect information

### [RedirectUserAuth](docs/sdks/redirectuserauth/README.md)

* [logout](docs/sdks/redirectuserauth/README.md#logout) - Redirect user to IDP with logout request

### [RegexLibEntry](docs/sdks/regexlibentry/README.md)

* [delete](docs/sdks/regexlibentry/README.md#delete) - Delete RegexLibEntry
* [post](docs/sdks/regexlibentry/README.md#post) - Create RegexLibEntry
* [update](docs/sdks/regexlibentry/README.md#update) - Update RegexLibEntry

### [RegexLibEntryID](docs/sdks/regexlibentryid/README.md)

* [get](docs/sdks/regexlibentryid/README.md#get) - Get RegexLibEntry by ID

### [RegexLibEntryObject](docs/sdks/regexlibentryobject/README.md)

* [get](docs/sdks/regexlibentryobject/README.md#get) - Get a list of RegexLibEntry objects

### [ReloadCriblSettings](docs/sdks/reloadcriblsettings/README.md)

* [post](docs/sdks/reloadcriblsettings/README.md#post) - Reload Cribl settings from the filesystem

### [RemoteRepo](docs/sdks/remoterepo/README.md)

* [sync](docs/sdks/remoterepo/README.md#sync) - syncs with remote repo via POST requests

### [RequestAuth](docs/sdks/requestauth/README.md)

* [get](docs/sdks/requestauth/README.md#get) - Accepts an authentication request from an IDP and authenticates the user
* [post](docs/sdks/requestauth/README.md#post) - API call that the IDP should use for an authentication request

### [RequestUserAuth](docs/sdks/requestuserauth/README.md)

* [logout](docs/sdks/requestuserauth/README.md#logout) - API call that the IDP should use for a logout request

### [RestSecret](docs/sdks/restsecret/README.md)

* [create](docs/sdks/restsecret/README.md#create) - Create RestSecret
* [delete](docs/sdks/restsecret/README.md#delete) - Delete RestSecret
* [get](docs/sdks/restsecret/README.md#get) - Get RestSecret by ID
* [update](docs/sdks/restsecret/README.md#update) - Update RestSecret

### [RestSecrets](docs/sdks/restsecrets/README.md)

* [get](docs/sdks/restsecrets/README.md#get) - Get a list of RestSecret objects

### [RestartCriblSettings](docs/sdks/restartcriblsettings/README.md)

* [post](docs/sdks/restartcriblsettings/README.md#post) - Restart Cribl server

### [Role](docs/sdks/role/README.md)

* [create](docs/sdks/role/README.md#create) - Create Role
* [delete](docs/sdks/role/README.md#delete) - Delete Role
* [get](docs/sdks/role/README.md#get) - Get Role by ID
* [update](docs/sdks/role/README.md#update) - Update Role

### [Roles](docs/sdks/roles/README.md)

* [get](docs/sdks/roles/README.md#get) - Get a list of Role objects

### [RouteListID](docs/sdks/routelistid/README.md)

* [get](docs/sdks/routelistid/README.md#get) - List all routes by id

### [RouteLists](docs/sdks/routelists/README.md)

* [get](docs/sdks/routelists/README.md#get) - List all routes

### [RouteObject](docs/sdks/routeobject/README.md)

* [update](docs/sdks/routeobject/README.md#update) - Add, delete or update the routes with the required content.

### [SampleContent](docs/sdks/samplecontent/README.md)

* [get](docs/sdks/samplecontent/README.md#get) - Get sample content by ID

### [SampleEvents](docs/sdks/sampleevents/README.md)

* [post](docs/sdks/sampleevents/README.md#post) - Sends sample events through a pipeline and returns the results

### [SampleOutput](docs/sdks/sampleoutput/README.md)

* [post](docs/sdks/sampleoutput/README.md#post) - Send sample data to an output to validate configuration or test connectivity

### [SavedJob](docs/sdks/savedjob/README.md)

* [delete](docs/sdks/savedjob/README.md#delete) - Delete SavedJob
* [get](docs/sdks/savedjob/README.md#get) - Get SavedJob by ID
* [update](docs/sdks/savedjob/README.md#update) - Update SavedJob

### [SavedJobs](docs/sdks/savedjobs/README.md)

* [create](docs/sdks/savedjobs/README.md#create) - Create SavedJob
* [get](docs/sdks/savedjobs/README.md#get) - Get a list of SavedJob objects

### [SavedQueries](docs/sdks/savedqueries/README.md)

* [create](docs/sdks/savedqueries/README.md#create) - Create SavedQuery
* [delete](docs/sdks/savedqueries/README.md#delete) - Delete SavedQuery
* [get](docs/sdks/savedqueries/README.md#get) - Get a list of SavedQuery objects
* [update](docs/sdks/savedqueries/README.md#update) - Update SavedQuery

### [SavedQuery](docs/sdks/savedquery/README.md)

* [get](docs/sdks/savedquery/README.md#get) - Get SavedQuery by ID

### [Schema](docs/sdks/schema/README.md)

* [create](docs/sdks/schema/README.md#create) - Create Schema
* [delete](docs/sdks/schema/README.md#delete) - Delete Schema
* [get](docs/sdks/schema/README.md#get) - Get Schema by ID
* [post](docs/sdks/schema/README.md#post) - Create Schema
* [update](docs/sdks/schema/README.md#update) - Update Schema

### [SchemaID](docs/sdks/schemaid/README.md)

* [delete](docs/sdks/schemaid/README.md#delete) - Delete Schema
* [get](docs/sdks/schemaid/README.md#get) - Get Schema by ID
* [update](docs/sdks/schemaid/README.md#update) - Update Schema

### [Schemas](docs/sdks/schemas/README.md)

* [get](docs/sdks/schemas/README.md#get) - Get a list of Schema objects

### [Script](docs/sdks/script/README.md)

* [create](docs/sdks/script/README.md#create) - Create Script
* [delete](docs/sdks/script/README.md#delete) - Delete Script
* [get](docs/sdks/script/README.md#get) - Get Script by ID
* [update](docs/sdks/script/README.md#update) - Update Script

### [Scripts](docs/sdks/scripts/README.md)

* [get](docs/sdks/scripts/README.md#get) - Get a list of Script objects

### [Search](docs/sdks/search/README.md)

* [dispatch_search](docs/sdks/search/README.md#dispatch_search) - Dispatch search *id* to worker nodes filtered by worker node filter using RPC

### [SearchDoc](docs/sdks/searchdoc/README.md)

* [get](docs/sdks/searchdoc/README.md#get) - Get Search documentation

### [SearchJob](docs/sdks/searchjob/README.md)

* [create](docs/sdks/searchjob/README.md#create) - Create SearchJob
* [delete](docs/sdks/searchjob/README.md#delete) - Delete SearchJob
* [get](docs/sdks/searchjob/README.md#get) - Get SearchJob by ID
* [update](docs/sdks/searchjob/README.md#update) - Update SearchJob

### [SearchJobMetrics](docs/sdks/searchjobmetrics/README.md)

* [get](docs/sdks/searchjobmetrics/README.md#get) - Get search job metrics

### [SearchJobs](docs/sdks/searchjobs/README.md)

* [get](docs/sdks/searchjobs/README.md#get) - Get a list of SearchJob objects

### [SearchLimits](docs/sdks/searchlimits/README.md)

* [get](docs/sdks/searchlimits/README.md#get) - Get search limits

### [SearchLogs](docs/sdks/searchlogs/README.md)

* [get](docs/sdks/searchlogs/README.md#get) - Get search logs

### [SearchTimeline](docs/sdks/searchtimeline/README.md)

* [get](docs/sdks/searchtimeline/README.md#get) - Get search timeline

### [SpecifiedOutput](docs/sdks/specifiedoutput/README.md)

* [get](docs/sdks/specifiedoutput/README.md#get) - Get samples data for the specified output. Used to get sample data for the test action.

### [StageDistributedPackage](docs/sdks/stagedistributedpackage/README.md)

* [post](docs/sdks/stagedistributedpackage/README.md#post) - Stage distributed group upgrade

### [SystemInfo](docs/sdks/systeminfo/README.md)

* [get](docs/sdks/systeminfo/README.md#get) - Get basic system information

### [TaskError](docs/sdks/taskerror/README.md)

* [get](docs/sdks/taskerror/README.md#get) - Get Task errors for a job by id

### [TaskErrors](docs/sdks/taskerrors/README.md)

* [get](docs/sdks/taskerrors/README.md#get) - Get Task errors for a job by id

### [TestDatabaseConnection](docs/sdks/testdatabaseconnection/README.md)

* [post](docs/sdks/testdatabaseconnection/README.md#post) - Test a database connection given a type and connectionString

### [TextualDiff](docs/sdks/textualdiff/README.md)

* [get](docs/sdks/textualdiff/README.md#get) - get the textual diff for given commit

### [TrustPolicies](docs/sdks/trustpolicies/README.md)

* [get](docs/sdks/trustpolicies/README.md#get) - Get a list of TrustPolicy objects

### [UIState](docs/sdks/uistate/README.md)

* [get](docs/sdks/uistate/README.md#get) - Get UI state by key
* [update](docs/sdks/uistate/README.md#update) - Update UI state by key

### [User](docs/sdks/user/README.md)

* [create_user](docs/sdks/user/README.md#create_user) - Create User

### [UserAuth](docs/sdks/userauth/README.md)

* [logout](docs/sdks/userauth/README.md#logout) - Log current user out

### [UserID](docs/sdks/userid/README.md)

* [delete](docs/sdks/userid/README.md#delete) - Delete User
* [get](docs/sdks/userid/README.md#get) - Get User by ID

### [UserObject](docs/sdks/userobject/README.md)

* [get](docs/sdks/userobject/README.md#get) - Get a list of User objects
* [update](docs/sdks/userobject/README.md#update) - Update User except for their roles

### [UserProperties](docs/sdks/userproperties/README.md)

* [update](docs/sdks/userproperties/README.md#update) - Update User properties – admin use only

### [Versioning](docs/sdks/versioning/README.md)

* [get](docs/sdks/versioning/README.md#get) - Get info about versioning availability

### [WorkerEdgeNodes](docs/sdks/workeredgenodes/README.md)

* [get](docs/sdks/workeredgenodes/README.md#get) - get worker and edge nodes
* [restarts](docs/sdks/workeredgenodes/README.md#restarts) - restarts worker nodes

### [WorkerEdgeNodesCount](docs/sdks/workeredgenodescount/README.md)

* [get](docs/sdks/workeredgenodescount/README.md#get) - get worker and edge nodes count

### [WorkingTree](docs/sdks/workingtree/README.md)

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
