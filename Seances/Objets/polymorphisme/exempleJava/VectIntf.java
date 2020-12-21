package exempleJava;

/**
 * Interface poublique des vercteurs
 * addition de vecteur v1+v2
 * multiplication par un scalaire l*v
 * produire scalaire v1*v2
 */
public interface VectIntf {
    public void   add(VectIntf autre);
    public double mult(VectIntf autre);
    public void   mult(double l);
}
