# GlobalVar

New Global Variable object


## Fields

| Field                                                 | Type                                                  | Required                                              | Description                                           |
| ----------------------------------------------------- | ----------------------------------------------------- | ----------------------------------------------------- | ----------------------------------------------------- |
| `description`                                         | *Optional[str]*                                       | :heavy_minus_sign:                                    | Brief description of this variable. Optional.         |
| `id`                                                  | *str*                                                 | :heavy_check_mark:                                    | Global variable name.                                 |
| `lib`                                                 | *Optional[str]*                                       | :heavy_minus_sign:                                    | N/A                                                   |
| `tags`                                                | *Optional[str]*                                       | :heavy_minus_sign:                                    | One or more tags related to this variable. Optional.  |
| `type`                                                | [GlobalVarType](../../models/shared/globalvartype.md) | :heavy_check_mark:                                    | Type of variable.                                     |
| `value`                                               | *str*                                                 | :heavy_check_mark:                                    | Value of variable                                     |