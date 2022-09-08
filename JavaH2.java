import java.util.Scanner;

//1. Teisendab tollid meetriteks
public class JavaH2 {

    public static void main(String[] args) {
    teisendamine();
    ellips();
    aeg();
    sportlane();
    }

    public static void teisendamine(){
        double meeter;
        int toll = 1;
        meeter = toll/39.37;
        System.out.println(toll + " tolli = " + meeter + " meetrit");

    }

    //2. Leiab ellipsi pindala
    public static void ellips(){


    }

    //3. Teisendab minutid tundideks
    public static void aeg(){
        double tund;
        int minut = 60;
        tund = minut/60;
        System.out.println(minut + " minutit = " + tund + " tundi");
    }
    
    //4. Leiab sportlase kiiruse
    public static void sportlane(){
        Scanner in = new Scanner(System.in);
        System.out.print("Sisesta aeg: ");
        int aeg = in.nextInt();
        System.out.print("Sisesta distants: ");
        int distants = in.nextInt();
        float kiirus = (float)distants / aeg;
        System.out.println("Kiirus on: " + kiirus);
    }
    
}
