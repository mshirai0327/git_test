import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
      System.out.println("Hello World.");

      Scanner stdin=new Scanner(System.in);
      System.out.print("how many * will you display on the screen?");
      int n=stdin.nextInt();

      int i=0;
      while(i<n){
        System.out.print('*');
        i++;
      }
      System.out.println();
    }
}