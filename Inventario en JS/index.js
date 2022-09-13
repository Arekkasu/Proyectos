const inv = {
}

var listado = document.getElementsByName('inventario')[0], //Nombre del <form>
    boton = document.getElementById('agregar'), //Name de boton
    eliminar = document.getElementsByName('delete'),
    items = document.getElementById('items'),
    reset = document.getElementById('reset');


// Funcion para evitar que se recopie el ciclo
const limpiar = () => {

    items.innerHTML = ' '

}

//Funcion de hacer la lista de los productos

const lista = (un_reload) => {
        
        for (const c in inv) {
        //items es la Id del Ul

        items.innerHTML += `    <li id='item'>
        <div class="container-fluid">
            <div class="row">
                <div class="col-lg-3">
                    <p class='item_text'>${c}</p>
                </div>
                <div class="col-lg-3">
                    <p class='cantidad_item'>${inv[c][0]}</p>
                </div>
                <div class="col-lg-3">
                    <p class='precio_item'>${inv[c][1]}</p>
                </div>
                <div class='col-lg-3' id='borrar'>
                    <button class="btn btn-primary delete" id="borrar"><i class="fa-solid fa-trash"></i></button>
                </div>
            </div>
        </div>
    </li>`
    }
};



//al accionar agregar sucede esto

var proceso = (un_reload) => {
    if(listado.nombre.value.length == 0  || listado.cantidad.value.length == 0 || listado.precio.value.length == 0){
        alert('Por favor rellene los datos')
        un_reload.preventDefault()
        return;
    }
    if(!inv.hasOwnProperty(listado.nombre.value)){
        inv[listado.nombre.value] = new Array
    }
    inv[listado.nombre.value].push(listado.cantidad.value) 
    inv[listado.nombre.value].push(listado.precio.value)
    
    limpiar()
    lista()
    
    un_reload.preventDefault()
}


listado.addEventListener('submit', proceso)



reset.addEventListener('submit', proceso)