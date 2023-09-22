/* ************************************************************************ */

/* ======================================== */
/*              Datos usuarios              */
/* ======================================== */

/* Editar usuario */
$(document).on("click", "#btnEditUser", function () {
    var edi_id_us = $(this).data('edi_id_us');
    var edi_us_us = $(this).data('edi_us_us');
    var edi_nom_us = $(this).data('edi_nom_us');
    var edi_id_rol_us = $(this).data('edi_id_rol_us');
    var edi_est_us = $(this).data('edi_est_us');
    var edi_fech_us = $(this).data('edi_fech_us');
    $("#edi_id_us").val(edi_id_us);
    $("#edi_us_us").val(edi_us_us);
    $("#edi_nom_us").val(edi_nom_us);
    $("#edi_id_rol_us").val(edi_id_rol_us);
    $("#edi_est_us").val(edi_est_us);
    $("#edi_fech_us").val(edi_fech_us);

});

/* Eliminar usuario */
$(document).on("click", "#btnDeleteUser", function () {
    var eli_nom_us = $(this).data('eli_nom_us');
    var eli_id_us = $(this).data('eli_id_us');
    $("#eli_nom_us").val(eli_nom_us);
    $("#eli_id_us").val(eli_id_us);

});

/* Editar clave usuario */
$(document).on("click", "#btnClaveUser", function () {
    var cla_nom_us = $(this).data('cla_nom_us');
    var cla_id_us = $(this).data('cla_id_us');
    $("#cla_nom_us").val(cla_nom_us);
    $("#cla_id_us").val(cla_id_us);

});

/* ************************************************************************ */

/* ======================================== */
/*              Datos paginas               */
/* ======================================== */

/* Editar imagen paginas */
$(document).on("click", "#btnEditImgPage", function () {
    var id_edi_img_pag = $(this).data('id_edi_img_pag');
    var img_pag = $(this).data('img_pag');
    $("#id_edi_img_pag").val(id_edi_img_pag);
    $("#img_pag").attr('src',img_pag);

});

/* Editar paginas */
$(document).on("click", "#btnEditPage", function () {
    var id_edi_page = $(this).data('id_edi_page');
    var nom_edi_page = $(this).data('nom_edi_page');
    var url_edi_page = $(this).data('url_edi_page');
    var est_edi_page = $(this).data('est_edi_page');
    var fech_edi_page = $(this).data('fech_edi_page');
    $("#id_edi_page").val(id_edi_page);
    $("#nom_edi_page").val(nom_edi_page);
    $("#url_edi_page").val(url_edi_page);
    $("#est_edi_page").val(est_edi_page);
    $("#fech_edi_page").val(fech_edi_page);

});

/* Eliminar paginas */
$(document).on("click", "#btnDeletePage", function () {
    var id_eli_page = $(this).data('id_eli_page');
    var nom_page = $(this).data('nom_page');
    $("#id_eli_page").val(id_eli_page);
    $("#nom_page").val(nom_page);

});

/* ************************************************************************ */

/* ======================================== */
/*              Datos carrusel               */
/* ======================================== */

/* Editar imagen carrusel */
$(document).on("click", "#btnImgCarrusel", function () {
    var id_edi_img_carro = $(this).data('id_edi_img_carro');
    var img_carro = $(this).data('img_carro');
    $("#id_edi_img_carro").val(id_edi_img_carro);
    $("#img_carro").attr('src',img_carro);

});

/* Editar carrusel */
$(document).on("click", "#btnEditCarrusel", function () {
    var id_edi_carro = $(this).data('id_edi_carro');
    var nom_edi_carro = $(this).data('nom_edi_carro');
    var est_edi_carro = $(this).data('est_edi_carro');
    var fech_edi_carro = $(this).data('fech_edi_carro');
    $("#id_edi_carro").val(id_edi_carro);
    $("#nom_edi_carro").val(nom_edi_carro);
    $("#est_edi_carro").val(est_edi_carro);
    $("#fech_edi_carro").val(fech_edi_carro);
    
});

/* Eliminar carrusel */
$(document).on("click", "#btnDeleteCarrusel", function () {
    var id_eli_carro = $(this).data('id_eli_carro');
    var nom_eli_carro = $(this).data('nom_eli_carro');
    $("#id_eli_carro").val(id_eli_carro);
    $("#nom_eli_carro").val(nom_eli_carro);

});

/* ************************************************************************ */

/* ======================================== */
/*              Datos empleados             */
/* ======================================== */

/* Editar imagen carrusel */
$(document).on("click", "#btnEditImgEmpleado", function () {
    var id_edi_img_emp = $(this).data('id_edi_img_emp');
    var img_emp = $(this).data('img_emp');
    $("#id_edi_img_emp").val(id_edi_img_emp);
    $("#img_emp").attr('src',img_emp);

});

/* Editar empleados */
$(document).on("click", "#btnEditEmpleados", function () {
    var id_edi_emp = $(this).data('id_edi_emp');
    var nom_edi_emp = $(this).data('nom_edi_emp');
    var edi_est_emp = $(this).data('edi_est_emp');
    var edi_fech_emp = $(this).data('edi_fech_emp');
    $("#id_edi_emp").val(id_edi_emp);
    $("#nom_edi_emp").val(nom_edi_emp);
    $("#edi_est_emp").val(edi_est_emp);
    $("#edi_fech_emp").val(edi_fech_emp);
    
});

/* Eliminar empleados */
$(document).on("click", "#btnDeleteEmpleados", function () {
    var id_eli_emp = $(this).data('id_eli_emp');
    var nom_eli_emp = $(this).data('nom_eli_emp');
    $("#id_eli_emp").val(id_eli_emp);
    $("#nom_eli_emp").val(nom_eli_emp);

});

/* ************************************************************************ */

/* ======================================== */
/*              Datos noticias              */
/* ======================================== */

/* Editar imagen carrusel */
$(document).on("click", "#btnEditImgNoticias", function () {
    var id_edi_img_not = $(this).data('id_edi_img_not');
    var img_not = $(this).data('img_not');
    $("#id_edi_img_not").val(id_edi_img_not);
    $("#img_not").attr('src',img_not);

});

/* Editar noticia */
$(document).on("click", "#btnEditNoticias", function () {
    var edi_id_not = $(this).data('edi_id_not');
    var edi_tit_not = $(this).data('edi_tit_not');
    var edi_sub_tit_not = $(this).data('edi_sub_tit_not');
    var edi_cue_not = $(this).data('edi_cue_not');
    var edi_est_not = $(this).data('edi_est_not');
    var edi_fech_not = $(this).data('edi_fech_not');
    $("#edi_id_not").val(edi_id_not);
    $("#edi_tit_not").val(edi_tit_not);
    $("#edi_sub_tit_not").val(edi_sub_tit_not);
    $("#edi_cue_not").val(edi_cue_not);
    $("#edi_est_not").val(edi_est_not);
    $("#edi_fech_not").val(edi_fech_not);
    
});

/* Eliminar noticia */
$(document).on("click", "#btnDeleteNoticias", function () {
    var eli_id_not = $(this).data('eli_id_not');
    var eli_tit_not = $(this).data('eli_tit_not');
    $("#eli_id_not").val(eli_id_not);
    $("#eli_tit_not").val(eli_tit_not);

});

/* ************************************************************************ */

/* ======================================== */
/*              Datos permisos              */
/* ======================================== */

/* Editar permisos */
$(document).on("click", "#btnEditPermiso", function () {
    var edi_id_per = $(this).data('edi_id_per');
    var edi_id_rol_per = $(this).data('edi_id_rol_per');
    var edi_id_page_per = $(this).data('edi_id_page_per');
    var edi_est_per = $(this).data('edi_est_per');
    $("#edi_id_per").val(edi_id_per);
    $("#edi_id_rol_per").val(edi_id_rol_per);
    $("#edi_id_page_per").val(edi_id_page_per);
    $("#edi_est_per").val(edi_est_per);
    
});

/* Eliminar permisos */
$(document).on("click", "#btnDeletePermiso", function () {
    var eli_id_per = $(this).data('eli_id_per');
    $("#eli_id_per").val(eli_id_per);
    $("#most_id_per").val(eli_id_per);

});

/* ************************************************************************ */

/* ======================================== */
/*                 Datos rol                */
/* ======================================== */

/* Editar rol */
$(document).on("click", "#btnEditRol", function () {
    var edi_id_rol = $(this).data('edi_id_rol');
    var edi_nom_rol = $(this).data('edi_nom_rol');
    var edi_est_rol = $(this).data('edi_est_rol');
    var edi_fech_rol = $(this).data('edi_fech_rol');
    $("#edi_id_rol").val(edi_id_rol);
    $("#edi_nom_rol").val(edi_nom_rol);
    $("#edi_est_rol").val(edi_est_rol);
    $("#edi_fech_rol").val(edi_fech_rol);
    
});

/* Eliminar rol */
$(document).on("click", "#btnDeleteRol", function () {
    var eli_id_rol = $(this).data('eli_id_rol');
    var eli_nom_rol = $(this).data('eli_nom_rol');
    $("#eli_id_rol").val(eli_id_rol);
    $("#eli_nom_rol").val(eli_nom_rol);

});

/* ************************************************************************ */

/* ======================================== */
/*              Datos inventario            */
/* ======================================== */

/* Editar Inventario */
$(document).on("click", "#btnEditHardware", function () {
    var edi_id_har = $(this).data('edi_id_har');
    var edi_id_emp_har = $(this).data('edi_id_emp_har');
    var edi_des_har = $(this).data('edi_des_har');
    var edi_mar_har = $(this).data('edi_mar_har');
    var edi_mod_har = $(this).data('edi_mod_har');
    var edi_ser_har = $(this).data('edi_ser_har');
    var edi_pro_har = $(this).data('edi_pro_har');
    var edi_com_har = $(this).data('edi_com_har');
    $("#edi_id_har").val(edi_id_har);
    $("#edi_id_emp_har").val(edi_id_emp_har);
    $("#edi_des_har").val(edi_des_har);
    $("#edi_mar_har").val(edi_mar_har);
    $("#edi_mod_har").val(edi_mod_har);
    $("#edi_ser_har").val(edi_ser_har);
    $("#edi_pro_har").val(edi_pro_har);
    $("#edi_com_har").val(edi_com_har);
    
});

/* Eliminar Inventario */
$(document).on("click", "#btnDeleteHardware", function () {
    var eli_id_per = $(this).data('eli_id_per');
    var eli_com_har = $(this).data('eli_com_har');
    $("#eli_id_per").val(eli_id_per);
    $("#eli_com_har").val(eli_com_har);

});