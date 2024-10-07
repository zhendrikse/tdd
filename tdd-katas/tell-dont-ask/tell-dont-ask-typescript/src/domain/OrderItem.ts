import Product from "./Product";
import bigDecimal from "js-big-decimal";

export default class OrderItem {
    private _product: Product = new Product();
    private _quantity: number = 0;
    private _taxedAmount: bigDecimal = new bigDecimal(0);
    private _tax: bigDecimal = new bigDecimal(0);

    constructor() {}

    get product(): Product {
        return this._product;
    }

    set product(value: Product) {
        this._product = value;
    }

    get quantity(): number {
        return this._quantity;
    }

    set quantity(value: number) {
        this._quantity = value;
    }

    get taxedAmount(): bigDecimal {
        return this._taxedAmount;
    }

    set taxedAmount(value: bigDecimal) {
        this._taxedAmount = value;
    }

    get tax(): bigDecimal {
        return this._tax;
    }

    set tax(value: bigDecimal) {
        this._tax = value;
    }
}