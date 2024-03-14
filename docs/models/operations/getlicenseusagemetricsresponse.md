# GetLicenseUsageMetricsResponse


## Fields

| Field                                                                        | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `http_meta`                                                                  | [components.HTTPMetadata](../../models/components/httpmetadata.md)           | :heavy_check_mark:                                                           | N/A                                                                          |
| `daily_metrics`                                                              | [Optional[components.DailyMetrics]](../../models/components/dailymetrics.md) | :heavy_minus_sign:                                                           | a list of DailyUsageMetrics objects                                          |