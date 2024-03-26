import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class perket {

    public static void main ( final String[] args ) {
        final Scanner s = new Scanner( System.in );
        final int size = s.nextInt();

        final List<Integer> sour = new ArrayList<Integer>();
        final List<Integer> bitter = new ArrayList<Integer>();
        final List<Integer> diffList = new ArrayList<Integer>();

        for ( int i = 0; i < size; i++ ) {
            sour.add( s.nextInt() );
            bitter.add( s.nextInt() );
        }
        mix( sour, bitter, 1, 0, 0, diffList );
        int min = Integer.MAX_VALUE;
        for ( int i = 0; i < diffList.size(); i++ ) {
            if ( diffList.get( i ) < min ) {
                min = diffList.get( i );
            }
        }
        System.out.println( min );
    }

    static void mix ( final List<Integer> sour, final List<Integer> bitter, final int currentSour,
            final int currentBitter, final int index, final List<Integer> diffList ) {

        for ( int i = index; i < sour.size(); i++ ) {
            mix( sour, bitter, currentSour * sour.get( i ), currentBitter + bitter.get( i ), i + 1, diffList );
            final int diff = Math.abs( currentSour * sour.get( i ) - ( currentBitter + bitter.get( i ) ) );
            // System.out.println("min:" + diff + " index: " + i);
            // System.out.println( "Sour: " + (currentSour * sour.get( i )) + "
            // bitter: " + (currentBitter + bitter.get( i )) );
            diffList.add( diff );
        }
    }

}
