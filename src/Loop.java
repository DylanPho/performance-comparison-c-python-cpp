public class Loop {
    public static double performLoop(int iterations, double seed) {
        double result = seed;
        for (int i = 0; i < iterations; i++) {
            result += 1;
        }
        return result;
    }

    public static void main(String[] args) {
        if (args.length < 2) {
            System.out.println("Usage: java Loop <iterations> <seed>");
            return;
        }

        int iterations = Integer.parseInt(args[0]);
        double seed = Double.parseDouble(args[1]);

        double result = performLoop(iterations, seed);
        System.out.println(result);
    }
}