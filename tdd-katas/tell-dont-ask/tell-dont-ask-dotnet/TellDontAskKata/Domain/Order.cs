using System.Collections.Generic;

namespace TellDontAskKata.Main.Domain
{
    public class Order
    {
        public decimal Total { get; set; }
        public string Currency { get; set; } = default!;
        public IList<OrderItem> Items { get; set; } = default!;
        public decimal Tax { get; set; }
        public OrderStatus Status { get; set; }
        public int Id { get; set; }
    }
}
