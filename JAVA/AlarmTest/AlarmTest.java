public class AlarmTest {
    public static void main(String[] args) {
        Alarm a = new SmartPhone();
        a.playMusic("아기상어");
        a.beep();

    }
}

interface Alarm {
    void playMusic (String title);
    void beep();
}

class SmartPhone implements Alarm {
    private String phoneNumber;
    public void playMusic(String title) {
        System.out.printf("%d 이 재생됩니다.\n", title);
    }

    public void beep() {
        System.out.println("비피음이 재생됩니다.");
    }
}