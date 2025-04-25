import java.util.LinkedList;
import java.util.List;
import java.util.Scanner;

public class gold {

    public static void main ( final String[] args ) {
        final Scanner s = new Scanner( System.in );
        final List<LinkedList<String>> maze = new LinkedList<LinkedList<String>>();
        LinkedList<String> row;
        final int x = s.nextInt();
        final int y = s.nextInt();
        s.nextLine();
        while ( s.hasNextLine() ) {
            final String line = s.nextLine();
            row = new LinkedList<String>();
            for ( int i = 0; i < line.length(); i++ ) {
                row.add( "" + line.charAt( i ) );
            }
            maze.add( row );
        }
        for ( int i = 0; i < maze.size(); i++ ) {
            for ( int j = 0; j < maze.get( 0 ).size(); j++ ) {
                System.out.print( maze.get( i ).get( j ) + "," );
            }
            System.out.print( "\n" );
        }

        int startingX = 0;
        int startingY = 0;
        for ( int i = 0; i < maze.size(); i++ ) {
            for ( int j = 0; j < maze.get( 0 ).size(); j++ ) {
                if ( maze.get( i ).get( j ).equals( "P" ) ) {
                    startingX = i;
                    startingY = j;
                }
            }
        }

        System.out.println( startingX + "," + startingY );
        final int gold = DFS( startingX, startingY, maze, 0 );
        System.out.println( gold );

    }

    static int DFS ( final int startingX, final int startingY, final List<LinkedList<String>> maze, final int gold ) {
        if ( isValid( startingX, startingY - 1, maze ) ) {
            if ( maze.get( startingX ).get( startingY - 1 ).equals( "G" ) ) {
                return DFS( startingX, startingY - 1, maze, gold + 1 );
            }
            else {
                return DFS( startingX, startingY - 1, maze, gold );
            }
        }
        if ( isValid( startingX, startingY + 1, maze ) ) {
            if ( maze.get( startingX ).get( startingY + 1 ).equals( "G" ) ) {
                return DFS( startingX, startingY + 1, maze, gold + 1 );
            }
            else {
                return DFS( startingX, startingY + 1, maze, gold );
            }
        }
        if ( isValid( startingX - 1, startingY, maze ) ) {
            if ( maze.get( startingX - 1 ).get( startingY ).equals( "G" ) ) {
                return DFS( startingX - 1, startingY, maze, gold + 1 );
            }
            else {
                return DFS( startingX - 1, startingY, maze, gold );
            }
        }
        if ( isValid( startingX + 1, startingY, maze ) ) {
            if ( maze.get( startingX + 1 ).get( startingY ).equals( "G" ) ) {
                return DFS( startingX + 1, startingY, maze, gold + 1 );
            }
            else {
                return DFS( startingX + 1, startingY, maze, gold );
            }
        }
        return gold;
    }

    static boolean isValid ( final int startingX, final int startingY, final List<LinkedList<String>> maze ) {
        if ( maze.get( startingX ).get( startingY ).equals( "#" )
                || maze.get( startingX ).get( startingY ).equals( "T" ) ) {
            return false;
        }
        else {
            return true;
        }
    }

}
