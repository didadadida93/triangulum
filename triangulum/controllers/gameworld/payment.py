from collections import Callable

from triangulum.controllers.base import BaseController
from triangulum.utils.enums import ShopVersion
from triangulum.utils.exceptions import ActionNotImplementedError


class Payment(BaseController):
    def __init__(self, action_handler: Callable):
        super().__init__(action_handler=action_handler, controller='payment')

    def get_payment_shop_url(self, shop_version: ShopVersion) -> dict:
        return self.invoke_action(
            action='getPaymentShopUrl',
            params={
                'shopVersion': shop_version,
            }
        )

    def get_smallest_package(self, feature_price: int) -> dict:
        raise ActionNotImplementedError

        # return self.invoke_action(
        #     action='getSmallestPackage',
        #     params={
        #         'featurePrice': feature_price,  # TODO: Enum this
        #     }
        # )
