# OutputKafkaAuthentication

Authentication parameters to use when connecting to brokers. Using TLS is highly recommended.


## Fields

| Field                                                                                                | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `disabled`                                                                                           | *Optional[bool]*                                                                                     | :heavy_minus_sign:                                                                                   | Enable Authentication                                                                                |
| `mechanism`                                                                                          | [Optional[components.OutputKafkaSASLMechanism]](../../models/components/outputkafkasaslmechanism.md) | :heavy_minus_sign:                                                                                   | SASL authentication mechanism to use.                                                                |