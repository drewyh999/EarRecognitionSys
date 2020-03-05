<template>
    <div>
        <div style="text-align: center;margin-top:10%">
        <div class="very_img_box">
<!--            <el-image src="../picture/ear_icon"></el-image>-->
            <el-image
                    style="width: 350px; height: 240px"
                    :src="require('../picture/ear_verified.jpeg')"
                    :fit="fit"></el-image>
            <el-card style="width: 350px; height:250px">
                <div class="step_2" v-if="is_confirmed">
                <h1>验证结果为</h1>
                <h1><span style="color:#87c5ff;text-align: left">{{result_string}}</span><span style="font-size: small">置信度为{{probability}}</span></h1>
                    <el-button style="width:80%" round type="primary" @click="continue_click">继续</el-button>
                </div>
                <div class="step_1" v-else style="margin-top:19%">
                    <h1>请确认是否为此人</h1>
                    <el-row>
                        <el-col :span="12">
                            <el-button style="width:80%" round type="primary" @click="comfirm_click">确认</el-button>
                        </el-col>
                        <el-col :span="12">
                            <el-button style="width:80%" type="danger" round>取消</el-button>
                        </el-col>
                    </el-row>
                </div>
            </el-card>
        </div>
        <div class="very_img_box">
            <video style="width:350px;height:500px"
                   v-bind:src="require('/Users/zhuyuanhao/Downloads/ear_recognition_server/static/video/xian1.mp4')"
                   class="avatar video-avatar"
                   controls="controls">
                您的浏览器不支持视频播放
            </video>
        </div>
        </div>
    </div>
</template>

<script>
    export default {
        name: "Verified",
        data(){
            return{
                is_confirmed:false,
                probability:0.892321,
                fit:'contain',
                result_string:'刘昊然',
                EarFaceURL:'require(../picture/ear_verified.jpeg)',
                videopath:'/Users/zhuyuanhao/Downloads/ear_recognition_server/static/video/xian1.mp4'
            }
        },
        methods:{
            comfirm_click(){
                this.is_confirmed = true;
            },
            continue_click(){
                this.is_confirmed = false;
            }
        }
    }
</script>

<style scoped>
.very_img_box{
    display:inline-block;
    text-align: center;
    margin-left: 50px;
    margin-right: 50px;
}
</style>
