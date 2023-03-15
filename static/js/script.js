var i = document.getElementById('tipo');
var f = document.getElementById('formpopup');
var d = document.getElementById('descricao');

function updateSpan(id){
    var teste = id;
    var s = document.getElementById(teste);
    document.getElementById('textoform').innerHTML = 'Texto da nota:';
    d.value = s.text;
    var aux = "/update/";
    aux = aux.concat(teste).concat('/');
    f.action = aux
}

function mudaTipo(idcard, idtipo){
    var modalcard = document.getElementById('modalcard');
    modalcard.value = idcard;
    var st = "btn"+idtipo;
    var valid = document.getElementById(st);
    var limpacampo = document.getElementsByName('btntipomuda');
    for(var c=0; c <limpacampo.length; c++){
        limpacampo[c].disabled = false;
    }
    valid.disabled = true;

}

function tipoInput(n, ty){
    d.value = ''
    document.getElementById('textoform').innerHTML = 'Texto da nota:';
    i.value = ty;
    aux = "/criar";
    aux = aux.concat('/');
    f.action = aux
}

function criarTipo(){
    var aux = "/criartipo/";
    d.value = ''
    f.action = aux
    document.getElementById('textoform').innerHTML = 'Texto do cardboard:';

}