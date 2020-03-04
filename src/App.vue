<template>
  <div style="height: 100%;width:200%;overflow: hidden" >
  <div id="app" style="height: 100%;width:100%;overflow: hidden">
    <div class="h_container parallax_cover" style="height: 100%;" id="cover">
      <Cover></Cover>
    </div>
    <div class="h_container parallax_form" id="form">
      <VideoGetEar msg="Welcome to Your Vue.js App"/>
    </div>
  </div>
  </div>
</template>

<script>
import VideoGetEar from './components/VideoGetEar.vue'
import Cover from './components/Cover.vue'

export default {
  name: 'App',
  components: {
    VideoGetEar,
    Cover
  },mounted () {//给window添加一个滚动滚动监听事件

  },
  methods:{

  },
  destroyed () {//离开该页面需要移除这个监听的事件
    window.removeEventListener('scroll', this.handleScroll)
  },
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
  margin: 0;
  border: 0;
}
.h_container{
  width: 50%;
  height: 100%;
  overflow:hidden;
  font-size: 100%;
  display: inline-block;
  margin:0;
  border:0;

}
.parallax_form{

}
img{
  float:right;
}
.parallax_cover {
  /* The image used */
  background-image: url("picture/Cover_background.jpg");

  /* Set a specific height */
  height: 100%;

  /* Create the parallax scrolling effect */
  background-attachment: fixed;
  background-position: center;
  background-repeat: no-repeat;
  background-size: cover;
}
</style>
