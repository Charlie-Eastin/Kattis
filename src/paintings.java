import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class paintings {

    public static void main ( final String[] args ) {
        final Scanner s = new Scanner( System.in );
        final int testCases = s.nextInt();
        final List<String> colors = new ArrayList<String>();
        final List<List<String>> badColors = new ArrayList<List<String>>();
        final List<List<String>> paintings = new ArrayList<List<String>>();
        final List<String> currentPainting = new ArrayList<String>();

        for ( int i = 0; i < testCases; i++ ) {
            int size = s.nextInt();
            for ( int j = 0; j < size; j++ ) {
                colors.add( s.next() );
            }
            size = s.nextInt();
            for ( int j = 0; j < size; j++ ) {
                final List<String> currentBadColor = new ArrayList<String>();
                currentBadColor.add( s.next() );
                currentBadColor.add( s.next() );
                badColors.add( currentBadColor );
            }
            paint( colors, badColors, 0, paintings, currentPainting );
            for ( int j = 0; j < paintings.size(); j++ ) {
                for ( int k = 0; k < paintings.get( j ).size(); k++ ) {
                    System.out.println( paintings.get( j ).get( k ) + " " );
                }
                System.out.print( "\n\n" );
            }
        }

    }

    static void paint ( final List<String> colors, final List<List<String>> badColors, final int index,
            final List<List<String>> paintings, final List<String> currentPainting ) {
        if ( index == colors.size() ) {
            paintings.add( currentPainting );
        }
        for ( int i = 0; i < colors.size(); i++ ) {
            if ( i == index ) {
                continue;
            }
            if ( currentPainting.size() == 0 ) {
                currentPainting.add( colors.get( i ) );
            }
            else {
                boolean valid = true;
                for ( int j = 0; j < badColors.size(); j++ ) {
                    if ( currentPainting.get( i - 1 ).equals( badColors.get( j ).get( 0 ) )
                            && currentPainting.get( i ).equals( badColors.get( j ).get( 1 ) ) ) {
                        valid = false;
                        break;
                    }
                    else if ( currentPainting.get( i ).equals( badColors.get( j ).get( 0 ) )
                            && currentPainting.get( i - 1 ).equals( badColors.get( j ).get( 1 ) ) ) {
                        valid = false;
                        break;
                    }
                }
                if ( valid == true ) {
                    currentPainting.add( colors.get( i ) );
                    paint( colors, badColors, index + 1, paintings, currentPainting );
                }
            }
        }
    }

}
