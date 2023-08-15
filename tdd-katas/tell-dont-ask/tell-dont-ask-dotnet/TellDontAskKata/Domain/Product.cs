namespace TellDontAskKata.Main.Domain
{
    public class Product
    {
        public string Name { get; set; } = default!;
        public decimal Price { get; set; }
        public Category Category { get; set; } = default!;
    }
}