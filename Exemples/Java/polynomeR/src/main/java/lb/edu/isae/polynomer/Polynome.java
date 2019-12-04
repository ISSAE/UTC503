package lb.edu.isae.polynomer;

import java.util.ArrayList;
import java.util.Arrays;

/**
 * @author Pascal Fares
 */
public class Polynome {
    ArrayList<Integer> coef;
    
    Polynome(Integer[] coef) {
        this.coef=new ArrayList<>(Arrays.asList(coef));
    }
    
    /**
     * coef = a_0 ... a_i ... a_n
     * P_coef(x)=a_0 + a_1 x^1 + ... + a_i x^i + ... a_n x^n
     *     = a_0 + x(a_1 + a_2 x^1 + .... + a_n x^(n-1)
     *     = prem(coef) + x*(P_reste(coef)(x)
     * @param coef
     * @param x
     * @return 
     */
    private int _P(ArrayList<Integer> coef, int x) {
        if (coef.isEmpty()) return 0;
        else {
            return coef.get(0)+ 
                    x *_P(new ArrayList<>(coef.subList(1, coef.size())),x);
        }
    }
    public int P(int x) {
        return _P(coef,x);
    } 
    public static void main(String args[]) {
        Integer[] c={1,1,1};
        System.out.println((new Polynome(c)).P(1));
    }   
}