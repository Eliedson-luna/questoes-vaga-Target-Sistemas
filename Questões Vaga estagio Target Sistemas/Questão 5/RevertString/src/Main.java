import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

        String myString;
        Scanner input = new Scanner(System.in);

        System.out.println("Entre com uma String para inverter:");
        myString = input.nextLine();

        var letsRevert = new RevertString(myString);

        letsRevert.myRevertFunction();




    }
}