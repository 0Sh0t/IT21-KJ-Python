//Harjutus 2

public class JavaH2 {
    
    public static void main(String[] args){
        double meter;
        int inch = 1;
    
        meter = inch/39.37;
    
        for(int i = 0;i <= 12 ; i++){
            for(inch =0;inch<=144;inch++){
            meter = inch/39.37;
            System.out.println(inch + "  inch =  " + meter + "  meters");
            }
            if(i==12)
                System.out.println();
                //i = 0;
        }
    }
}