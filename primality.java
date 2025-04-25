import java.util.Scanner;

public class primality {

    public static void main ( final String[] args ) {
        final Scanner s = new Scanner( System.in );

        final long prime = s.nextLong();

        final long primeCount = (long) Math.sqrt( prime );
        boolean found = false;
        if ( prime <= 1 ) {
            System.out.println( "NO" );

        }
        else if ( prime == 2 || prime == 3 ) {
            System.out.println( "YES" );
        }
        else if ( prime % 2 == 0 || prime % 3 == 0 ) {
            found = true;
            System.out.println( "NO" );
        }
        else {
            for ( int i = 5; i <= primeCount; i += 6 ) {
                if ( prime % i == 0 || prime % ( i + 2 ) == 0 ) {
                    System.out.println( "NO" );
                    found = true;
                    break;
                }
            }
            if ( found == false ) {
                System.out.println( "YES" );
            }
        }

    }

}
