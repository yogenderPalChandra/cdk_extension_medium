from constructs import Construct

from aws_cdk import (
    Aws,
)

from aws_cdk_extensions.aws_ssm_extensions.document import ShellScriptDocument

class Singleton(type):
    __instance = None
    def __call__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__call__(*args, **kwargs)
        return cls.__instance


class GetTestDocument(ShellScriptDocument, metaclass=Singleton):
    def __init__(self, scope: Construct, construct_id: str):
        super().__init__(
            scope,
            construct_id,
            document_name_tag_value=f'{Aws.STACK_NAME}-Test',
            parameters={
                'uploadUrl': {
                    'type': 'String',
                    'description': 'Presigned upload URL to staging bucket'
                }
            },
            commands=[
                'command 1',
                'command 2',
                'command ${RANDOM_STRING}.json'
            ]
        )
