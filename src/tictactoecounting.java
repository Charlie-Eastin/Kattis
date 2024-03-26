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
                board[i][j] = line.charAt( i * board.length + j );
            }
        }
        solutions( board, 'O' );
        System.out.println( xWins + " " + oWins );
        s.close();

    }

    static void solutions ( final char[][] board, final char turn ) {
        if ( checkWins( board ) == true ) {
            return;
        }
        for ( int i = 0; i < board.length; i++ ) {
            for ( int j = 0; j < board.length; j++ ) {
                if ( board[i][j] == '.' ) {
                    if ( turn == 'X' ) {
                        board[i][j] = 'X';
                        solutions( board, 'O' );
                        board[i][j] = '.';
                    }
                    else if ( turn == 'O' ) {
                        board[i][j] = 'O';
                        solutions( board, 'X' );
                        board[i][j] = '.';
                    }

                }
            }
        }

    }

    static boolean checkWins ( final char[][] board ) {
        for ( int i = 0; i < 3; i++ ) {
            if ( board[i][0] == 'X' && board[i][1] == 'X' && board[i][2] == 'X' ) {
                xWins++;
                return true;
            }
            if ( board[0][i] == 'X' && board[1][i] == 'X' && board[2][i] == 'X' ) {
                xWins++;
                return true;
            }
            if ( board[i][0] == 'O' && board[i][1] == 'O' && board[i][2] == 'O' ) {
                oWins++;
                return true;
            }
            if ( board[0][i] == 'O' && board[1][i] == 'O' && board[2][i] == 'O' ) {
                oWins++;
                return true;
            }
        }
        if ( board[0][0] == 'X' && board[1][1] == 'X' && board[2][2] == 'X' ) {
            xWins++;
            return true;
        }
        if ( board[2][0] == 'X' && board[1][1] == 'X' && board[0][2] == 'X' ) {
            xWins++;
            return true;
        }
        if ( board[0][0] == 'O' && board[1][1] == 'O' && board[2][2] == 'O' ) {
            oWins++;
            return true;
        }
        if ( board[2][0] == 'O' && board[1][1] == 'O' && board[0][2] == 'O' ) {
            oWins++;
            return true;
        }
        return false;
    }

}
