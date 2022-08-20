package com.infnet.pessoa;

public class App {
    public static void main(String[] args) throws Exception {
        Person Person = new Person();
        PersonF PersonF = new PersonF(); 
        Person.setName("Kaique");
        Person.setIdade(19);
        System.out.println(Person.createEmail("Claudio", 19));
        System.out.println(PersonF.createEmail(Person.getName(), Person.getIdade()));

    }
}
