public class CurrencyTest {
    public static void main(String[] args) {
        KRW won = new KRW(1500.00);
        USD doller = new USD(100.50);
        EUR euro = new EUR(260.75);

        Currency[] Currencys = {won, doller, euro};
        for (int i = 0; i < Currencys.length; i++) {
            Currencys[i].printInfo();
            System.out.println();
        }
    }
}

abstract class Currency {
    protected double amount;
    protected void printInfo() {

    }
}
class KRW extends Currency {

    KRW(double _amount) {
        amount = _amount;
    }
    protected void printInfo() {
        System.out.printf("KRW: %.2f 원", amount);
    }
}
class USD extends Currency {
    USD(double _amount) {
        amount = _amount;
    }
    protected void printInfo() {
        System.out.printf("USD: %.2f 달러", amount);
    }
}
class EUR extends Currency {
    EUR(double _amount) {
        amount = _amount;
    }
    protected void printInfo() {
        System.out.printf("EUR: %.2f 유로", amount);
    }
}
