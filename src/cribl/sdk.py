"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

import requests as requests_http
from .appscopelibentries import AppscopeLibEntries
from .appscopelibentry import AppscopeLibEntry
from .authenticationsettings import AuthenticationSettings
from .authorizations import Authorizations
from .authtoken import AuthToken
from .branches import Branches
from .bulletinmessage import BulletinMessage
from .bulletinmessages import BulletinMessages
from .bytes import Bytes
from .cancelrunninggroup import CancelRunningGroup
from .certificate import Certificate
from .certificates import Certificates
from .changedfiles import ChangedFiles
from .changelogs import Changelogs
from .changelogviewstate import ChangelogViewState
from .clientroles import ClientRoles
from .cluis import Cluis
from .collector import Collector
from .collectorobject import CollectorObject
from .commit import Commit
from .condition import Condition
from .conditions import Conditions
from .configgroup import ConfigGroup
from .configuredcollectors import ConfiguredCollectors
from .container import Container
from .countfile import CountFile
from .createpipeline import CreatePipeline
from .criblmetadata import CriblMetadata
from .criblssettings import CriblsSettings
from .criblsystemsettings import CriblSystemSettings
from .currentconfig import CurrentConfig
from .databaseconnection import DatabaseConnection
from .databaseconnectionconfigid import DatabaseConnectionConfigID
from .datasample import DataSample
from .datasampleid import DataSampleID
from .dataset import Dataset
from .datasetobject import DatasetObject
from .datasetobjects import DatasetObjects
from .datasets import Datasets
from .destinationqueue import DestinationQueue
from .diagbundle import DiagBundle
from .diagbundles import DiagBundles
from .distributeddeployment import DistributedDeployment
from .edgehostfiles import EdgeHostFiles
from .edgelisting import EdgeListing
from .eventbreaker import EventBreaker
from .eventbreakerid import EventBreakerID
from .eventbreakerondata import EventBreakerOnData
from .events import Events
from .executedistributedupgrade import ExecuteDistributedUpgrade
from .executorid import ExecutorID
from .executorobject import ExecutorObject
from .existingdiagbundles import ExistingDiagBundles
from .feature import Feature
from .features import Features
from .fieldsummaries import FieldSummaries
from .fleetmapping import FleetMapping
from .fleetmappings import FleetMappings
from .fleetorworkergroup import FleetOrWorkerGroup
from .functionid import FunctionID
from .gitsettings import GitSettings
from .givecriblversion import GiveCriblVersion
from .globalvariable import GlobalVariable
from .globalvariableid import GlobalVariableID
from .grokfile import GrokFile
from .grokfiles import GrokFiles
from .groupbundle import GroupBundle
from .groups import Groups
from .healthinfo import HealthInfo
from .hostmetadatastructure import HostMetadataStructure
from .idpauth import IDPAuth
from .idpuserauth import IDPUserAuth
from .internalsystemmetrics import InternalSystemMetrics
from .javascriptexpression import JavascriptExpression
from .job import Job
from .jobinfos import JobInfos
from .jobresult import JobResult
from .jobresults import JobResults
from .jobstatus import JobStatus
from .keymetadataentities import KeyMetadataEntities
from .keymetadataentity import KeyMetadataEntity
from .kmsconfig import KMSConfig
from .kmshealth import KMSHealth
from .latestpq import LatestPQ
from .license import License
from .licenses import Licenses
from .licenseusagemetrics import LicenseUsageMetrics
from .listauthgroup import ListAuthGroup
from .listcontainerdetail import ListContainerDetail
from .listcriblversion import ListCriblVersion
from .listdatabaseconnection import ListDatabaseConnection
from .listdatasample import ListDataSample
from .listeventbreaker import ListEventBreaker
from .listglobalvariable import ListGlobalVariable
from .listparser import ListParser
from .listprocessrunningdetail import ListProcessRunningDetail
from .listschema import ListSchema
from .livedata import LiveData
from .logandtextual import LogandTextual
from .logfilecontent import LogFileContent
from .logfilecontents import LogFileContents
from .logfilelist import LogFileList
from .logfiles import LogFiles
from .logfilescontent import LogFilesContent
from .loggerconfig import LoggerConfig
from .loggerconfigs import LoggerConfigs
from .lookup import Lookup
from .lookups import Lookups
from .mappingruleset import MappingRuleset
from .mappingrulesetid import MappingRulesetID
from .mappingrulesets import MappingRulesets
from .masternodepackage import MasterNodePackage
from .metrics import Metrics
from .notificationtarget import NotificationTarget
from .notificationtargets import NotificationTargets
from .objectfunction import ObjectFunction
from .outputid import OutputID
from .outputobject import OutputObject
from .outputobjects import OutputObjects
from .outputstatus import OutputStatus
from .outputstatusid import OutputStatusID
from .pack import Pack
from .packs import Packs
from .parserid import ParserID
from .parserobject import ParserObject
from .pipelineid import PipelineID
from .pipelineobject import PipelineObject
from .policyrule import PolicyRule
from .policyrules import PolicyRules
from .previouscriblpackage import PreviousCriblPackage
from .processes import Processes
from .processrunningdetail import ProcessRunningDetail
from .profiler import Profiler
from .profilers import Profilers
from .querysnippet import QuerySnippet
from .redirectinfo import RedirectInfo
from .redirectuserauth import RedirectUserAuth
from .regexlibentry import RegexLibEntry
from .regexlibentryid import RegexLibEntryID
from .regexlibentryobject import RegexLibEntryObject
from .reloadcriblsettings import ReloadCriblSettings
from .remoterepo import RemoteRepo
from .requestauth import RequestAuth
from .requestuserauth import RequestUserAuth
from .restartcriblsettings import RestartCriblSettings
from .restsecret import RestSecret
from .restsecrets import RestSecrets
from .role import Role
from .roles import Roles
from .routelistid import RouteListID
from .routelists import RouteLists
from .routeobject import RouteObject
from .samplecontent import SampleContent
from .sampleevents import SampleEvents
from .sampleoutput import SampleOutput
from .savedjob import SavedJob
from .savedjobs import SavedJobs
from .savedqueries import SavedQueries
from .savedquery import SavedQuery
from .schema import Schema
from .schemaid import SchemaID
from .schemas import Schemas
from .script import Script
from .scripts import Scripts
from .sdkconfiguration import SDKConfiguration
from .search import Search
from .searchdoc import SearchDoc
from .searchjob import SearchJob
from .searchjobmetrics import SearchJobMetrics
from .searchjobs import SearchJobs
from .searchlimits import SearchLimits
from .searchlogs import SearchLogs
from .searchtimeline import SearchTimeline
from .specifiedoutput import SpecifiedOutput
from .stagedistributedpackage import StageDistributedPackage
from .systeminfo import SystemInfo
from .taskerror import TaskError
from .taskerrors import TaskErrors
from .testdatabaseconnection import TestDatabaseConnection
from .textualdiff import TextualDiff
from .trustpolicies import TrustPolicies
from .uistate import UIState
from .user import User
from .userauth import UserAuth
from .userid import UserID
from .userobject import UserObject
from .userproperties import UserProperties
from .versioning import Versioning
from .workeredgenodes import WorkerEdgeNodes
from .workeredgenodescount import WorkerEdgeNodesCount
from .workingtree import WorkingTree
from cribl import utils
from cribl._hooks import SDKHooks
from cribl.models import components
from typing import Callable, Dict, Union

class Cribl:
    r"""Cribl API Reference: This API Reference lists available REST endpoints, along with their supported operations for accessing, creating, updating, or deleting resources. See our complementary product documentation at [docs.cribl.io](http://docs.cribl.io)."""
    idp_auth: IDPAuth
    list_auth_group: ListAuthGroup
    auth_token: AuthToken
    user_auth: UserAuth
    cribl_metadata: CriblMetadata
    redirect_user_auth: RedirectUserAuth
    idp_user_auth: IDPUserAuth
    request_user_auth: RequestUserAuth
    redirect_info: RedirectInfo
    request_auth: RequestAuth
    authorizations: Authorizations
    client_roles: ClientRoles
    changelogs: Changelogs
    changelog_view_state: ChangelogViewState
    cluis: Cluis
    collector_object: CollectorObject
    collector: Collector
    conditions: Conditions
    condition: Condition
    list_container_detail: ListContainerDetail
    container: Container
    configured_collectors: ConfiguredCollectors
    events: Events
    bytes: Bytes
    edge_host_files: EdgeHostFiles
    log_file_list: LogFileList
    edge_listing: EdgeListing
    host_metadata_structure: HostMetadataStructure
    list_process_running_detail: ListProcessRunningDetail
    process_running_detail: ProcessRunningDetail
    executor_object: ExecutorObject
    executor_id: ExecutorID
    fleet_mappings: FleetMappings
    fleet_mapping: FleetMapping
    mapping_ruleset: MappingRuleset
    mapping_rulesets: MappingRulesets
    object_function: ObjectFunction
    function_id: FunctionID
    health_info: HealthInfo
    job_infos: JobInfos
    job: Job
    task_error: TaskError
    task_errors: TaskErrors
    job_results: JobResults
    job_result: JobResult
    appscope_lib_entries: AppscopeLibEntries
    appscope_lib_entry: AppscopeLibEntry
    list_event_breaker: ListEventBreaker
    event_breaker: EventBreaker
    event_breaker_id: EventBreakerID
    list_database_connection: ListDatabaseConnection
    database_connection: DatabaseConnection
    test_database_connection: TestDatabaseConnection
    database_connection_config_id: DatabaseConnectionConfigID
    javascript_expression: JavascriptExpression
    grok_files: GrokFiles
    grok_file: GrokFile
    saved_jobs: SavedJobs
    saved_job: SavedJob
    list_schema: ListSchema
    schema: Schema
    schema_id: SchemaID
    list_parser: ListParser
    parser_object: ParserObject
    parser_id: ParserID
    regex_lib_entry_object: RegexLibEntryObject
    regex_lib_entry: RegexLibEntry
    regex_lib_entry_id: RegexLibEntryID
    schemas: Schemas
    list_global_variable: ListGlobalVariable
    global_variable: GlobalVariable
    global_variable_id: GlobalVariableID
    mapping_ruleset_id: MappingRulesetID
    diag_bundles: DiagBundles
    groups: Groups
    config_group: ConfigGroup
    group_bundle: GroupBundle
    fleet_or_worker_group: FleetOrWorkerGroup
    distributed_deployment: DistributedDeployment
    worker_edge_nodes_count: WorkerEdgeNodesCount
    worker_edge_nodes: WorkerEdgeNodes
    notification_targets: NotificationTargets
    notification_target: NotificationTarget
    packs: Packs
    pack: Pack
    pipeline_object: PipelineObject
    create_pipeline: CreatePipeline
    pipeline_id: PipelineID
    sample_events: SampleEvents
    route_lists: RouteLists
    route_list_id: RouteListID
    route_object: RouteObject
    datasets: Datasets
    dataset: Dataset
    dataset_objects: DatasetObjects
    dataset_object: DatasetObject
    search_doc: SearchDoc
    event_breaker_on_data: EventBreakerOnData
    search_jobs: SearchJobs
    search_job: SearchJob
    search: Search
    field_summaries: FieldSummaries
    search_logs: SearchLogs
    search_job_metrics: SearchJobMetrics
    job_status: JobStatus
    search_timeline: SearchTimeline
    query_snippet: QuerySnippet
    saved_queries: SavedQueries
    saved_query: SavedQuery
    trust_policies: TrustPolicies
    kms_config: KMSConfig
    kms_health: KMSHealth
    features: Features
    feature: Feature
    live_data: LiveData
    certificates: Certificates
    certificate: Certificate
    diag_bundle: DiagBundle
    existing_diag_bundles: ExistingDiagBundles
    cancel_running_group: CancelRunningGroup
    previous_cribl_package: PreviousCriblPackage
    stage_distributed_package: StageDistributedPackage
    execute_distributed_upgrade: ExecuteDistributedUpgrade
    system_info: SystemInfo
    log_file_contents: LogFileContents
    key_metadata_entities: KeyMetadataEntities
    key_metadata_entity: KeyMetadataEntity
    licenses: Licenses
    license: License
    license_usage_metrics: LicenseUsageMetrics
    logger_configs: LoggerConfigs
    logger_config: LoggerConfig
    log_files: LogFiles
    log_files_content: LogFilesContent
    log_file_content: LogFileContent
    lookups: Lookups
    lookup: Lookup
    bulletin_messages: BulletinMessages
    bulletin_message: BulletinMessage
    metrics: Metrics
    internal_system_metrics: InternalSystemMetrics
    output_objects: OutputObjects
    output_object: OutputObject
    output_id: OutputID
    destination_queue: DestinationQueue
    latest_pq: LatestPQ
    specified_output: SpecifiedOutput
    sample_output: SampleOutput
    policy_rules: PolicyRules
    policy_rule: PolicyRule
    processes: Processes
    profilers: Profilers
    profiler: Profiler
    roles: Roles
    role: Role
    list_data_sample: ListDataSample
    data_sample: DataSample
    data_sample_id: DataSampleID
    sample_content: SampleContent
    scripts: Scripts
    script: Script
    rest_secrets: RestSecrets
    rest_secret: RestSecret
    cribls_settings: CriblsSettings
    authentication_settings: AuthenticationSettings
    cribl_system_settings: CriblSystemSettings
    git_settings: GitSettings
    reload_cribl_settings: ReloadCriblSettings
    restart_cribl_settings: RestartCriblSettings
    search_limits: SearchLimits
    list_cribl_version: ListCriblVersion
    master_node_package: MasterNodePackage
    give_cribl_version: GiveCriblVersion
    output_status: OutputStatus
    output_status_id: OutputStatusID
    user_object: UserObject
    user: User
    user_id: UserID
    user_properties: UserProperties
    ui_state: UIState
    branches: Branches
    commit: Commit
    count_file: CountFile
    textual_diff: TextualDiff
    changed_files: ChangedFiles
    versioning: Versioning
    current_config: CurrentConfig
    logand_textual: LogandTextual
    working_tree: WorkingTree
    remote_repo: RemoteRepo

    sdk_configuration: SDKConfiguration

    def __init__(self,
                 bearer_auth: Union[str, Callable[[], str]],
                 organization_id: str = None,
                 server_idx: int = None,
                 server_url: str = None,
                 url_params: Dict[str, str] = None,
                 client: requests_http.Session = None,
                 retry_config: utils.RetryConfig = None
                 ) -> None:
        """Instantiates the SDK configuring it with the provided parameters.
        
        :param bearer_auth: The bearer_auth required for authentication
        :type bearer_auth: Union[str, Callable[[], str]]
        :param organization_id: Allows setting the organizationID variable for url substitution
        :type organization_id: str
        :param server_idx: The index of the server to use for all operations
        :type server_idx: int
        :param server_url: The server URL to use for all operations
        :type server_url: str
        :param url_params: Parameters to optionally template the server URL with
        :type url_params: Dict[str, str]
        :param client: The requests.Session HTTP client to use for all operations
        :type client: requests_http.Session
        :param retry_config: The utils.RetryConfig to use globally
        :type retry_config: utils.RetryConfig
        """
        if client is None:
            client = requests_http.Session()
        
        if callable(bearer_auth):
            def security():
                return components.Security(bearer_auth = bearer_auth())
        else:
            security = components.Security(bearer_auth = bearer_auth)
        
        if server_url is not None:
            if url_params is not None:
                server_url = utils.template_url(server_url, url_params)
        server_defaults = [
            {
                'organizationID': organization_id or 'api',
            },
        ]

        self.sdk_configuration = SDKConfiguration(client, security, server_url, server_idx, server_defaults, retry_config=retry_config)

        hooks = SDKHooks()

        current_server_url, *_ = self.sdk_configuration.get_server_details()
        server_url, self.sdk_configuration.client = hooks.sdk_init(current_server_url, self.sdk_configuration.client)
        if current_server_url != server_url:
            self.sdk_configuration.server_url = server_url

        # pylint: disable=protected-access
        self.sdk_configuration._hooks=hooks
       
        self._init_sdks()
    
    def _init_sdks(self):
        self.idp_auth = IDPAuth(self.sdk_configuration)
        self.list_auth_group = ListAuthGroup(self.sdk_configuration)
        self.auth_token = AuthToken(self.sdk_configuration)
        self.user_auth = UserAuth(self.sdk_configuration)
        self.cribl_metadata = CriblMetadata(self.sdk_configuration)
        self.redirect_user_auth = RedirectUserAuth(self.sdk_configuration)
        self.idp_user_auth = IDPUserAuth(self.sdk_configuration)
        self.request_user_auth = RequestUserAuth(self.sdk_configuration)
        self.redirect_info = RedirectInfo(self.sdk_configuration)
        self.request_auth = RequestAuth(self.sdk_configuration)
        self.authorizations = Authorizations(self.sdk_configuration)
        self.client_roles = ClientRoles(self.sdk_configuration)
        self.changelogs = Changelogs(self.sdk_configuration)
        self.changelog_view_state = ChangelogViewState(self.sdk_configuration)
        self.cluis = Cluis(self.sdk_configuration)
        self.collector_object = CollectorObject(self.sdk_configuration)
        self.collector = Collector(self.sdk_configuration)
        self.conditions = Conditions(self.sdk_configuration)
        self.condition = Condition(self.sdk_configuration)
        self.list_container_detail = ListContainerDetail(self.sdk_configuration)
        self.container = Container(self.sdk_configuration)
        self.configured_collectors = ConfiguredCollectors(self.sdk_configuration)
        self.events = Events(self.sdk_configuration)
        self.bytes = Bytes(self.sdk_configuration)
        self.edge_host_files = EdgeHostFiles(self.sdk_configuration)
        self.log_file_list = LogFileList(self.sdk_configuration)
        self.edge_listing = EdgeListing(self.sdk_configuration)
        self.host_metadata_structure = HostMetadataStructure(self.sdk_configuration)
        self.list_process_running_detail = ListProcessRunningDetail(self.sdk_configuration)
        self.process_running_detail = ProcessRunningDetail(self.sdk_configuration)
        self.executor_object = ExecutorObject(self.sdk_configuration)
        self.executor_id = ExecutorID(self.sdk_configuration)
        self.fleet_mappings = FleetMappings(self.sdk_configuration)
        self.fleet_mapping = FleetMapping(self.sdk_configuration)
        self.mapping_ruleset = MappingRuleset(self.sdk_configuration)
        self.mapping_rulesets = MappingRulesets(self.sdk_configuration)
        self.object_function = ObjectFunction(self.sdk_configuration)
        self.function_id = FunctionID(self.sdk_configuration)
        self.health_info = HealthInfo(self.sdk_configuration)
        self.job_infos = JobInfos(self.sdk_configuration)
        self.job = Job(self.sdk_configuration)
        self.task_error = TaskError(self.sdk_configuration)
        self.task_errors = TaskErrors(self.sdk_configuration)
        self.job_results = JobResults(self.sdk_configuration)
        self.job_result = JobResult(self.sdk_configuration)
        self.appscope_lib_entries = AppscopeLibEntries(self.sdk_configuration)
        self.appscope_lib_entry = AppscopeLibEntry(self.sdk_configuration)
        self.list_event_breaker = ListEventBreaker(self.sdk_configuration)
        self.event_breaker = EventBreaker(self.sdk_configuration)
        self.event_breaker_id = EventBreakerID(self.sdk_configuration)
        self.list_database_connection = ListDatabaseConnection(self.sdk_configuration)
        self.database_connection = DatabaseConnection(self.sdk_configuration)
        self.test_database_connection = TestDatabaseConnection(self.sdk_configuration)
        self.database_connection_config_id = DatabaseConnectionConfigID(self.sdk_configuration)
        self.javascript_expression = JavascriptExpression(self.sdk_configuration)
        self.grok_files = GrokFiles(self.sdk_configuration)
        self.grok_file = GrokFile(self.sdk_configuration)
        self.saved_jobs = SavedJobs(self.sdk_configuration)
        self.saved_job = SavedJob(self.sdk_configuration)
        self.list_schema = ListSchema(self.sdk_configuration)
        self.schema = Schema(self.sdk_configuration)
        self.schema_id = SchemaID(self.sdk_configuration)
        self.list_parser = ListParser(self.sdk_configuration)
        self.parser_object = ParserObject(self.sdk_configuration)
        self.parser_id = ParserID(self.sdk_configuration)
        self.regex_lib_entry_object = RegexLibEntryObject(self.sdk_configuration)
        self.regex_lib_entry = RegexLibEntry(self.sdk_configuration)
        self.regex_lib_entry_id = RegexLibEntryID(self.sdk_configuration)
        self.schemas = Schemas(self.sdk_configuration)
        self.list_global_variable = ListGlobalVariable(self.sdk_configuration)
        self.global_variable = GlobalVariable(self.sdk_configuration)
        self.global_variable_id = GlobalVariableID(self.sdk_configuration)
        self.mapping_ruleset_id = MappingRulesetID(self.sdk_configuration)
        self.diag_bundles = DiagBundles(self.sdk_configuration)
        self.groups = Groups(self.sdk_configuration)
        self.config_group = ConfigGroup(self.sdk_configuration)
        self.group_bundle = GroupBundle(self.sdk_configuration)
        self.fleet_or_worker_group = FleetOrWorkerGroup(self.sdk_configuration)
        self.distributed_deployment = DistributedDeployment(self.sdk_configuration)
        self.worker_edge_nodes_count = WorkerEdgeNodesCount(self.sdk_configuration)
        self.worker_edge_nodes = WorkerEdgeNodes(self.sdk_configuration)
        self.notification_targets = NotificationTargets(self.sdk_configuration)
        self.notification_target = NotificationTarget(self.sdk_configuration)
        self.packs = Packs(self.sdk_configuration)
        self.pack = Pack(self.sdk_configuration)
        self.pipeline_object = PipelineObject(self.sdk_configuration)
        self.create_pipeline = CreatePipeline(self.sdk_configuration)
        self.pipeline_id = PipelineID(self.sdk_configuration)
        self.sample_events = SampleEvents(self.sdk_configuration)
        self.route_lists = RouteLists(self.sdk_configuration)
        self.route_list_id = RouteListID(self.sdk_configuration)
        self.route_object = RouteObject(self.sdk_configuration)
        self.datasets = Datasets(self.sdk_configuration)
        self.dataset = Dataset(self.sdk_configuration)
        self.dataset_objects = DatasetObjects(self.sdk_configuration)
        self.dataset_object = DatasetObject(self.sdk_configuration)
        self.search_doc = SearchDoc(self.sdk_configuration)
        self.event_breaker_on_data = EventBreakerOnData(self.sdk_configuration)
        self.search_jobs = SearchJobs(self.sdk_configuration)
        self.search_job = SearchJob(self.sdk_configuration)
        self.search = Search(self.sdk_configuration)
        self.field_summaries = FieldSummaries(self.sdk_configuration)
        self.search_logs = SearchLogs(self.sdk_configuration)
        self.search_job_metrics = SearchJobMetrics(self.sdk_configuration)
        self.job_status = JobStatus(self.sdk_configuration)
        self.search_timeline = SearchTimeline(self.sdk_configuration)
        self.query_snippet = QuerySnippet(self.sdk_configuration)
        self.saved_queries = SavedQueries(self.sdk_configuration)
        self.saved_query = SavedQuery(self.sdk_configuration)
        self.trust_policies = TrustPolicies(self.sdk_configuration)
        self.kms_config = KMSConfig(self.sdk_configuration)
        self.kms_health = KMSHealth(self.sdk_configuration)
        self.features = Features(self.sdk_configuration)
        self.feature = Feature(self.sdk_configuration)
        self.live_data = LiveData(self.sdk_configuration)
        self.certificates = Certificates(self.sdk_configuration)
        self.certificate = Certificate(self.sdk_configuration)
        self.diag_bundle = DiagBundle(self.sdk_configuration)
        self.existing_diag_bundles = ExistingDiagBundles(self.sdk_configuration)
        self.cancel_running_group = CancelRunningGroup(self.sdk_configuration)
        self.previous_cribl_package = PreviousCriblPackage(self.sdk_configuration)
        self.stage_distributed_package = StageDistributedPackage(self.sdk_configuration)
        self.execute_distributed_upgrade = ExecuteDistributedUpgrade(self.sdk_configuration)
        self.system_info = SystemInfo(self.sdk_configuration)
        self.log_file_contents = LogFileContents(self.sdk_configuration)
        self.key_metadata_entities = KeyMetadataEntities(self.sdk_configuration)
        self.key_metadata_entity = KeyMetadataEntity(self.sdk_configuration)
        self.licenses = Licenses(self.sdk_configuration)
        self.license = License(self.sdk_configuration)
        self.license_usage_metrics = LicenseUsageMetrics(self.sdk_configuration)
        self.logger_configs = LoggerConfigs(self.sdk_configuration)
        self.logger_config = LoggerConfig(self.sdk_configuration)
        self.log_files = LogFiles(self.sdk_configuration)
        self.log_files_content = LogFilesContent(self.sdk_configuration)
        self.log_file_content = LogFileContent(self.sdk_configuration)
        self.lookups = Lookups(self.sdk_configuration)
        self.lookup = Lookup(self.sdk_configuration)
        self.bulletin_messages = BulletinMessages(self.sdk_configuration)
        self.bulletin_message = BulletinMessage(self.sdk_configuration)
        self.metrics = Metrics(self.sdk_configuration)
        self.internal_system_metrics = InternalSystemMetrics(self.sdk_configuration)
        self.output_objects = OutputObjects(self.sdk_configuration)
        self.output_object = OutputObject(self.sdk_configuration)
        self.output_id = OutputID(self.sdk_configuration)
        self.destination_queue = DestinationQueue(self.sdk_configuration)
        self.latest_pq = LatestPQ(self.sdk_configuration)
        self.specified_output = SpecifiedOutput(self.sdk_configuration)
        self.sample_output = SampleOutput(self.sdk_configuration)
        self.policy_rules = PolicyRules(self.sdk_configuration)
        self.policy_rule = PolicyRule(self.sdk_configuration)
        self.processes = Processes(self.sdk_configuration)
        self.profilers = Profilers(self.sdk_configuration)
        self.profiler = Profiler(self.sdk_configuration)
        self.roles = Roles(self.sdk_configuration)
        self.role = Role(self.sdk_configuration)
        self.list_data_sample = ListDataSample(self.sdk_configuration)
        self.data_sample = DataSample(self.sdk_configuration)
        self.data_sample_id = DataSampleID(self.sdk_configuration)
        self.sample_content = SampleContent(self.sdk_configuration)
        self.scripts = Scripts(self.sdk_configuration)
        self.script = Script(self.sdk_configuration)
        self.rest_secrets = RestSecrets(self.sdk_configuration)
        self.rest_secret = RestSecret(self.sdk_configuration)
        self.cribls_settings = CriblsSettings(self.sdk_configuration)
        self.authentication_settings = AuthenticationSettings(self.sdk_configuration)
        self.cribl_system_settings = CriblSystemSettings(self.sdk_configuration)
        self.git_settings = GitSettings(self.sdk_configuration)
        self.reload_cribl_settings = ReloadCriblSettings(self.sdk_configuration)
        self.restart_cribl_settings = RestartCriblSettings(self.sdk_configuration)
        self.search_limits = SearchLimits(self.sdk_configuration)
        self.list_cribl_version = ListCriblVersion(self.sdk_configuration)
        self.master_node_package = MasterNodePackage(self.sdk_configuration)
        self.give_cribl_version = GiveCriblVersion(self.sdk_configuration)
        self.output_status = OutputStatus(self.sdk_configuration)
        self.output_status_id = OutputStatusID(self.sdk_configuration)
        self.user_object = UserObject(self.sdk_configuration)
        self.user = User(self.sdk_configuration)
        self.user_id = UserID(self.sdk_configuration)
        self.user_properties = UserProperties(self.sdk_configuration)
        self.ui_state = UIState(self.sdk_configuration)
        self.branches = Branches(self.sdk_configuration)
        self.commit = Commit(self.sdk_configuration)
        self.count_file = CountFile(self.sdk_configuration)
        self.textual_diff = TextualDiff(self.sdk_configuration)
        self.changed_files = ChangedFiles(self.sdk_configuration)
        self.versioning = Versioning(self.sdk_configuration)
        self.current_config = CurrentConfig(self.sdk_configuration)
        self.logand_textual = LogandTextual(self.sdk_configuration)
        self.working_tree = WorkingTree(self.sdk_configuration)
        self.remote_repo = RemoteRepo(self.sdk_configuration)
    