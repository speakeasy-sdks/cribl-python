# EventBreakerRulesetRules


## Fields

| Field                                                                                                                               | Type                                                                                                                                | Required                                                                                                                            | Description                                                                                                                         |
| ----------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- |
| `condition`                                                                                                                         | *Optional[str]*                                                                                                                     | :heavy_minus_sign:                                                                                                                  | Filter expression (JS) that matches data to apply rule to. To test your sample, use the maximize icon on the right.                 |
| `definitions`                                                                                                                       | [Optional[components.Definitions]](../../models/components/definitions.md)                                                          | :heavy_minus_sign:                                                                                                                  | N/A                                                                                                                                 |
| `disabled`                                                                                                                          | *Optional[bool]*                                                                                                                    | :heavy_minus_sign:                                                                                                                  | Allows breaker rule to be enabled or disabled, default is enabled.                                                                  |
| `fields`                                                                                                                            | List[[components.Fields](../../models/components/fields.md)]                                                                        | :heavy_minus_sign:                                                                                                                  | Key value pairs to be added to each event.                                                                                          |
| `max_event_bytes`                                                                                                                   | *Optional[int]*                                                                                                                     | :heavy_minus_sign:                                                                                                                  | The maximum number of bytes that an event can be before being flushed to the pipelines                                              |
| `name`                                                                                                                              | *str*                                                                                                                               | :heavy_check_mark:                                                                                                                  | N/A                                                                                                                                 |
| `parser_enabled`                                                                                                                    | *Optional[bool]*                                                                                                                    | :heavy_minus_sign:                                                                                                                  | Parser.                                                                                                                             |
| `timestamp`                                                                                                                         | [components.EventBreakerRulesetTimestampFormat](../../models/components/eventbreakerrulesettimestampformat.md)                      | :heavy_check_mark:                                                                                                                  | Auto, manual format (strptime) or current time.                                                                                     |
| `timestamp_anchor_regex`                                                                                                            | *Optional[str]*                                                                                                                     | :heavy_minus_sign:                                                                                                                  | Regex to match before attempting timestamp extraction. Use $ (end of string anchor) to not perform extraction.                      |
| `timestamp_earliest`                                                                                                                | *Optional[str]*                                                                                                                     | :heavy_minus_sign:                                                                                                                  | The earliest timestamp value allowed relative to now. E.g., -42years. Parsed values prior to this date will be set to current time. |
| `timestamp_latest`                                                                                                                  | *Optional[str]*                                                                                                                     | :heavy_minus_sign:                                                                                                                  | The latest timestamp value allowed relative to now. E.g., +42days. Parsed values after this date will be set to current time.       |
| `timestamp_timezone`                                                                                                                | *Optional[str]*                                                                                                                     | :heavy_minus_sign:                                                                                                                  | Timezone to assign to timestamps without timezone info.                                                                             |
| `type`                                                                                                                              | [Optional[components.EventBreakerType]](../../models/components/eventbreakertype.md)                                                | :heavy_minus_sign:                                                                                                                  | Event Breaker Type                                                                                                                  |