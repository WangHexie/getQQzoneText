#引用库
var jqry = document.createElement('script');
jqry.src='https://code.jquery.com/jquery-3.3.1.js';
head = document.getElementsByTagName('head');
head[0].appendChild(jqry);

#转到说说页面
var shuoshuo = $('[title="说说"]');
shuoshuo.get(0).click();

var textContent = document.getElementsByTagName('pre');
var page = document.getElementById('pager_num_0_2');
var page = document.getElementById('pager_next_3');
page.click()


page = $('[title="下一页"]');
page.get(0).click();