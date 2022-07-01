package aplicacao;


import entidades.*;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Date;
import java.util.HashMap;
import java.math.BigDecimal;
import java.net.URI;
import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;
import java.io.Reader;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.text.DecimalFormat;
import java.text.NumberFormat;
import java.time.LocalDate;
import java.util.List;
import java.util.Locale;
import java.util.Map;
import java.util.Scanner;
import java.util.stream.Collectors;
import java.util.stream.Stream;

import com.opencsv.CSVReader;
import com.opencsv.CSVReaderBuilder;
import com.opencsv.bean.CsvToBean;
import com.opencsv.bean.CsvToBeanBuilder;


public class Programa {

	public static void main(String[] args) throws IOException  {
		// TODO Auto-generated method stub

		
		
		Scanner sc = new Scanner(System.in);
		System.out.println("Digite o caminho para o arquivo: ");
		String path = sc.nextLine();
		
		//String path = "F:\\programacao\\ws-java\\projedata_teste\\src\\funcionarios.csv";
		
		List<Funcionario> list = new ArrayList<Funcionario>();
		
		try (BufferedReader br = new BufferedReader(new FileReader(path))) {
		
			Locale.setDefault(Locale.US);
			
			String line = br.readLine();
			
			//pulo o cabeçalho
			line = br.readLine();
			
			while (line != null) {
				
				String[] vect = line.split(",");
				
				
				String nome = vect[0];
				String data = vect[1];
				Double salario = Double.parseDouble(vect[2]);
				String funcao = vect[3];
				
				//
				Funcionario xFunc = new Funcionario(nome,data,salario,funcao);
				list.add(xFunc);
				line = br.readLine();
				
			}
				
			System.out.println("\n ---------------Lista inicial ---------------- \n");
				
				for (Funcionario p : list) {
					
					System.out.println(p);
					
				}
				for (int i = 0; i < list.size(); i++) {
					if (list.get(i).getNome().equals("João")) {
						//Removendo o joão 
						list.remove(i);
					}
															
				}
				
				System.out.println("\n ---------------Lista sem o João! ---------------- \n ");
				
				for (Funcionario p : list) {
					System.out.println(p);
				}
				//instancio uma nova lista
				
				for (int i = 0; i < list.size(); i++) {
					
					double sal = list.get(i).getSalario();
							
					list.get(i).setSalario(sal+(sal*0.10));
					
					
				}
				
				
				
				System.out.println("\n ---------------Lista salarios atualizados ---------------- \n");
				
				for (Funcionario p : list) {
					System.out.println(p);
				}

				
				System.out.println("\n ---------------Funcionarios Agrupados por Função ---------------- \n");
				
				Map<String, String> mapFuncao = new HashMap<>();
				for (int i = 0; i < list.size(); i++) {
					
					//mapeio a funcao por linha
					
					String mapChave = list.get(i).getFuncao();
					String mapFuncionario = list.get(i).toString();
					
					//se primeiro registro ok, senao acumulo
					if (mapFuncao.get(mapChave) == null) {
						
						mapFuncao.put(mapChave,mapFuncionario);
						
					}
					else {
						mapFuncionario = mapFuncionario + " | " + list.get(i).toString();
						mapFuncao.put(mapChave,mapFuncionario);
						
					}
					
					
					
				}	
				
				//imprimindo o map
				
				
				
				for (String key : mapFuncao.keySet()) {
					
					System.out.println("Chave = " + key + ", Valor= " + mapFuncao.get(key));
					
					
				}
				
				
				//aniversariantes mes 10 e 12
				System.out.println("\n ---------------Lista aniversariantes mes 10 e 12  ---------------- \n ");
				
				
				for (int i = 0; i < list.size(); i++) {
					String mesFunc = list.get(i).data();
					if (mesFunc.substring(3,5).compareTo("10") == 0 || mesFunc.substring(3,5).compareTo("12") == 0) {
						System.out.println(list.get(i).toString());
					}
				}
				
				//funcionario mais velho
				System.out.println("\n ---------------O mais velho ---------------- \n ");
				
				
				
				int idadeAtual;
				int idadeAux = list.get(0).getIdade();
				
				for (int i = 0; i < list.size(); i++) {
					
					idadeAtual = list.get(i).getIdade();
					
					if (i != 0 && idadeAtual > idadeAux ) {
						
						idadeAux = idadeAtual;
						
						if (idadeAtual >= list.get(0).getIdade()) {
							
							System.out.println(list.get(i).toString() + " A sua idade é de : " +  Integer.toString(list.get(i).getIdade()) + " anos.");
						}
					
					}
					
					
					//ou seja,primeiro item e maior que o resto
					if (i == 0 && idadeAtual < idadeAux ) {
						
						idadeAux = list.get(1).getIdade();
						
					}
					
						
					
				//se o primeiro item for maior que o seugndo e nao entrou no for de cima
				if (list.get(0).getIdade() > list.get(1).getIdade()) {
					
					System.out.println(list.get(0).toString() + " A sua idade é de : " +  Integer.toString(list.get(0).getIdade()) + " anos.");	
					
				}
				
						
					
				}
				
				
				//lista em ordem alfabetica
				
				System.out.println("\n ---------------Lista em ordem alfabetica ---------------- \n ");
				
				Map<String, String> mapNome = new HashMap<>();
				for (int i = 0; i < list.size(); i++) {
					
					//mapeio a funcao por linha
					
					String mapChave = list.get(i).getNome();
					String mapFuncionario = list.get(i).toString();
					
					//se primeiro registro ok, senao acumulo
					if (mapNome.get(mapChave) == null) {
						
						mapNome.put(mapChave,mapFuncionario);
						
					}
					else {
						mapFuncionario = mapFuncionario + " | " + list.get(i).toString();
						mapNome.put(mapChave,mapFuncionario);
						
					}
					
					
					
				}	
				
				//
				//ordenando por ordem alfabetica de nome 
				//mapNome.forEach((k,v)->System.out.println(k+"="+v));
				//System.out.println("After Sorting by value");
				Stream<Map.Entry<String, String>> sorted =
					    mapNome.entrySet().stream()
					       .sorted(Map.Entry.comparingByValue());
				sorted.forEach(System.out::println);
				
				
				
				//total de salarios 
				
				System.out.println("\n ---------------Total de salarios ---------------- \n ");
				
				double salarioTotal = 0;
				
				
				for (int i = 0; i < list.size(); i++) {
				
					salarioTotal = salarioTotal + list.get(i).getSalario();
					
				}
				
				
				
				String salarioTotalFormatado = NumberFormat.getCurrencyInstance().format(salarioTotal);
				salarioTotalFormatado = salarioTotalFormatado.replace('.',',');
				salarioTotalFormatado = salarioTotalFormatado.replaceFirst(",", ".");
								
				//System.out.println("Total de salario: R$ " + df.format(salarioTotal) + ".");
				System.out.println("Total de salario: R" + salarioTotalFormatado + ".");
			
				// total de salario minimo por funcionario 
				
				
				
				System.out.println("\n ---------------Total de salarios minimos por funcionario ---------------- \n ");
				
				for (int i = 0; i < list.size(); i++) {
					
					
					System.out.println(list.get(i).toString() + " Quantidade de salarios minimos: " + Double.toString(list.get(i).getSalarioMinimo()));
					
					
				}
				
				
				
				
		}
		catch (IOException e) {
			
			System.out.println("Error: " + e.getMessage());
			
		}
				
		
		
		
		
		
		
		
			
	}

}
