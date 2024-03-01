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

    static void _9498(){
        // 9498.시험 성적
        Scanner sc = new Scanner(System.in);

        int num = sc.nextInt();

        if (num >= 90) {
            System.out.println("A");
        } else if (num >= 80){
            System.out.println("B");
        } else if (num >= 70) {
            System.out.println("C");
        } else if (num >= 60){
            System.out.println("D");
        } else {
            System.out.println("F");
        }
    }

    static void _14681(){
        // 14681.사분면 고르기
        Scanner sc = new Scanner(System.in);
        
        int x, y;
        x = sc.nextInt();
        y = sc.nextInt();
        
        if (y > 0) {
            System.out.println((x > 0) ?  1 : 2);
        } else if (y < 0) {
            System.out.println((x > 0) ?  4 : 3);
        }
    }

    static void _2753(){
        // 2753.윤년
        Scanner sc = new Scanner(System.in);

        int year = sc.nextInt();

        if ((year % 4 == 0 && year % 100 != 0) || year % 400 == 0){
            System.out.println(1);
        } else {
            System.out.println(0);
        }
    }

    static void _2420() {
        // 2420. 사파리월드
        Scanner sc = new Scanner(System.in);

        long a, b;
        a = sc.nextInt();
        b = sc.nextInt();

        long num = (a - b);
        if (num < 0){
            System.out.println(-num);
        } else {
            System.out.println(num);
        }
    }

    public static void main(String[] args) {
        if_statement._1330();
        if_statement._9498();
        if_statement._14681();
        if_statement._2753();
        if_statement._2420();
    }
}
