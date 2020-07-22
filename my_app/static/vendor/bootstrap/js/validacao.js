   $("#pesquisa_form").validate({
      rules : {
            pesquisa: {
					required: true,
					minlength: 3,
					maxlength: 50
				}
       },
      messages:{
            pesquisa:{
                    required:"Por favor, informe a palavra para pesquisa",
                    minlength:"O nome deve ter pelo menos 3 caracteres",
                    maxlength:"O nome deve ter no máximo 50 caracteres"
            }
       }
});
