# Authentication

Authentication parameters to use when connecting to brokers. Using TLS is highly recommended.


## Fields

| Field                                                                      | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `disabled`                                                                 | *Optional[bool]*                                                           | :heavy_minus_sign:                                                         | Enable authentication.                                                     |
| `mechanism`                                                                | [Optional[components.SASLMechanism]](../../models/shared/saslmechanism.md) | :heavy_minus_sign:                                                         | SASL authentication mechanism to use                                       |