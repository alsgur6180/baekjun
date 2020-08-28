import java.util.Scanner;

public class Alram {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int h = scanner.nextInt();
        int m = scanner.nextInt();
        if(m<45 && h>0){
            m = m+60 -45;
            h = h-1;
        }
        else if (m< 45&&h==0) {
            m = m+60 -45;
            h = 23;
        }
        else{
            m = m-45;
        }
        System.out.println(h + " " + m);
        scanner.close();
    }
    
}