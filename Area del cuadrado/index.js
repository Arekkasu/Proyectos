var formulario = document.getElementsByName('calculate')[0],
    valor = calculate.elements,
    boton = document.getElementById('boton');
    resultado = document.getElementById('resultado')
    resultado.classList.toggle('shadow-drop-2-center');

var proceso = (un_reload) => {
    if(calculate.lado.value == 0){
        alert('tiene que se mayor que 0')
        un_reload.preventDefault()
        return
    }
    else{
        
        
        area = calculate.lado.value*formulario.lado.value

        

        resultado.value = area

        resultado.style.visibility = 'visible'
        

        resultado.classList.toggle('shadow-drop-2-center');
        un_reload.preventDefault()
        
    }
}

calculate.addEventListener('submit', proceso);



