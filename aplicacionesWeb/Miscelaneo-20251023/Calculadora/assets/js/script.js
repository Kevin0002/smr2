let n1 = "";
let n2 = "";
let primero = true;
let oprcn = 0;

// Función que ajusta el contenido a la ventana
function ajustarBotones(){
    if(window.innerWidth < 938){
        // Entraría aquí en el caso de que la ventana fuese menor de 938 px
        document.getElementById("botones").innerHTML = 
                    "<button class='boton' id='limpiar' onclick=\"limpiarPantalla()\">C</button>" +
                    "<button class=\"boton\" id=\"raiz\" onclick=\"operacion(5)\">√</button>" +
                    "<button class=\"boton\" id=\"porcentaje\" onclick=\"operacion(6)\">%</button>" +
                    "<button class=\"boton\" id=\"resta\" onclick=\"operacion(2)\">-</button>" +
                    "<button class=\"boton\" id=\"multi\" onclick=\"operacion(3)\">x</button>" +
                    "<button class=\"boton\" id=\"division\" onclick=\"operacion(4)\">/</button>" +
                    "<button class=\"boton\" onclick=\"recogidaDatos('7')\">7</button>" +
                    "<button class=\"boton\" onclick=\"recogidaDatos('8')\">8</button>" +
                    "<button class=\"boton\" onclick=\"recogidaDatos('9')\">9</button>" +
                    "<button class=\"boton\" onclick=\"recogidaDatos('4')\">4</button>" +
                    "<button class=\"boton\" onclick=\"recogidaDatos('5')\">5</button>" +
                    "<button class=\"boton\" onclick=\"recogidaDatos('6')\">6</button>" +
                    "<button class=\"boton\" onclick=\"recogidaDatos('1')\">1</button>" +
                    "<button class=\"boton\" onclick=\"recogidaDatos('2')\">2</button>" +
                    "<button class=\"boton\" onclick=\"recogidaDatos('3')\">3</button>" +
                    "<button class=\"boton\" onclick=\"recogidaDatos('.')\">.</button>" +
                    "<button class=\"boton\" onclick=\"recogidaDatos('0')\">0</button>" +
                    "<button class=\"boton\" id=\"suma\" onclick=\"operacion(1)\">+</button>" +
                    "<button class=\"boton\" id=\"igual\" onclick=\"resultado()\">=</button>";

        var calcu = document.getElementById("calculadora");
        calcu.style.width = "70%";
        
        var igual = document.getElementById("igual");
        igual.style.width = "60%";

        var boton = document.getElementsByClassName("boton");
        for(let i = 0 ; i < boton.length - 1 ; i++){
            boton[i].style.width = "30%";
            boton[i].style.height = "6vh";
            
        }
        
    }else{
        // Aquí en el caso contrario
        document.getElementById("botones").innerHTML = 
                    "<button class='boton' id='limpiar' onclick=\"limpiarPantalla()\">C</button>" +
                    "<button class=\"boton\" id=\"raiz\" onclick=\"operacion(5)\">√</button>" +
                    "<button class=\"boton\" id=\"porcentaje\" onclick=\"operacion(6)\">%</button>" +
                    "<button class=\"boton\" id=\"suma\" onclick=\"operacion(1)\">+</button>" +
                    "<button class=\"boton\" onclick=\"recogidaDatos('7')\">7</button>" +
                    "<button class=\"boton\" onclick=\"recogidaDatos('8')\">8</button>" +
                    "<button class=\"boton\" onclick=\"recogidaDatos('9')\">9</button>" +
                    "<button class=\"boton\" id=\"resta\" onclick=\"operacion(2)\">-</button>" +
                    "<button class=\"boton\" onclick=\"recogidaDatos('4')\">4</button>" +
                    "<button class=\"boton\" onclick=\"recogidaDatos('5')\">5</button>" +
                    "<button class=\"boton\" onclick=\"recogidaDatos('6')\">6</button>" +
                    "<button class=\"boton\" id=\"multi\" onclick=\"operacion(3)\">x</button>" +
                    "<button class=\"boton\" onclick=\"recogidaDatos('1')\">1</button>" +
                    "<button class=\"boton\" onclick=\"recogidaDatos('2')\">2</button>" +
                    "<button class=\"boton\" onclick=\"recogidaDatos('3')\">3</button>" +
                    "<button class=\"boton\" id=\"division\" onclick=\"operacion(4)\">/</button>" +
                    "<button class=\"boton\" onclick=\"recogidaDatos('.')\">.</button>" +
                    "<button class=\"boton\" onclick=\"recogidaDatos('0')\">0</button>" +
                    "<button class=\"boton\" id=\"igual\" onclick=\"resultado()\">=</button>";

        var calcu = document.getElementById("calculadora");
        calcu.style.width = "45%";
        
        var igual = document.getElementById("igual");
        igual.style.setProperty("width", "49%", "important")

        var boton = document.getElementsByClassName("boton");
        for(let i = 0 ; i < boton.length - 1 ; i++){
            boton[i].style.width = "24%";
            boton[i].style.height = "5vh";
        }
    }
}

window.addEventListener("resize", ajustarBotones);
window.addEventListener("load", ajustarBotones);

// Ésta es la función para realizar los cálculos
function calculo(num1, num2, operacion){
    switch(operacion){
        case 1: 
            //Suma
            return num1 + num2;
        case 2:
            // Resta
            return (num1 - num2);
        case 3:
            // Multiplicación
            return num1 * num2;
        case 4:
            // División
            return num1 / num2;
        case 5:
            // Raíz cuadrada
            return Math.sqrt(num1);
        case 6:
            // Porcentaje
            num2 = num2 / 100;
            return num1 * num2;
        default: 
            return "ERROR";
    }
    
}

// Para limpiar la pantalla y así reiniciar los cálculos
function limpiarPantalla(){
    document.getElementById("pantalla").innerHTML = 0;
    n1 = "";
    n2 = "";
    primero = true;
    oprcn = 0;
}

// Función que recoge los datos mediante los botones
function recogidaDatos(n){
    if(primero){
        if(n1 == "" && n == "."){
            n1 += 0;
        }
        if(n == "." && n1.includes(".")) {
            document.getElementById("error").innerHTML = "No puedes introducir dos puntos en un número<br>";

        }else {
            n1 += n;
            document.getElementById("pantalla").innerHTML = n1;

        }
        
    }else{
        if(n2 == "" && n == "."){
            n2 += 0;
        }
        if(n == "." && n2.includes(".")) {
            document.getElementById("error").innerHTML = "No puedes introducir dos puntos en un número<br>";

        }else {
            n2 += n;
            document.getElementById("pantalla").innerHTML = n2;

        }
    }
}

// Función que reliza el cambio para recoger los datos en el siguiente número para el cálculo 
function cambio(){
    primero = false;
    document.getElementById("pantalla").innerHTML = 0;

}

// Función que selecciona la operación que se va a utilizar
function operacion(n){
    if(oprcn == 0){
        oprcn = parseFloat(n);
        cambio();

    }else if(n == 5){
        oprcn = n;
        resultado();

    }else{
        document.getElementById("error").innerHTML = "No puedes realizar más de una operación a la vez, primero resuelve el cálculo y luego continuas haciendo las operaciones<br>";

    }
    cE();
}

// Función que realiza las operaciones necesarias para llamar a la función cáclulo sin que el programa explote
function resultado(){
    let numero1 = parseFloat(n1);
    if(n2 != "" && oprcn != 5){
        debugger;
        let numero2 = parseFloat(n2);

        n1 = calculo(numero1, numero2, oprcn);
    
        document.getElementById("pantalla").innerHTML = n1;
        n2 = "";
        oprcn = 0;
        primero = true;

    }else if(n2 == "" && oprcn == 5){
        debugger;
        n1 = calculo(numero1, 0, oprcn);
    
        document.getElementById("pantalla").innerHTML = n1;
        n2 = "";
        oprcn = 0;
        primero = true;
    }else{
        document.getElementById("error").innerHTML = "Debes introducir un segundo número para realizar el cálculo<br>";

    }
    cE();
}

// Función que reliza la recogida de datos mediante las teclas
document.addEventListener("keydown", manejarTecla);

function manejarTecla(event) {
    document.getElementById("error").innerHTML = "";
    if(primero){
        const tecla = event.key; // ejemplo: "1", "2", "+", "Enter", "Backspace"

        // Si la tecla es un operador
        if (/^[+\-\/%*]+$/.test(tecla)) {
            if(!cE()){
                if(tecla == "+"){
                    operacion(1);
                }else if(tecla == "-"){
                    operacion(2);
                }else if(tecla == "*"){
                    operacion(3);
                }else if(tecla == "/"){
                    operacion(4);
                }else if(tecla == "%"){
                    operacion(6);
                }else{
                    document.getElementById("error").innerHTML = "Operador no válido<br>";
                }
                document.getElementById("pantalla").innerHTML = n1;
            }
            cE();
            
            // Recoge los números o la coma para poder añadirla al string
        }else if(/^\d+(\.\d+)?$|^\.$/.test(tecla)) {
            if(n1 == "" && tecla == "."){
                n1 += 0;
            }
            if(tecla == "." && n1.includes(".")) {
                document.getElementById("error").innerHTML = "No puedes introducir dos puntos en un número<br>";

            }else {
                n1 += tecla;
                document.getElementById("pantalla").innerHTML = n1;

            }
        }

        // Si pulsa Enter → calcular
        else if (tecla === "Enter") {
            document.getElementById("error").innerHTML = "Necesitas seleccionar un operador para continuar";
            //resultado();
            cE();

        }

        // Si pulsa Backspace → borrar último carácter
        else if (tecla === "Backspace") {
            n1 = n1.slice(0, -1);
            document.getElementById("pantalla").innerHTML = n1;
        }
        
    }else{ 
        // En el caso haber introducido el primer número, para n2
        
        const tecla = event.key; // ejemplo: "1", "2", "+", "Enter", "Backspace"

        // Si la tecla es un número o una coma, la añadimos
        if(/^\d+(\.\d+)?$|^\.$/.test(tecla)) {
            if(n2 == "" && tecla == "."){
                n2 += 0;
            }
            if(tecla == "." && n2.includes(".")) {
                document.getElementById("error").innerHTML = "No puedes introducir dos puntos en un número<br>";

            }else {
                n2 += tecla;
                document.getElementById("pantalla").innerHTML = n2;
                
            }
            cE();

            // Si la tecla es un operador daría error porque ya está seleccionado 
        }else if (/^[+\-\/%*]+$/.test(tecla)) {
            document.getElementById("error").innerHTML = "Debes introducir un segundo número para realizar el cálculo<br>";
        }

        // Si pulsa Enter → calcular
        else if (tecla === "Enter") {
            if(n2 == ""){
                document.getElementById("error").innerHTML = "Necesitas añadir un segundo número para realizar la operación";
            }else{
                resultado();
            }
            cE();
        }

        // Si pulsa Backspace → borrar último carácter
        else if (tecla === "Backspace") {
            n2 = n2.slice(0, -1);
            document.getElementById("pantalla").innerHTML = n2;
        }
    }
}

// Función que permite al usuario limpiar la última operación realizada
function cE(){
    debugger;
    if(oprcn == 5){
        resultado();
        return true;
    }else if(oprcn != 0){
        document.getElementById("limpiar").innerHTML = "CE";
        // Desactivo todos los botones de raiz, resta, suma, división, multiplicación y porcentaje
        document.getElementById("raiz").setAttribute("class", "botones-desactivados");
        document.getElementById("raiz").setAttribute("enable", true);
        document.getElementById("resta").setAttribute("class", "botones-desactivados");
        document.getElementById("resta").setAttribute("enable", true);
        document.getElementById("suma").setAttribute("class", "botones-desactivados");
        document.getElementById("suma").setAttribute("enable", true);
        document.getElementById("multi").setAttribute("class", "botones-desactivados");
        document.getElementById("multi").setAttribute("enable", true);
        document.getElementById("porcentaje").setAttribute("class", "botones-desactivados");
        document.getElementById("porcentaje").setAttribute("enable", true);
        document.getElementById("division").setAttribute("class", "botones-desactivados");
        document.getElementById("division").setAttribute("enable", true);

        // Asigno al botón de CE la funcion de cancelar operacion
        document.getElementById("limpiar").setAttribute("onclick", "desactivarOperacion()");
        return true;
    }else{
        document.getElementById("limpiar").innerHTML = "C";
        document.getElementById("limpiar").setAttribute("onclick", "limpiarPantalla()");

        document.getElementById("raiz").setAttribute("class", "boton");
        document.getElementById("raiz").setAttribute("enable", false);

        document.getElementById("resta").setAttribute("class", "boton");
        document.getElementById("resta").setAttribute("enable", false);

        document.getElementById("suma").setAttribute("class", "boton");
        document.getElementById("suma").setAttribute("enable", false);

        document.getElementById("multi").setAttribute("class", "boton");
        document.getElementById("multi").setAttribute("enable", false);

        document.getElementById("porcentaje").setAttribute("class", "boton");
        document.getElementById("porcentaje").setAttribute("enable", false);

        document.getElementById("division").setAttribute("class", "boton");
        document.getElementById("division").setAttribute("enable", false);
        return false;
    }
}

function desactivarOperacion(){
    debugger;
    if(oprcn != 0 && n2 == ""){
        oprcn = 0;
        primero = true;
        
    }else if(oprcn != 0 && n2 != "") {
        n2 = "";
        document.getElementById("pantalla").innerHTML = n2;
        
    }
    cE();
}