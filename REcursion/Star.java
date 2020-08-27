import java.util.Scanner;

public class Star {
    static char[][] arr;
    static int rec = 0;
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        arr = new char[n][n];

        star(n);

        for(int i =0;i<n;i++){
            for(int k = 0;k<n;k++){
                System.out.print(arr[i][k]);
            }
            System.out.println("\n");
        }
    }
    public static void star(int n) {
        int blcokSize = n/3;
        for(int i =0;i<n;i++){
            for(int k = 0;k<n;k++){
               arr[i][k] = '*';
            }
        }        
        for(int b = 0;b<Math.pow(9,rec);b++)
        for(int i =blcokSize;i<blcokSize*2;i++){
            for(int k = blcokSize; k< blcokSize*2;k++){
                arr[i][k] = ' ';
            }
        }
        rec++;
        if(blcokSize != 1/3){
            star(n/3);
        }  
    }
    //실패
}