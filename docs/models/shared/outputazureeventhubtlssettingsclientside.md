# OutputAzureEventhubTLSSettingsClientSide


## Fields

| Field                                                                                                                      | Type                                                                                                                       | Required                                                                                                                   | Description                                                                                                                |
| -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| `disabled`                                                                                                                 | *bool*                                                                                                                     | :heavy_check_mark:                                                                                                         | N/A                                                                                                                        |
| `reject_unauthorized`                                                                                                      | *Optional[bool]*                                                                                                           | :heavy_minus_sign:                                                                                                         | Reject certs that are not authorized by a CA in the CA certificate path, or by another trusted CA (e.g., the system's CA). |