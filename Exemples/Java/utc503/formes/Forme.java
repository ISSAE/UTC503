/**
 * Forme inerface pour les formes géométrique
 * Application de l'encapsulation
 * Et permettre le polumorphisme 
 */
public interface Formes {
    public int perimetre();
    public float surface();
    public void translation(int x, int y);
    public void homothecie(int lx, int ly);
}