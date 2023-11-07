# UpdateSavedQueriesRequest


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `id`                                                                 | *str*                                                                | :heavy_check_mark:                                                   | Unique ID                                                            |
| `saved_query`                                                        | [Optional[components.SavedQuery]](../../models/shared/savedquery.md) | :heavy_minus_sign:                                                   | SavedQuery object to be updated                                      |