# OutputSplunkHecUrls


## Fields

| Field                                                                                                | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `url`                                                                                                | *str*                                                                                                | :heavy_check_mark:                                                                                   | URL to a Splunk HEC endpoint to send events to, e.g., http://localhost:8088/services/collector/event |
| `weight`                                                                                             | *Optional[int]*                                                                                      | :heavy_minus_sign:                                                                                   | The weight to use for load-balancing purposes.                                                       |