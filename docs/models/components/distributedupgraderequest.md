# DistributedUpgradeRequest


## Fields

| Field                                                                                       | Type                                                                                        | Required                                                                                    | Description                                                                                 |
| ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- |
| `package_urls`                                                                              | List[[components.PackageUrls](../../models/components/packageurls.md)]                      | :heavy_minus_sign:                                                                          | Provide your own URLs or local paths for platform-specific Cribl packages.                  |
| `upgrade_mode`                                                                              | [Optional[components.UpgradeMode]](../../models/components/upgrademode.md)                  | :heavy_minus_sign:                                                                          | N/A                                                                                         |
| `upgrade_percentage`                                                                        | *Optional[int]*                                                                             | :heavy_minus_sign:                                                                          | Percentage of the total worker nodes on the group to run the upgrade on                     |
| `worker_retries`                                                                            | *Optional[int]*                                                                             | :heavy_minus_sign:                                                                          | Number of times to retry conncecting to a worker node before marking the upgrade as failed. |
| `worker_retry_delay`                                                                        | *Optional[int]*                                                                             | :heavy_minus_sign:                                                                          | Delay between retries                                                                       |