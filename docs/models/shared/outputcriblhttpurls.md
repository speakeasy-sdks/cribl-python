# OutputCriblHTTPUrls


## Fields

| Field                                                                 | Type                                                                  | Required                                                              | Description                                                           |
| --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- |
| `url`                                                                 | *str*                                                                 | :heavy_check_mark:                                                    | URL of a Cribl Worker to send events to, e.g., http://localhost:10200 |
| `weight`                                                              | *Optional[int]*                                                       | :heavy_minus_sign:                                                    | The weight to use for load-balancing purposes.                        |