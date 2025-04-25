import java.util.Scanner;

public class blueberrywaffle {

    public static void main ( final String[] args ) {
        final Scanner s = new Scanner( System.in );

        final int rotateTime = s.nextInt();
        final int totalTime = s.nextInt();

        final int remainder = totalTime % rotateTime;
        final int ratio = totalTime / rotateTime;

        if ( remainder < ( rotateTime / 2 ) && ( ratio % 2 == 0 ) ) {
            System.out.println( "up" );
        }
        else if ( remainder < ( rotateTime / 2 ) && ( ratio % 2 != 0 ) ) {
            System.out.println( "down" );
        }
        else if ( remainder > ( rotateTime / 2 ) && ( ratio % 2 != 0 ) ) {
            System.out.println( "up" );
        }
        else {
            System.out.println( "down" );
        }

    }

}
