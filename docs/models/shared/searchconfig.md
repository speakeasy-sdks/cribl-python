# SearchConfig


## Fields

| Field                                                   | Type                                                    | Required                                                | Description                                             |
| ------------------------------------------------------- | ------------------------------------------------------- | ------------------------------------------------------- | ------------------------------------------------------- |
| `datasets`                                              | list[*str*]                                             | :heavy_check_mark:                                      | N/A                                                     |
| `has_send_operator`                                     | *bool*                                                  | :heavy_check_mark:                                      | N/A                                                     |
| `ordered_field_names`                                   | list[*str*]                                             | :heavy_check_mark:                                      | N/A                                                     |
| `search_terms`                                          | list[[SearchTerm](../../models/shared/searchterm.md)]   | :heavy_check_mark:                                      | N/A                                                     |
| `sort_fields`                                           | list[[SortByField](../../models/shared/sortbyfield.md)] | :heavy_minus_sign:                                      | N/A                                                     |
| `suppress_event_marking`                                | *bool*                                                  | :heavy_check_mark:                                      | N/A                                                     |
| `use_formatted_visualization`                           | *bool*                                                  | :heavy_check_mark:                                      | N/A                                                     |