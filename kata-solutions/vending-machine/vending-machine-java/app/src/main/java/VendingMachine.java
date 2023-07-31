import java.util.Map;
import java.util.HashMap;

public class VendingMachine {
    // private Map<Choice, Can> choiceCanMap = new HashMap<Choice, Can>();
    // private Map<Choice, Integer> choicePriceMap = new HashMap<Choice, Integer>();
    // private int balanceInCents = 0;
  
    // public void configure(final Choice choice, final Can can, final int priceInCents) {
    //   this.choiceCanMap.put(choice, can);
    //   this.choicePriceMap.put(choice, priceInCents);
    // }
  
    // public void configure(final Choice choice, final Can can) {
    //   configure(choice, can, 0);
    // }

    // public void insert(final int amountInCents) {
    //   this.balanceInCents = amountInCents;
    // }

    // public Can deliver(final Choice choice) {
    //   if (!choiceCanMap.containsKey(choice)) return Can.NOTHING;

    //   final int canPrice = choicePriceMap.get(choice);
    //   if (canPrice > balanceInCents ) return Can.NOTHING;
      
    //   balanceInCents -= canPrice;
    //   return choiceCanMap.get(choice);
    // }

  private Map<Choice, Drawer> choiceDrawerMap = new HashMap<Choice, Drawer>();
  private int balanceInCents = 0;

  public void provision(Choice choice, Drawer drawer) {
    this.choiceDrawerMap.put(choice, drawer);
  }

  public void insertMoney(int priceInCents) {
    this.balanceInCents = priceInCents;
  }
  
  public Can deliver(final Choice choice) {
    if (!this.choiceDrawerMap.containsKey(choice)) return Can.NOTHING;

    final int canPrice = this.choiceDrawerMap.get(choice).priceInCents;

    if (canPrice > this.balanceInCents) return Can.NOTHING;

    this.balanceInCents -= canPrice;
    return this.choiceDrawerMap.get(choice).can;
  }

  public class Drawer {
    public final Can can;
    public final int priceInCents;

    public Drawer(Can can) {
      this(can, 0);
    }

    public Drawer(Can can, int priceInCents) {
      this.can = can;
      this.priceInCents = priceInCents;
    }
  }
}