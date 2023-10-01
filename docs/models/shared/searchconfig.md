# SearchConfig


## Fields

| Field                                                              | Type                                                               | Required                                                           | Description                                                        |
| ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ |
| `datasets`                                                         | list[*str*]                                                        | :heavy_check_mark:                                                 | N/A                                                                |
| `has_send_operator`                                                | *Optional[bool]*                                                   | :heavy_check_mark:                                                 | N/A                                                                |
| `ordered_field_names`                                              | list[*str*]                                                        | :heavy_check_mark:                                                 | N/A                                                                |
| `search_terms`                                                     | list[[shared.SearchTerm](undefined/models/shared/searchterm.md)]   | :heavy_check_mark:                                                 | N/A                                                                |
| `sort_fields`                                                      | list[[shared.SortByField](undefined/models/shared/sortbyfield.md)] | :heavy_minus_sign:                                                 | N/A                                                                |
| `suppress_event_marking`                                           | *Optional[bool]*                                                   | :heavy_check_mark:                                                 | N/A                                                                |
| `use_formatted_visualization`                                      | *Optional[bool]*                                                   | :heavy_check_mark:                                                 | N/A                                                                |