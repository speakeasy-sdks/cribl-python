# LicenseUsageMetrics
(*.license_usage_metrics*)

### Available Operations

* [get](#get) - Get license usage metrics, aggregated by day, up to last 90 days

## get

Get license usage metrics, aggregated by day, up to last 90 days

### Example Usage

```python
import cribl

s = cribl.Cribl(
    bearer_auth="",
)


res = s.license_usage_metrics.get()

if res.daily_metrics is not None:
    # handle response
    pass
```


### Response

**[operations.GetLicenseUsageMetricsResponse](../../models/operations/getlicenseusagemetricsresponse.md)**

