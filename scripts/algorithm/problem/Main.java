import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        String problemNumber = "";
        String path = System.getProperty("user.dir") + "\\scripts\\algorithm\\problem\\txt\\" + problemNumber + ".txt";
        BufferedReader br = new BufferedReader(new FileReader(path));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        // BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        // StringTokenizer st = new StringTokenizer(br.readLine());

    }
}
