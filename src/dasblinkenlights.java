import java.util.Scanner;

public class dasblinkenlights {

    public static void main ( final String[] args ) {
        final Scanner s = new Scanner( System.in );

        final int firstLight = s.nextInt();
        final int secondLight = s.nextInt();
        final int time = s.nextInt();
        s.close();
        boolean blink = false;

        for ( int i = 1; i <= time; i++ ) {
            if ( ( i % firstLight ) == 0 && ( i % secondLight ) == 0 ) {
                blink = true;
            }
        }

        if ( blink == true ) {
            System.out.println( "yes" );
        }
        else {
            System.out.println( "no" );
        }

    }

}
