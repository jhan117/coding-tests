import java.util.Scanner;

public class input {

    static void _1000(){
        // 1000.A+B
        Scanner sc = new Scanner(System.in);

        int fNum, sNum;
        fNum = sc.nextInt();
        sNum = sc.nextInt();

        System.out.println(fNum+sNum);
        
        sc.close();
    }

    public static void main(String[] args) {
        input._1000();
    }
    
}
