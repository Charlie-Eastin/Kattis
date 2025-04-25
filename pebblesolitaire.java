import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

public class pebblesolitaire {

    private static Map<String, Integer> cache = new HashMap<>();

    public static void main ( final String[] args ) {
        final Scanner s = new Scanner( System.in );

        final int limit = s.nextInt();
        for ( int i = 0; i < limit; i++ ) {
            int count = 0;
            final String line = s.next();
            final char[] arr = new char[23];
            for ( int j = 0; j < arr.length; j++ ) {
                arr[j] = line.charAt( j );
                if ( arr[j] == 'o' ) {
                    count++;
                }
            }
            final int solution = solve( new String( arr ), count );
            System.out.println( solution );
        }

        s.close();
    }

    static int solve ( final String state, final int count ) {
        // Check cache
        if ( cache.containsKey( state ) ) {
            return cache.get( state );
        }

        int min = count;
        final char[] arr = state.toCharArray();

        for ( int i = 0; i < arr.length - 1; i++ ) {
            if ( arr[i] == 'o' && arr[i + 1] == 'o' ) {
                if ( i != 0 && arr[i - 1] != 'o' ) {
                    arr[i - 1] = 'o';
                    arr[i] = '-';
                    arr[i + 1] = '-';
                    final int tempMin = solve( new String( arr ), count - 1 );
                    arr[i - 1] = '-';
                    arr[i] = 'o';
                    arr[i + 1] = 'o';
                    if ( min > tempMin ) {
                        min = tempMin;
                    }
                }
                if ( i != arr.length - 2 && arr[i + 2] != 'o' ) {
                    arr[i + 2] = 'o';
                    arr[i + 1] = '-';
                    arr[i] = '-';
                    final int tempMin = solve( new String( arr ), count - 1 );
                    arr[i + 2] = '-';
                    arr[i + 1] = 'o';
                    arr[i] = 'o';
                    if ( min > tempMin ) {
                        min = tempMin;
                    }
                }
            }
        }

        // Cache the result before returning
        cache.put( state, min );
        return min;
    }
}
