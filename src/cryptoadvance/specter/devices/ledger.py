from . import DeviceTypes
from .hwi_device import HWIDevice


class Ledger(HWIDevice):
    device_type = DeviceTypes.LEDGER
    name = "Ledger"
    icon = "ledger_icon.svg"

    supports_policy_registration = True

    def create_psbts(self, base64_psbt, wallet):
        return {"hwi": wallet.fill_psbt(base64_psbt, non_witness=True)}
