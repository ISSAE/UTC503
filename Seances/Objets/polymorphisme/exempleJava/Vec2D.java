package exempleJava;

public class Vec2D extends Vecteur {
    public Vec2D(double x, double y) {
        super(x,y);
    }


    @Override
    public String toString() {
        return String.format("<<Vec2D (%.2f,%.2f)>>", getVec(0), getVec(1));
    }

    
    public static void main(String ...args) {
        var v1 = new Vec2D(10.0,20.0);
        System.out.println(v1);

        var lv = new Vecteur[4];

        lv[0] = new Vecteur(1,2,3,4,5);
        lv[1] = new Vec2D(10,20);

        lv[1].add(lv[0]);
        System.out.println(lv[1]);
        lv[0].add(lv[1]);
        System.out.println(lv[0]);
    }
}
