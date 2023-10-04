# OutputElasticUrls


## Fields

| Field                                                                      | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `url`                                                                      | *Optional[str]*                                                            | :heavy_check_mark:                                                         | URL to an Elastic node to send events to – e.g., http://elastic:9200/_bulk |
| `weight`                                                                   | *Optional[int]*                                                            | :heavy_minus_sign:                                                         | The weight to use for load-balancing purposes.                             |