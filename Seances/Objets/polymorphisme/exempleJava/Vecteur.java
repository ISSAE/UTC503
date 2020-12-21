package exempleJava;

public class Vecteur {

    /** Les attributs doivent être privé encapsulation */
    // Element du vecteur
    private double[] _vec;

    /** Le ou les constructeurs */
    // n dimension du vecteur
    public Vecteur(int n) {
        _vec = new double[n];
    }

    // La surcharge d’une méthode ou d’un constructeur permet de définir plusieurs
    // fois une même méthode/constructeur avec des arguments différents.
    // Le compilateur choisit la méthode qui doit être appelée en fonction du nombre
    // et du type des arguments .

    public Vecteur(double ...termes) {
        _vec = termes;
    }

    /** LES ACCESSEURS (mutateurs) getters/setters */
    // ! ceci pourrait poser un problème _vec est une référence vers termes
    public void setVec(double[] termes) {
        _vec = termes;
    }

    public double[] getVec() {
        return _vec;
    }

    public void setVec(double terme, int i) {
        _vec[i] = terme;
    }

    public double getVec(int i) {
        return _vec[i];
    }

    /** Les opérations */

    // Ajoute autre au vecteur courant
    // Translation (vec1 + vec2)
    public void add(Vecteur autre) {
        // TODO: faut vérifier que les 2 vecteurs on la même dimension
        for (int i = 0; i < _vec.length; i++) {
            _vec[i] += autre._vec[i]; // vec[i] = vec[i] + autre.vec[i]
        }
    }

    //produit scalaire vec1 * vec2
    public double mult(Vecteur autre) {
        // TODO: faut vérifier que les 2 vecteurs on la même dimension
        int s=0;
        for (int i = 0; i < _vec.length; i++) {
             s += _vec[i] * autre._vec[i]; // vec[i] = vec[i] + autre.vec[i]
        }
        return s;
    }

    // produit avec un scalaire l * vec
    public void mult(double l) {
        for (int i = 0; i < _vec.length; i++) {
            _vec[i] *= l; // vec[i] = l * vec[i]
        }
    }

    public String toString() {
        int n = _vec.length;
        String s = "<<Vec: (";
        for (int i = 0; i < n - 1; i++) {
            s += _vec[i] + ",";
        }
        s += _vec[n - 1] + ") >>";
        return s;
    }

    // pour tester
    public static void main(String args[]) {
        double[] t = new double[] { 1.0, 2.0, 3.0, 4.0, 5.0 };
        double[] t2 = new double[] { 10.0, 20.0, 30.0, 40.0, 50.0 };
        var v1 = new Vecteur(t);
        var v2 = new Vecteur(t2);
        var v3 = new Vecteur(11,22,33,44);
        System.out.printf("\n\tv1=%s v2=%s v3=%s\n", v1, v2, v3);
        v1.add(v2);
        System.out.printf("\nTranslation\tv1=%s v2=%s\n", v1, v2);
        v1.mult(10);
        System.out.printf("\nHomothétie\tv1=%s v2=%s\n", v1, v2);
        System.out.println(t[0]);

    }
}