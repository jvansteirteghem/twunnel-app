from twisted.application import service
import twunnel.dns_resolver
import twunnel.local_proxy_server
import twunnel.logger

configuration = \
{
    "LOGGER":
    {
        "LEVEL": 3
    },
    "DNS_RESOLVER":
    {
        "HOSTS":
        {
            "FILE": ""
        },
        "SERVERS":
        [
            # {
                # "ADDRESS": "",
                # "PORT": 0
            # }
        ]
    },
    "PROXY_SERVERS":
    [
        # {
            # "TYPE": "HTTPS",
            # "ADDRESS": "",
            # "PORT": 0,
            # "ACCOUNT":
            # {
            #     "NAME": "",
            #     "PASSWORD": ""
            # }
            
            # "TYPE": "SOCKS5",
            # "ADDRESS": "",
            # "PORT": 0,
            # "ACCOUNT":
            # {
            #     "NAME": "",
            #     "PASSWORD": ""
            # }
        # }
    ],
    "LOCAL_PROXY_SERVER":
    {
        # "TYPE": "HTTPS",
        # "ADDRESS": "",
        # "PORT": 0
        
        # "TYPE": "SOCKS5",
        # "ADDRESS": "",
        # "PORT": 0,
        # "ACCOUNTS":
        # [
        #     {
        #         "NAME": "",
        #         "PASSWORD": ""
        #     }
        # ]
    },
    "REMOTE_PROXY_SERVERS":
    [
        # {
            # "TYPE": "SSH",
            # "ADDRESS": "",
            # "PORT": 0,
            # "KEY":
            # {
            #     "FINGERPRINT": ""
            # },
            # "ACCOUNT":
            # {
            #     "NAME": "",
            #     "PASSWORD": "",
            #     "KEYS":
            #     [
            #         {
            #             "PUBLIC":
            #             {
            #                 "FILE": "",
            #                 "PASSPHRASE": ""
            #             },
            #             "PRIVATE":
            #             {
            #                 "FILE": "",
            #                 "PASSPHRASE": ""
            #             }
            #         }
            #     ],
            #     "CONNECTIONS": 0
            # }
            
            # "TYPE": "WS",
            # "ADDRESS": "",
            # "PORT": 0,
            # "ACCOUNT":
            # {
            #     "NAME": "",
            #     "PASSWORD": ""
            # }
            
            # "TYPE": "WSS",
            # "ADDRESS": "",
            # "PORT": 0,
            # "CERTIFICATE":
            # {
            #     "AUTHORITY":
            #     {
            #         "FILE": ""
            #     }
            # },
            # "ACCOUNT":
            # {
            #     "NAME": "",
            #     "PASSWORD": ""
            # }
        # }
    ]
}

twunnel.logger.configure(configuration)

resolver = twunnel.dns_resolver.createResolver(configuration)
if resolver is not None:
    twunnel.dns_resolver.setDefaultResolver(resolver)

class ApplicationService(service.Service):
    def __init__(self, configuration):
        twunnel.logger.log(3, "trace: ApplicationService.__init__")
        
        self.port = twunnel.local_proxy_server.createPort(configuration)
    
    def startService(self):
        twunnel.logger.log(3, "trace: ApplicationService.startService")
        
        if self.port != None:
            self.port.startListening()
    
    def stopService(self):
        twunnel.logger.log(3, "trace: ApplicationService.stopService")
        
        if self.port != None:
            self.port.stopListening()

application = service.Application("local")
applicationService = ApplicationService(configuration)
applicationService.setServiceParent(application)