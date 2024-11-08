hashFunction(string s) {
    int hash = 0;
    for (int i = 0; i < s.length; i++) {
        hash += (i + 1) * (s[i] - 'a' + 1);
    }
    print(hash)
}



public class test {

    public static void main ( final String[] args ) {
        hashFunction("xwxx")
    }
}