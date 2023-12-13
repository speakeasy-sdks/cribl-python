# LicenseUsageMetrics
(*license_usage_metrics*)

### Available Operations

* [get](#get) - Get license usage metrics, aggregated by day, up to last 90 days

## get

Get license usage metrics, aggregated by day, up to last 90 days

### Example Usage

```python
import cribl

s = cribl.Cribl(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.license_usage_metrics.get()

if res.daily_metrics is not None:
    # handle response
    pass
```


### Response

**[operations.GetLicenseUsageMetricsResponse](../../models/operations/getlicenseusagemetricsresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 401,500          | application/json |
| errors.SDKError  | 400-600          | */*              |
