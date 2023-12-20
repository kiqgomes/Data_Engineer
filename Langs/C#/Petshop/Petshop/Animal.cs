using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

class Animal
{
    public string name;
    public int age;
    public bool alive;
    public string dadName;


    override
    public string ToString() { return $"My name is {name}\nI'm {age} years age\nMy dad name is {dadName}\n{(!alive ? "I'm on the sky!": "I'm with my human family :)")}"; }

}

