package com.infnet.pessoa;


public class PersonF extends Person {
    private int CPF;

    public PersonF(){};

    public PersonF(int CPF){
        this.CPF = CPF;
    }

    @Override
    public String createEmail(String name, int idade) {
        String email = name+ "@" + idade + ".gmail.com";
        return email;
    }
    
    public int getCPF() {
        return CPF;
    }

    public void setCPF(int cPF) {
        CPF = cPF;
    }

    @Override
    public String toString() {
        return "PersonF [CPF=" + CPF + "]";
    };

}
