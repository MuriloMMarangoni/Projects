let links = document.querySelectorAll('.links')      /* pega todos os links e empacota */
let link1 = links[0]                                 /* desempacota os links */
let link2 = links[1]
let link3 = links[2]
let link4 = links[3]
let sobre_mim = document.querySelector('#sobre_mim') /* textos ao clique */
let formacao  = document.querySelector('#formacao')
let portifolio= document.querySelector('#portifolio')
let contato   = document.querySelector('#contato')
function reset(){                                    /* não exibe nenhum dos 4 textos*/
    sobre_mim.style.display = 'none';
    formacao.style.display = 'none';
    portifolio.style.display = 'none';
    contato.style.display = 'none';
}

reset();                                             /* por padrão já desativa os 4 textos */

link1.addEventListener('click',event=>{              /* desativa os 4 e ativa o texto correspondente a opção clicada */
    event.preventDefault();
    reset();
    sobre_mim.style.display = 'inline-block';        /* exibe o texto correspondente */
})
link2.addEventListener('click',event=>{
    event.preventDefault();
    reset();
    formacao.style.display = 'inline-block';
})
link3.addEventListener('click',event=>{
    event.preventDefault();
    reset();
    portifolio.style.display = 'inline-block';
})
link4.addEventListener('click',event=>{
    event.preventDefault();
    reset();
    contato.style.display = 'inline-block';
})