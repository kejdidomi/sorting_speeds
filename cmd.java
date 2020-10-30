import java.util.Random;
import java.util.Arrays;
public class cmd {
   public static void main(String[] args) {
      Random rd = new Random(); // creating Random object
      int[] arr = new int[Integer.parseInt(args[0])];
      for (int i = 0; i < arr.length; i++) {
         arr[i] = rd.nextInt(); // storing random integers in an array
         
      }
      long startTime = System.nanoTime();
      Arrays.sort(arr);
      long elapsedTime = System.nanoTime() - startTime;
      System.out.println((float)elapsedTime/1000000000);
   }
}