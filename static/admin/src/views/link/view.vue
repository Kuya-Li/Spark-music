<template>
	<el-main class="bg edit_wrap link">
		<el-form ref="form" :model="form" status-icon label-width="100px">
			<el-row class="row_e">
				<el-col :xs="24" :sm="12" :lg="12" class="el_form_item_warp">
				<el-form-item label="友情链接图" prop="img">
					<el-upload class="avatar-uploader" drag accept="image/gif, image/jpeg, image/png, image/jpg"
						action="" :http-request="uploadimg" :show-file-list="false">
						<img v-if="form.img" :src="$fullUrl(form.img)" class="avatar">
						<i v-else class="el-icon-plus avatar-uploader-icon"></i>
					</el-upload>
				</el-form-item>
			</el-col>

			<el-col :xs="24" :sm="12" :lg="12" class="el_form_item_warp">
				<el-form-item label="友情链接名" prop="name">
					<el-input v-model="form.name" placeholder="请输入友情链接名"></el-input>
				</el-form-item>
			</el-col>

			<el-col :xs="24" :sm="12" :lg="12" class="el_form_item_warp">
				<el-form-item label="链接地址" prop="url">
					<el-input v-model="form.url" placeholder="请输入链接地址"></el-input>
				</el-form-item>
			</el-col>

			<el-col :xs="24" :sm="12" :lg="12" class="el_form_item_warp">
				<el-form-item label="显示顺序" prop="display">
					<el-input-number v-model="form.display" placeholder="请输入显示顺序"></el-input-number>
				</el-form-item>
			</el-col>
			</el-row>
			

			<el-col :xs="24" :sm="24" :lg="24" class="el_form_btn_warp">
				<el-form-item>
					<el-col :xs="24" :sm="24" :lg="12" class="el_form_btn el_form_btn_1">
						<el-button style="width: 100%; float: left;" type="primary" @click="submit()">提交</el-button>
					</el-col>
					<el-col :xs="24" :sm="24" :lg="12" class="el_form_btn el_form_btn_2">
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
				title: "link",
				field: "link_id",

				// 路径集
				url_add: "~/api/link/add?",
				url_set: "~/api/link/set?",
				url_get_obj: "~/api/link/get_obj?",
				url_upload: "~/api/link/upload?",

				query: {
					link_id: 0
				},

				form: {
					link_id: 0,
					img: "",
					name: "",
					url: ""
				},
			}
		},
		methods: {
			submit_check(params) {
				var msg = "";
				if (params.name === "") {
					msg = "链接名不能为空";
					return msg;
				}
				if (params.url === "") {
					msg = "连接不能为空";
					return msg;
				}
			},
			/**
			 * 上传封面图
			 * @param {Object} param
			 */
			uploadimg(param) {
				this.uploadFile(param.file);
			}

		},
		created() {}
	}
</script>

<style>
	.bg {
		background: white;
	}

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
