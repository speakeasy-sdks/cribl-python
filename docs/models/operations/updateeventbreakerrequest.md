# UpdateEventBreakerRequest


## Fields

| Field                                                                                  | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `id`                                                                                   | *Optional[str]*                                                                        | :heavy_check_mark:                                                                     | Unique ID                                                                              |
| `event_breaker_ruleset`                                                                | [Optional[shared.EventBreakerRuleset]](undefined/models/shared/eventbreakerruleset.md) | :heavy_minus_sign:                                                                     | Event Breaker Ruleset object to be updated                                             |