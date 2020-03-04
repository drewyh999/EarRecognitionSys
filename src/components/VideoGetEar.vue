<template>
  <div >
  <div class="pic_block" v-if = "EarFaceURL !=''">
  <div style="height:100px;">
   <el-button v-if="resultForm==''" type="primary" @click="submit">{{buttonLog}}</el-button>
   <span v-else >{{resultForm}}</span>
  </div>
   <div style=" padding:50px;text-align:center">
    <el-image
      style="width: 200px; height: 200px;margin-bottom:80%;border:#999 solid 1px;padding:20px;"
      :src="EarFaceURL"
      fit = "contain"
      ></el-image>

    </div>
   </div>

    <div style="text-align: center">
        <div class="pic_img">
            <div class="pic_img_box">
                <p class="type_title">
                    <span>上传视频</span>
                </p>
                <el-upload class="avatar-uploader"
                           action="http://localhost:5000/upload"
                           v-bind:data="{FoldPath:'上传目录',SecretKey:'安全验证'}"
                           v-bind:on-progress="uploadVideoProcess"
                           v-bind:on-success="handleVideoSuccess"
                           v-bind:before-upload="beforeUploadVideo"
                           v-bind:show-file-list="false">

                    <i v-if="videoForm.showVideoPath =='' && !videoFlag"
                       class="el-icon-plus v_icon"></i>
                    <div v-if="videoFlag == true" style="height: 260px;width: 350px;" class="el-icon-plus">
                        <el-progress
                                type="circle"
                                v-bind:percentage="imageUploadPercent"
                        ></el-progress>
                    </div>
                </el-upload>

                <video v-if="videoForm.showVideoPath !='' && !videoFlag"
                           v-bind:src="videoForm.showVideoPath"
                           class="avatar video-avatar"
                           controls="controls">
                        您的浏览器不支持视频播放
                </video>
                <p>最多可以上传1个视频,推荐格式mp4</p>
            </div>
            <div class="pic_img_box">
                <p class="type_title">
                    <span>上传图片</span>
                </p>
                <el-upload class="avatar-uploader"
                           action="http://localhost:5000/upload"
                           v-bind:data="{FoldPath:'上传目录',SecretKey:'安全验证'}"
                           v-bind:on-progress="uploadimageProcess"
                           v-bind:on-success="handleimageSuccess"
                           v-bind:before-upload="beforeUploadimage"
                           v-bind:show-file-list="false">
                    <i v-if="imageForm.showimagePath =='' && !imageFlag"
                       class="el-icon-plus e_icon"></i>
                    <div v-if="imageFlag == true" style="height: 260px;width: 350px;">
                        <el-progress
                                 type="circle"
                                 v-bind:percentage="imageUploadPercent"
                                 ></el-progress>
                    </div>
                </el-upload>
                <el-card class="box-card" style="width: 350px">
                <el-form :model="ruleForm"  label-width="50px" class="ruleForm" v-loading="Formloading">
                    <el-form-item label="姓名" >
                        <el-input v-model="ruleForm.name" autocomplete="off"></el-input>
                    </el-form-item>
                    <el-form-item label="年龄" style="margin-bottom: 19px">
                        <el-input-number style="width:100%" :min="1" :max="100" v-model.number="ruleForm.age"></el-input-number>
                    </el-form-item>
                    <el-form-item label="性别" style="margin-bottom: 19px">
                            <el-radio v-model="ruleForm.gender" label="male" >男</el-radio>
                            <el-radio v-model="ruleForm.gender" label="female" >女</el-radio>
                    </el-form-item>

                    <el-form-item >
                        <el-button style="width: 100%; max-height: 80%" type="primary" @click="submitForm('ruleForm')">提交</el-button>
                    </el-form-item>
                </el-form>
                </el-card>

                <video v-if="imageForm.showimagePath !='' && !imageFlag"
                       v-bind:src="imageForm.showimagePath"
                       class="avatar video-avatar"
                       controls="controls">
                    您的浏览器不支持视频播放
                </video>
                 <p>
                    *支持图片格式为png/jpg/jpeg
                </p>
            </div>
        </div>
    </div>
</div>
</template>

<script>
import layer from 'vue-layer'
import axios from 'axios'
export default {
  name: 'imageGetEar',
        data(){
          return{
            videoFlag: false,
            //是否显示进度条
            videoUploadPercent: '',
            //进度条的进度，
            isShowUploadVideo: false,
            //显示上传按钮
            videoForm: {
                showVideoPath: ''
            },
              imageFlag: false,
              //是否显示进度条
              imageUploadPercent: '',
              //进度条的进度，
              isShowUploadimage: false,
              //显示上传按钮
              imageForm: {
                  showimagePath: ''
              },
            EarFaceURL:'',
            resultForm:'',
            buttonLog:'确认对象',
              ruleForm:{
                'name':'',
                  'gender':'',
                  'age':'',
              },
              Formloading:false

        }},
        methods:{
            //上传前回调
            beforeUploadVideo(file) {
                var fileSize = file.size / 1024 / 1024 < 50;
                if (['video/mp4', 'video/ogg', 'video/flv', 'video/avi', 'video/wmv', 'video/rmvb', 'video/mov'].indexOf(file.type) == -1) {
                    this.$message.error('请上传正确的格式');
                    return false;
                }
                if (!fileSize) {
                    layer.msg("视频大小不能超过50MB");
                    return false;
                }
                this.isShowUploadVideo = false;
            },
            beforeUploadimage(file) {
                var fileSize = file.size / 1024 / 1024 < 5;
                if (['image/jpeg', 'image/png', 'image/jpg'].indexOf(file.type) == -1) {
                    this.$message.error('请上传正确的格式');
                    return false;
                }
                if (!fileSize) {
                    layer.msg("图片大小不能超过5MB");
                    return false;
                }
                this.isShowUploadimage = false;
            },
            //进度条
            uploadVideoProcess(event, file) {
                this.videoFlag = true;
                this.videoUploadPercent = file.percentage.toFixed(0) * 1;
            },
            uploadimageProcess(event, file) {
                this.imageFlag = true;
                this.imageUploadPercent = file.percentage.toFixed(0) * 1;
            },
            //上传成功回调
            handleVideoSuccess(res) {
                this.isShowUploadVideo = true;
                this.imageFlag = false;
                this.videoUploadPercent = 0;

                //前台上传地址
               // if (file.status == 'success' ) {
               //     this.videoForm.showVideoPath = file.url;
               // } else {
               //      layer.msg("上传失败，请重新上传");
               // }

                //后台上传地址
                if (res.Code == 0) {
                    this.videoForm.showVideoPath = res.data;
                    console.log(this.videoForm.showVideoPath);
                    this.EarFaceURL = "http://localhost:5000/static/face_ear/1_0.jpg";
                } else {
                    layer.msg(res.Message);
                }
            },
            handleimageSuccess(res) {
                this.isShowUploadimage = true;
                this.imageFlag = false;
                this.imageUploadPercent = 0;

                //前台上传地址
                // if (file.status == 'success' ) {
                //     this.videoForm.showVideoPath = file.url;
                // } else {
                //      layer.msg("上传失败，请重新上传");
                // }

                //后台上传地址
                if (res.Code == 0) {
                    this.videoForm.showVideoPath = res.data;
                    console.log(this.imageForm.showimagePath);
                    this.EarFaceURL = "http://localhost:5000/static/face_ear/1_0.jpg";
                } else {
                    layer.msg(res.Message);
                }
            },
            submit(){
                this.buttonLog = '请稍后';
                axios.get("http://localhost:5000/submit?code=1")
                .then((response) => {

                    this.resultForm = response.data
                })
                .catch( (error) => {
                    console.log(error);
                })
            },
            submitForm(){
                this.Formloading = true;
            },
            submit_e(){
                this.buttonLog = '请稍后';
                axios.get("http://localhost:5000/submit?code=1")
                    .then((response) => {

                        this.resultForm = response.data
                    })
                    .catch( (error) => {
                        console.log(error);
                    })
            }

          }


}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
.album{
  text-align:center;
}
.type_title{
  font-size:30px;
}
.v_icon{
  height: 550px;
  width: 350px;
  background:url("../picture/add1.jpg") no-repeat center;
  opacity:0.5;
  background-size:25% 15%;
  background-color:#efefef;
  border:#333333 dotted 3px;
}
.e_icon{
    height: 260px;
    width: 350px;
    background:url("../picture/ear_icon.png") no-repeat center;
    opacity:0.5;
    background-size:13% 15%;
    background-color:#efefef;
    border:#333333 dotted 3px;
}
video{
  margin-left: 30px;
  width:350px;
}
.avatar-uploader{
    display:inline-block;
}
.pic_img_box{
    display:inline-block;
    text-align: center;
    margin-left: 50px;
    margin-right: 50px;
}
.ruleForm{
    height: 200px;
    border: 3px;
    padding: 24px;
}
.pic_block{
    display:inline-block;
    padding:50px;
}

</style>
