# GetChangedFilesResponse


## Fields

| Field                                                                        | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `http_meta`                                                                  | [components.HTTPMetadata](../../models/components/httpmetadata.md)           | :heavy_check_mark:                                                           | N/A                                                                          |
| `changed_files`                                                              | [Optional[components.ChangedFiles]](../../models/components/changedfiles.md) | :heavy_minus_sign:                                                           | a list of GitFilesResponse objects                                           |