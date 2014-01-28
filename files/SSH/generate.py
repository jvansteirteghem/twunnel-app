import twunnel.generator

configuration = \
{
    "KEY":
    {
        "FILE": "KP.pem",
        "PASSPHRASE": ""
    }
}

twunnel.generator.generateKey(configuration)