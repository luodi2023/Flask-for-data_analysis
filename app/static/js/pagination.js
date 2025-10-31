let index = 1;
let li_objs = document.getElementsByClassName('page-item');
li_objs[index].setAttribute('class', 'page-item active');

function clear_page(){
    for (var i = 0; i < li_objs.length; i++) {
          li_objs[i].setAttribute('class', 'page-item');
    }
}

function loc_page(id){
    clear_page();
    li_objs[id].setAttribute('class', 'page-item active');
}

function li_left(){
    if(index > 1){
        clear_page();
        li_objs[--index].setAttribute('class', 'page-item active');
    }
}

function li_right(){
    if(index < li_objs.length - 2){
        clear_page();

        li_objs[++index].setAttribute('class', 'page-item active');


    }
}
