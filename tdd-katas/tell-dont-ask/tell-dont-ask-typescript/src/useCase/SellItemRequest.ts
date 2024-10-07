export default class SellItemRequest {
    private _quantity: number = 0;
    private _productName: string = "";

    constructor() {
    }

    get quantity(): number {
        return this._quantity;
    }

    set quantity(value: number) {
        this._quantity = value;
    }

    get productName(): string {
        return this._productName;
    }

    set productName(value: string) {
        this._productName = value;
    }
}