import java.util.Scanner;

public class almostperfect {

    public static void main ( final String[] args ) {
        final Scanner s = new Scanner( System.in );
        while ( s.hasNextInt() == true ) {
            final int num = s.nextInt();
            int total = 0;
            for ( int i = 0; i < num; i++ ) {
                if ( num % i == 0 ) {
                    total = i + total;
                }
            }
            if ( total == num ) {
                System.out.println( num + " perfect" );
            }
            else if ( Math.abs( total - num ) <= 2 ) {
                System.out.println( num + " almost perfect" );
            }
            else {
                System.out.println( num + " not perfect" );
            }

        }

    }

}
