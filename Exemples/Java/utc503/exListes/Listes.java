package utc503.exListes;
public class Listes {
    //Une constante
    static final int MAX=100;
    int taille;
    int[] contenu;

    //Création de liste : contructeur
    public Listes() {
        taille=0;
        contenu=new int[MAX];
    }
    public Listes(int max) {
        taille=0;
        contenu=new int[max];
    }
    //Ajouter
    public void ajouter(int e){
        contenu[taille++]=e;
    }
    //Afficher si taille=0 ceci ne fonctionne pas!
    public String toString(){
        StringBuffer s;
        s=new StringBuffer("[");
        for (int i=0;i<taille-2; i++) {
            s.append(contenu[i]+ ", ");
        }
        //i>=taille-2 cad taille-1 le dernier éleémtn de la liste
        s.append(contenu[taille-1]+"]");
        return s.toString();
    }
    public static void main(String args[]){
        Listes l = new Listes();
        l.ajouter(1);
        l.ajouter(10);
        l.ajouter(100);
        l.ajouter(10);
        l.ajouter(1);
        System.out.println(l);
    }
}