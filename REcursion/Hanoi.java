import java.util.ArrayList;
import java.util.Scanner;

public class Hanoi {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int plate = sc.nextInt();
        int count = 0;
        ArrayList<Integer> top1 = new ArrayList<Integer>();
        ArrayList<Integer> top2 = new ArrayList<Integer>();
        ArrayList<Integer> top3 = new ArrayList<Integer>();
        
        for(int i =plate;i>0;i--){
            top1.add(i);
        }
        hanoi(plate);
    
    }
    public static void hanoi(int plate) {
        
        
    }
}