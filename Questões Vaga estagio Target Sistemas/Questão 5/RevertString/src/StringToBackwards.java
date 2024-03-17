import java.util.Scanner;

public class StringToBackwards {
    public static void main(String[] args) {

        String myString;

        Scanner input = new Scanner(System.in);

        System.out.println("Entre com uma String para inverter:");
        myString = input.nextLine();

        new MyStringFunctions(myString).revertFunction();

    }
}