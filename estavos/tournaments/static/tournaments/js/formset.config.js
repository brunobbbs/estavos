jQuery(document).ready(function() {
    var prefix = jQuery(".formset-prefix").attr('prefix');
    jQuery("#form-subscription tbody tr").formset({
        prefix: prefix,
        addText: "Adicionar outro",
        deleteText: "Remover"
    });
});
