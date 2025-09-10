import logging

import algokit_utils

logger = logging.getLogger(__name__)


# define deployment behaviour based on supplied app spec
def deploy() -> None:
    from smart_contracts.artifacts.contracts.contracts_client import (
        HelloWorldArgs,
        AddArgs,
        SubtractArgs,
        MultiplyArgs,
        ContractsFactory,
    )

    algorand = algokit_utils.AlgorandClient.from_environment()
    deployer_ = algorand.account.from_environment("DEPLOYER")

    factory = algorand.client.get_typed_app_factory(
        ContractsFactory, default_sender=deployer_.address
    )

    app_client, result = factory.deploy(
        on_update=algokit_utils.OnUpdate.AppendApp,
        on_schema_break=algokit_utils.OnSchemaBreak.AppendApp,
    )

    if result.operation_performed in [
        algokit_utils.OperationPerformed.Create,
        algokit_utils.OperationPerformed.Replace,
    ]:
        algorand.send.payment(
            algokit_utils.PaymentParams(
                amount=algokit_utils.AlgoAmount(algo=1),
                sender=deployer_.address,
                receiver=app_client.app_address,
            )
        )

    name = "world"
    response = app_client.send.hello_world(args=HelloWorldArgs(name=name))
    add = app_client.send.add(args=AddArgs(a=5, b=7))
    subtract = app_client.send.subtract(args=SubtractArgs(a=15,b=4))
    multiply = app_client.send.multiply(args=MultiplyArgs(a=10,b=2))
    logger.info(
        f"with name={name}, received: {response.abi_return}"
        f" \nAddition result is {add.abi_return}"
        f"\n Subtraction result is  {subtract.abi_return}"
        f"\n Multiplication result is {multiply.abi_return}"
    )
