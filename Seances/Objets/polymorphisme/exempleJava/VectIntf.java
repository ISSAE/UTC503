package exempleJava;

/**
 * Interface publique des vecteurs
 * addition de vecteur v1+v2
 * multiplication par un scalaire l*v
 * produire scalaire v1*v2
 * Le contrat
 */
public interface VectIntf {
    public void   add(VectIntf autre);
    public void   mult(double l);
    public double mult(VectIntf autre);
}
