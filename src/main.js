import Vue from 'vue'
import App from './App.vue'
import layer from 'vue-layer'
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'
import VideoPlayer from 'vue-video-player'
import axios from 'axios';
Vue.prototype.$axios = axios;
require('video.js/dist/video-js.css')
require('vue-video-player/src/custom-theme.css')
Vue.use(VideoPlayer)
Vue.use(ElementUI)
Vue.prototype.$layer = layer(Vue);
Vue.config.productionTip = false

new Vue({
  render: h => h(App),
}).$mount('#app')
var dbody=document.getElementsByClassName('wrap')[0];
//ff用
objAddEvent(document,'DOMMouseScroll', function(e){return mouse_scroll(e);})

//非ff chrome 用
objAddEvent(document,'mousewheel', function(e){return mouse_scroll(e);})

//chrome用
objAddEvent(dbody,'mousewheel', function(e){return mouse_scroll(e);})
function mouse_scroll(e){
  e=e || window.event;
  var delD=e.wheelDelta?e.wheelDelta: -e.detail*40;//判断上下方向
  // var move_s=delD>0?-50:50;
  var move_s = delD;
  document.documentElement.scrollLeft+=move_s; //非chrome浏览器用这个
  // document.getElementById('form').style.transform = "translate(" + move_s + "px,0)";
// chrome浏览器用这个
  var original_radius_x = parseInt(document.getElementById('form').style.borderRadius[0]);
  var original_radius_y = parseInt(document.getElementById('form').style.borderRadius[3]);
  if(document.documentElement.scrollLeft==0){
    document.body.scrollLeft+=0.1 * move_s;
    // document.getElementById('form').style.transform = "translate(" + move_s + "px,0)"
    document.getElementById('form').style.borderRadius = (move_s * 10 + original_radius_x) + "px 0 0 " + (move_s * 10 + original_radius_y) + "px";
  }
  return false;
}
//这个是给对象增加监控方法的函数
function objAddEvent(oEle, sEventName, fnHandler)
{
  if(oEle.attachEvent) oEle.attachEvent('on'+sEventName, fnHandler);
  else oEle.addEventListener(sEventName, fnHandler, false);
}

