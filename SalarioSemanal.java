public class SalarioSemanal {
    public static void main(String[] args) {
        double horasTrabajadas = 40; // Ejemplo de horas trabajadas
        double tarifaPorHora = 15; // Ejemplo de tarifa por hora

        double salarioSemanal = calcularSalarioSemanal(horasTrabajadas, tarifaPorHora);
        System.out.println("El salario semanal es: " + salarioSemanal);
    }

    public static double calcularSalarioSemanal(double horas, double tarifa) {
        return horas * tarifa;
    }
}





