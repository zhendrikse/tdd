from dataclasses import dataclass


@dataclass
class OrderApprovalRequest:
    _order_id: int
    _approved: bool = False

    def get_order_id(self):
        return self._order_id

    def approve(self):
        self._approved = True

    def is_approved(self):
        return self._approved
