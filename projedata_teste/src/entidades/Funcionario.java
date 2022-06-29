package entidades;
import java.util.*;
import java.io.Serializable;
import java.math.BigDecimal;
import java.text.DateFormat;
import java.text.DecimalFormat;
import java.text.DecimalFormatSymbols;
import java.text.NumberFormat;
import java.text.SimpleDateFormat;
import java.time.LocalDate;
import java.util.Date;

public class Funcionario extends Pessoa implements Serializable{

	private static  final long serialVersionUID = 1L;
	private int anoNascimento;
	private int anoAtual;
	private LocalDate dataAtual = LocalDate.now();
	private int idade;
	private double salarioMinimo;
	
	
	//private String nome;
	//private String data;
	private Double salario;
	private String funcao;
	
	public Funcionario(String nome, String data, Double salario, String funcao ) {
		super(nome, data);
	
		this.nome = nome;
		this.data = data;
		this.salario = salario;
		this.funcao = funcao;
		
	}

	public double getSalarioMinimo() {
		
		salarioMinimo = salario / 1212.00;
		
		
		return salarioMinimo;
		
	}
	
	
	
	public int getIdade() {
		
		anoNascimento = Integer.parseInt(data.substring(6,10)); 
		anoAtual = dataAtual.getYear();
		
		idade = anoAtual - anoNascimento;
		
		return idade;
		
		
	}
	
	
	public String getNome() {
		return nome;
	}


	public void setNome(String nome) {
		this.nome = nome;
	}

	
	public String data() {
		return data;
	}


	public void setData(String data) {
		this.data = data;
	}
	
	
	public String getFuncao() {
		return funcao;
	}


	public void setFuncao(String funcao) {
		this.funcao = funcao;
	}


	public Double getSalario() {
		return salario;
	}


	public void setSalario(Double salario) {
		this.salario = salario;
	}



	@Override
	public String toString() {
		   
		String salarioFormatado = NumberFormat.getCurrencyInstance().format(salario);
		
		salarioFormatado = salarioFormatado.replace('.',',');
		salarioFormatado = salarioFormatado.replaceFirst(",", ".");
		
		return "Funcionario [nome=" + nome + ", data=" + data + ", salario=R" + salarioFormatado + ", funcao=" + funcao + "]";
	}


	
	
	
	
	
 	/*
 	public String toString() {
        return "CsvFuncionario{nome='" + nome + "\', data=" + data + ", salario='" + salario + ", funcao='" + funcao + "\'}";
    }
 	*/
	
}
