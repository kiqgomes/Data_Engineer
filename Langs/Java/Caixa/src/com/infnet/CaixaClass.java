package src.com.infnet;

public class CaixaClass {

    private double altura;
    private double largura;
    private double comprimento;

    public CaixaClass(double altura,double largura,double comprimento){
        this.altura = altura;
        this.largura = largura;
        this.comprimento = comprimento;
    };

    public void CalculaVolume() {
        double vol = this.altura * this.largura * this.comprimento;
        System.out.printf("Volume da Caixa: %.4f\n", vol);
    }

}