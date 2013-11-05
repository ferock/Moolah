m = jQuery.noConflict();
m(document).ready(function(){
	/* --- [Interface de Registro] --- */
	
	/* --- [Efect Inputs] --- */
	m(".campo input").on("focus",function(){efectInput(this,"data-minw");})
	m(".campo input").on("blur",function(){
		val = parseInt(m(this).val().length);
		if(val<1){
			efectInput(this,"data-maxw");
		}
	})
	m(".campo input").hover(function(){
		efectInput(this,"data-minw");
	},function(){
		val = parseInt(m(this).val().length);
		if(val<1){efectInput(this,"data-maxw");}
	})
	function efectInput(pThis,w){
		if(!pThis){return false;}
		Label = m(pThis).parent().find("p.label");
		Label.stop().animate({"width":Label.attr(w)},300);
	}
	
	/* --- [Cuando cambia el tipo de cuenta] --- */
	m('.campo input[type="radio"]').on("change",function(){
		m('.campo input[type="radio"]').parent().removeClass("active");
		if(m(this).val()){
			m(this).parent().addClass("active");
		}
	})
	
	/* --- [Agregar nuevos Beneficiarios] --- */
	m("form#addPayee").on("submit",function(){
		Campos = m(this).serialize();
		console.log(Campos)
		m.ajax({
			type:"POST",
			url:"/addBeneficiario",
			data:Campos,
			success:function(ID, textStatus, jqXHR){
				NewRemitente = "<li id='remi_"+ID+"'>"+m("#addPayee #name").val()+"<span class='del'>delete</span></li>";
				m(".beneficiarios .lista ul").append(NewRemitente);
				m(".beneficiarios .lista ul li#remi_"+ID+" span.del").on("click",function(){Eliminar(this)});
				m(".payee input[type='text']").val("");
			},
			error:function(jqXHR, textStatus, errorThrown){
				m(".beneficiarios .lista").html("Error al agrega");
			},
			complete:function(){
			}
		});
		return false;
	})
	
	/* --- [Eliminar Beneficiarios] --- */
	m(".beneficiarios .lista ul li span.del").on("click",function(){Eliminar(this)});
	
	/* --- [Enviar x Ajax el ID y Eliminar] --- */
	function Eliminar(pThis){
		m(pThis).parent().remove();
	}
})