import java.util.Scanner;

public class character {

    public static void main ( final String[] args ) {
        final Scanner s = new Scanner( System.in );

        final int characters = s.nextInt();

        int total = 0;

        total = (int) Math.pow( 2, characters );

        total -= 1;
        total -= characters;

        System.out.println( total );

    }

}
