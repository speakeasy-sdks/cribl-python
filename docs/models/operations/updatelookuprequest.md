# UpdateLookupRequest


## Fields

| Field                                                                                | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `id`                                                                                 | *str*                                                                                | :heavy_check_mark:                                                                   | Unique ID                                                                            |
| `lookup_file`                                                                        | [Optional[Union[components.One, components.Two]]](../../models/shared/lookupfile.md) | :heavy_minus_sign:                                                                   | LookupFile object to be updated                                                      |