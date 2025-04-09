<template>
    <el-main class="bg edit_wrap ad">
        <el-form ref="form" :model="form" status-icon label-width="80px">        
            <el-row class="row_e"> 
                <el-col :xs="24" :sm="12" :lg="6" class="el_form_item_warp">
                <el-form-item label="标题" prop="title">
                    <el-input v-model="form.title" placeholder="请输入标题"></el-input>
                </el-form-item>
            </el-col>

            <el-col :xs="24" :sm="12" :lg="6" class="el_form_item_warp">
                <el-form-item label="链接" prop="url">
                    <el-input v-model="form.url" placeholder="请输入链接"></el-input>
                </el-form-item>
            </el-col>

            <el-col :xs="24" :sm="12" :lg="6" class="el_form_item_warp">
                <el-form-item label="投放位置" prop="location">
                    <el-select v-model="form.location" placeholder="请选择">
                        <el-option value="顶部广告">顶部广告</el-option>
                        <el-option value="中部广告">中部广告</el-option>
                        <el-option value="底部广告">底部广告</el-option>
                    </el-select>
                </el-form-item>
            </el-col>

            <el-col :xs="24" :sm="24" :lg="24" class="editor el_form_editor_warp">
                <el-form-item label="内容" prop="content">
                    <quill-editor v-model="form.content">
                    </quill-editor>
                </el-form-item>
            </el-col>
            </el-row>
            <el-col :xs="24" :sm="24" :lg="24" class="el_form_btn_warp">
                <el-form-item>
                    <el-col :xs="24" :sm="12" :lg="12" class="el_form_btn el_form_btn_1">
                        <el-button style="width: 100%; float: left;" type="primary" @click="submit()">提交</el-button>
                    </el-col>
                    <el-col :xs="24" :sm="12" :lg="12" class="el_form_btn el_form_btn_2">
                        <el-button style="width: 100%; float: right;" @click="cancel()">取消</el-button>
                    </el-col>
                </el-form-item>
            </el-col>

        </el-form>
        
    </el-main>
</template>

<script>
    import mixin from "@/mixins/page.js";

    export default {
        mixins: [mixin],
        data() {
            return {
                table: "ad",
                field: "ad_id",
                url_add: "~/api/ad/add?",
                url_set: "~/api/ad/set?",
                url_get_obj: "~/api/ad/get_obj?",
                url_upload: "~/api/ad/upload?",
                query: {
                    ad_id: 0
                },
                form: {
                    ad_id: 0,
                    title: "",
                    content: "",
                    url: "",
                    img: "",
                    display: 0,
                    hits: 0,
					          location: ""
                }
            }
        },
        methods: {
            submit_check(params) {
            	var msg = "";
                if (params.title === "") {
					msg = "标题不能为空";
                    return msg;
                }
                if (params.content === "") {
					msg = "文本不能为空";
					return msg;
                }
                if (params.url === "") {
					msg = "连接不能为空";
					return msg;
                }
				if (params.location === "") {
					msg = "投放位置不能为空";
					return msg;
				}
            },
            /**
             * 上传文件
             * @param {Object} param
             */
            uploadimg(param) {
                this.uploadFile(param.file);
            },

            remove_ing() {
                this.form.img = ''
            }
        },
    }
</script>

<style>

    .avatar-uploader .el-upload {
        border: 1px dashed #d9d9d9;
        border-radius: 6px;
        cursor: pointer;
        position: relative;
        overflow: hidden;
    }

    .avatar-uploader .el-upload:hover {
        border-color: #409EFF;
    }

    .avatar-uploader-icon {
        font-size: 28px;
        color: #8c939d;
        width: 178px;
        height: 178px;
        line-height: 178px;
        text-align: center;
    }

    .avatar {
        width: 178px;
        height: 178px;
        display: block;
    }
</style>
