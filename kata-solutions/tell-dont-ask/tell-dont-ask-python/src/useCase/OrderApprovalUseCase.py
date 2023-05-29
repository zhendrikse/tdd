from src.repository.OrderRepository import OrderRepository
from src.useCase.OrderApprovalRequest import OrderApprovalRequest

class OrderApprovalUseCase:
    def __init__(self, order_repository: OrderRepository):
        self.order_repository = order_repository

    def run(self, request: OrderApprovalRequest):
        order = self.order_repository.get_by_id(request.get_order_id())

        if request.is_approved():
          order.approve()
        else:
          order.reject()

        self.order_repository.save(order)
