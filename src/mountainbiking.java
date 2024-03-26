import java.util.Scanner;

public class mountainbiking {

    public static void main ( final String[] args ) {

        final Scanner s = new Scanner( System.in );

        final int n = s.nextInt();
        final int gravity = s.nextInt();

        final int[][] slopes = new int[n][2];

        for ( int i = 0; i < n; i++ ) {
            slopes[i][0] = s.nextInt();
            slopes[i][1] = s.nextInt();
        }

        velocity( 0, gravity, slopes, slopes.length - 1 );

    }

    static void velocity ( final float initialVelocity, final int gravity, final int[][] slopes, final int index ) {
        if ( index != -1 ) {
            final float acceleration = (float) Math.cos( Math.toRadians( slopes[index][1] ) ) * gravity;
            final float velocity = initialVelocity + ( 2 * acceleration * slopes[index][0] );
            velocity( velocity, gravity, slopes, index - 1 );
            System.out.println( Math.sqrt( velocity ) );
        }
    }

}
