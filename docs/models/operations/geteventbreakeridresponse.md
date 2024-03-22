# GetEventBreakerIDResponse


## Fields

| Field                                                                                        | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `http_meta`                                                                                  | [components.HTTPMetadata](../../models/components/httpmetadata.md)                           | :heavy_check_mark:                                                                           | N/A                                                                                          |
| `event_breaker_rulesets`                                                                     | [Optional[components.EventBreakerRulesets]](../../models/components/eventbreakerrulesets.md) | :heavy_minus_sign:                                                                           | a list of Event Breaker Ruleset objects                                                      |