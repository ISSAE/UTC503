package exempleJava;

public class Vec2D extends Vecteur {
    public Vec2D(double x, double y) {
        super(x,y);
    }

    
    public static void main(String ...args) {
        var v1 = new Vec2D(10.0,20.0);
        System.out.println(v1);
    }

    @Override
    public String toString() {
        return String.format("<<Vec2D (%.2f,%.2f)>>", getVec(0), getVec(1));
    }
}
