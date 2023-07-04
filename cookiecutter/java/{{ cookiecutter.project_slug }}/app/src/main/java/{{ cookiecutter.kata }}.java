public class {{ cookiecutter.kata }} {
    public String getGreeting() {
        return "Hello World!";
    }

    public static void main(String[] args) {
        System.out.println(new {{ cookiecutter.kata }}().getGreeting());
    }
}
