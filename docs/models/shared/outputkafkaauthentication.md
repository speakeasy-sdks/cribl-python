# OutputKafkaAuthentication

Authentication parameters to use when connecting to brokers. Using TLS is highly recommended.


## Fields

| Field                                                                                                             | Type                                                                                                              | Required                                                                                                          | Description                                                                                                       |
| ----------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- |
| `disabled`                                                                                                        | *bool*                                                                                                            | :heavy_check_mark:                                                                                                | Enable Authentication                                                                                             |
| `mechanism`                                                                                                       | [Optional[OutputKafkaAuthenticationSASLMechanism]](../../models/shared/outputkafkaauthenticationsaslmechanism.md) | :heavy_minus_sign:                                                                                                | SASL authentication mechanism to use.                                                                             |