export default class OrderShipmentRequest {
    private _orderId: number = 0;

    constructor() {}

    get orderId(): number {
        return this._orderId;
    }

    set orderId(value: number) {
        this._orderId = value;
    }
}