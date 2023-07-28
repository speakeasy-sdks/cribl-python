# KeyMetadataEntity

New KeyMetadataEntity object


## Fields

| Field                                                                                                                                                                        | Type                                                                                                                                                                         | Required                                                                                                                                                                     | Description                                                                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `algorithm`                                                                                                                                                                  | [KeyMetadataEntityEncryptionAlgorithm](../../models/shared/keymetadataentityencryptionalgorithm.md)                                                                          | :heavy_check_mark:                                                                                                                                                           | N/A                                                                                                                                                                          |
| `cipher_key`                                                                                                                                                                 | *Optional[str]*                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                           | N/A                                                                                                                                                                          |
| `created`                                                                                                                                                                    | *Optional[int]*                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                           | N/A                                                                                                                                                                          |
| `description`                                                                                                                                                                | *Optional[str]*                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                           | N/A                                                                                                                                                                          |
| `expires`                                                                                                                                                                    | *Optional[int]*                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                           | N/A                                                                                                                                                                          |
| `key_id`                                                                                                                                                                     | *str*                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                           | N/A                                                                                                                                                                          |
| `keyclass`                                                                                                                                                                   | *int*                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                           | N/A                                                                                                                                                                          |
| `kms`                                                                                                                                                                        | [KeyMetadataEntityKMSForThisKey](../../models/shared/keymetadataentitykmsforthiskey.md)                                                                                      | :heavy_check_mark:                                                                                                                                                           | N/A                                                                                                                                                                          |
| `plain_key`                                                                                                                                                                  | *Optional[str]*                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                           | N/A                                                                                                                                                                          |
| `use_iv`                                                                                                                                                                     | *Optional[bool]*                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                           | Seed encryption with a [nonce](https://en.wikipedia.org/wiki/Cryptographic_nonce) to make the key more random and unique. Must be toggled on with the aes-256-gcm algorithm. |