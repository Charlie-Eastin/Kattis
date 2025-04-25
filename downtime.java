import java.util.Scanner;

public class downtime {

    public static void main ( final String[] args ) {
        final Scanner s = new Scanner( System.in );

        final int n = s.nextInt();
        final int requests = s.nextInt();
        final int[] arr = new int[n];

        int k = 0;
        while ( s.hasNextInt() ) {
            arr[k] = s.nextInt();
            k++;
        }
        int current = 0;
        int next = 0;
        int localCount = 0;
        int count = 1;
        int globalCount = 0;
        for ( int i = 0; i < n; i++ ) {
            current = arr[i];
            next = current;
            localCount = 0;
            int j = 0;
            for ( j = i; j < n; j++ ) {
                next = arr[j];
                if ( current + 1000 <= next ) {
                    break;
                }

                localCount++;
            }
            count = ( localCount + requests - 1 ) / requests;
            if ( count > globalCount ) {
                globalCount = count;
            }
        }
        System.out.println( globalCount );
    }
}
