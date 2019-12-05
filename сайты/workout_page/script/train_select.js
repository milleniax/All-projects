var data_base = {
	"плечи": ["отжимания на брусьях","отжимания","отжимания в стойке на руках","армейские отжимания","алмазные отжимания","горзионтальный упор","упор супермена"],
	"бицепс":["подтягивания","подтягивания обратным хватом","выход силой","узкие подтягивания","подтяг,ивания ганнибала"],
	"спина":["подтягивания","австралийские подтягивания","широкие подтягивания","выход силой","узкие подтягивания","подтягивания ганнибала"],
	"трицепс":["отжимания ганнибала","отжимания на брусьях","алмазные отжимания","отжимания на одной","отжимания с прижатыми локтями"],
	"грудь":["отжимания на брусьях","отжимания","алмазные отжимания","отжимания на турнике","отжимания с наклоном вперед"],
	"пресс":["поднятие ног к турнику","книжка","скручивания","уголок","флаг дракона","планка","ножницы"],
	

}
var modal = document.getElementById('modal').classList;
var overlay = document.getElementById('overlay').classList;

document.querySelector('input').addEventListener('keydown', function(e) {
    if (e.keyCode === 13) {
      	var text = document.getElementById('input').value;
      	if(data_base[text] !== undefined){

      		var table = '<table class="exercise_list">';
      		row = data_base[text].length;
			for( var i = 0; i < row; i++ ){

				table += '<tr>';

				table += '<td>' +  (i + 1) + '.' + data_base[text][i]  + '</td>';

				table += '</tr>';
			}
			table += '</table>';

			modal.add('active');
			overlay.add('active');
			document.getElementById('modal').innerHTML = table;

			
      	}

      	else{

      		alert("Такой группы мышц или элемента нет в базе");
      	}
      	
		  }
  });

document.querySelector('div').addEventListener('click', function(e) {
			modal.remove('active');
			overlay.remove('active');
	  });
