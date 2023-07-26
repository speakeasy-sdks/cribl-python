# LicenseInfo


## Fields

| Field                                                     | Type                                                      | Required                                                  | Description                                               |
| --------------------------------------------------------- | --------------------------------------------------------- | --------------------------------------------------------- | --------------------------------------------------------- |
| `effective_class`                                         | [LicenseType](../../models/shared/licensetype.md)         | :heavy_check_mark:                                        | N/A                                                       |
| `email`                                                   | *Optional[str]*                                           | :heavy_minus_sign:                                        | N/A                                                       |
| `expiration`                                              | *int*                                                     | :heavy_check_mark:                                        | N/A                                                       |
| `guid`                                                    | *str*                                                     | :heavy_check_mark:                                        | N/A                                                       |
| `is_running_in_saa_s`                                     | *bool*                                                    | :heavy_check_mark:                                        | N/A                                                       |
| `is_splunk_app`                                           | *Optional[bool]*                                          | :heavy_minus_sign:                                        | N/A                                                       |
| `license_enforce_reason`                                  | *str*                                                     | :heavy_check_mark:                                        | N/A                                                       |
| `limits`                                                  | dict[str, *Any*]                                          | :heavy_check_mark:                                        | N/A                                                       |
| `phone_home`                                              | *bool*                                                    | :heavy_check_mark:                                        | N/A                                                       |
| `phone_home_grace`                                        | *int*                                                     | :heavy_check_mark:                                        | N/A                                                       |
| `quota`                                                   | *int*                                                     | :heavy_check_mark:                                        | N/A                                                       |
| `type`                                                    | [LicenseInfoType](../../models/shared/licenseinfotype.md) | :heavy_check_mark:                                        | N/A                                                       |