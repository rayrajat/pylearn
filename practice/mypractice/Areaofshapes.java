import java.util.*;
public class Areaofshapes {
    @SuppressWarnings("ConvertToTryWithResources")
    public static void main(String args[]) {
        int l, b, h, r, side, ch;
        Scanner sc = new Scanner(System.in);

        System.out.println("Which area do you want?");
        System.out.println("1.Rectangle\n2.Circle\n3.Square\n4.Triangle");
        ch = sc.nextInt();

        switch (ch) {
            case 1 -> {
                Rectangle rect = new Rectangle();
                System.out.print("Enter length and breadth: ");
                l = sc.nextInt();
                b = sc.nextInt();
                System.out.println("Area of Rectangle: " + rect.area(l, b));
            }

            case 2 -> {
                Circle c = new Circle();
                System.out.print("Enter radius: ");
                r = sc.nextInt();
                System.out.println("Area of Circle: " + c.area(r));
            }

            case 3 -> {
                Square s = new Square();
                System.out.print("Enter side: ");
                side = sc.nextInt();
                System.out.println("Area of Square: " + s.area(side));
            }

            case 4 -> {
                Triangle t = new Triangle();
                System.out.print("Enter height and base: ");
                h = sc.nextInt();
                b = sc.nextInt();
                System.out.println("Area of Triangle: " + t.area(h, b));
            }

            default -> System.out.println("Invalid choice");
        }

        sc.close();
    }
}



class Rectangle {
    int area(int l, int b) {
        return l * b;
    }
}

class Circle {
    double area(int r) {
        return 3.14 * r * r;
    }
}

class Square {
    int area(int side) {
        return side * side;
    }
}

class Triangle {
    int area(int h, int b) {
        return (h * b) / 2;
    }
}
