import java.util.Scanner;

public class tictactoecounting {
    static int xWins = 0;
    static int oWins = 0;

    public static void main ( final String[] args ) {
        final Scanner s = new Scanner( System.in );
        final char[][] board = new char[3][3];
        final String line = s.next();
        for ( int i = 0; i < board.length; i++ ) {
            for ( int j = 0; j < board.length; j++ ) {
                board[i][j] = line.charAt( i );
            }
        }

    }

    void solutions ( final char[][] board ) {
        for ( int i = 0; i < 3; i++ ) {
            if ( board[i][0] == 'X' && board[i][1] == 'X' && board[i][2] == 'X' ) {
                xWins++;

            }
        }
    }

}
