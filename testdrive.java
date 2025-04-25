import java.util.Scanner;

public class testdrive {

    public static void main ( final String[] args ) {
        final Scanner s = new Scanner( System.in );

        final int a = s.nextInt();
        final int b = s.nextInt();
        final int c = s.nextInt();

        if ( c - b == b - a ) {
            System.out.println( "cruised" );
        }
        else if ( ( b > a && b > c ) || ( c > b && a > b ) ) {
            System.out.println( "turned" );
        }
        else if ( Math.abs( a - b ) < Math.abs( b - c ) ) {
            System.out.println( "accelerated" );
        }
        else if ( Math.abs( c - b ) < Math.abs( b - a ) ) {
            System.out.println( "braked" );
        }
        else {
            System.out.println( "Uknown" );
        }

    }

}
