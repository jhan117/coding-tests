import java.util.Scanner;

public class input {

    static void _1000(){
        // 1000.A+B
        Scanner sc = new Scanner(System.in);

        int fNum, sNum;
        fNum = sc.nextInt();
        sNum = sc.nextInt();

        System.out.println(fNum+sNum);
    }

    static void _1001(){
        // 1001.A-B
        Scanner sc = new Scanner(System.in);

        int fNum, sNum;
        fNum = sc.nextInt();
        sNum = sc.nextInt();

        System.out.println(fNum-sNum);
    }

    static void _10998(){
        // 10998.AxB
        Scanner sc = new Scanner(System.in);

        int fNum, sNum;
        fNum = sc.nextInt();
        sNum = sc.nextInt();

        System.out.println(fNum*sNum);
    }

    static void _10869(){
        // 10869.사칙연산
        Scanner sc = new Scanner(System.in);

        int fNum, sNum;
        fNum = sc.nextInt();
        sNum = sc.nextInt();

        System.out.println(fNum+sNum);
        System.out.println(fNum-sNum);
        System.out.println(fNum*sNum);
        System.out.println(fNum/sNum);
        System.out.println(fNum%sNum);
    }

    static void _1008(){
        // 1008.A/B
        Scanner sc = new Scanner(System.in);

        double fNum, sNum;
        fNum = sc.nextDouble();
        sNum = sc.nextDouble();

        System.out.println(fNum/sNum);
    }

    static void _11382(){
        // 11382.꼬마 정민
        Scanner sc = new Scanner(System.in);

        long fNum, sNum, tNum;
        fNum = sc.nextLong();
        sNum = sc.nextLong();
        tNum = sc.nextLong();

        System.out.println(fNum+sNum+tNum);
    }

    public static void main(String[] args) {
        input._1000();
        input._1001();
        input._10998();
        input._10869();
        input._1008();
        input._11382();
    }
    
}
