#���ÿ�
var jqry = document.createElement('script');
jqry.src='https://code.jquery.com/jquery-3.3.1.js';
head = document.getElementsByTagName('head');
head[0].appendChild(jqry);

#ת��˵˵ҳ��
var shuoshuo = $('[title="˵˵"]');
shuoshuo.get(0).click();

var textContent = document.getElementsByTagName('pre');
var page = document.getElementById('pager_num_0_2');
var page = document.getElementById('pager_next_3');
page.click()


page = $('[title="��һҳ"]');
page.get(0).click();