import java.util.Scanner;

public class bestcompression {

    public static void main ( final String[] args ) {
        final Scanner s = new Scanner( System.in );

        final int files = s.nextInt();

        final int bits = s.nextInt();

        if ( files <= ( files << ( bits + 1 ) ) - 1 ) {
            System.out.println( "yes" );
        }
        else {
            System.out.println( "no" );
        }

    }

}
