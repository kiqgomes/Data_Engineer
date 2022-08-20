package com.infnet.pessoa;

public class Person {
    private  String name;
    private int idade;

    public Person() {};

    public Person(String name,int CPF,int idade) {
    this.name = name;
    this.idade = idade;
    }

    public String createEmail(String name, int idade) {
        String email = name+ "@" + idade;
        return email;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
 
    public int getIdade() {
        return idade;
    }

    public void setIdade(int idade) {
        this.idade = idade;
    }

    @Override
    public String toString() {
        return "Pessoa [Idade=" + idade + ", name=" + name + "]";
    }
}
