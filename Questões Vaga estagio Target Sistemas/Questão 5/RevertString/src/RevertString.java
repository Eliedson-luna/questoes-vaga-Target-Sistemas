import java.util.ArrayList;
import java.util.List;

public class RevertString {
    String stringToRevert;

    String revertedString = "";
    Character character;
    RevertString(String stringToRevert) {
        this.stringToRevert = stringToRevert;
    }

    public void myRevertFunction() {
        int maxLength = stringToRevert.length()-1;
        int counter = 0;
        while (counter!=maxLength) {
               character =  stringToRevert.charAt(maxLength);
               revertedString+=character;
               counter+=1;
               maxLength-=1;
               if (maxLength<0) {
                   break;
               }
        }
        System.out.println(revertedString);

    }
}
