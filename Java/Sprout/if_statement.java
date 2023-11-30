import java.util.Scanner;

public class if_statement {
    static void _1330(){
        // 1330.두 수 비교하기
        Scanner sc = new Scanner(System.in);

        int a, b;
        a = sc.nextInt();
        b = sc.nextInt();

        if (a < b) {
            System.out.println("<");
        } else if (a > b) {
            System.out.println(">");
        } else {
            System.out.println("==");
        }
    }

    public static void main(String[] args) {
        if_statement._1330();
    }
}
