<template>
	<el-main class="bg edit_wrap comtable_e">
		<el-form ref="form" :model="form" status-icon label-width="120px" v-if="is_view()">
		<el-row class="row_ce"> 
							<el-col v-if="user_group === '管理员' || $check_field('get','song_title') || $check_field('add','song_title') || $check_field('set','song_title')" :xs="24" :sm="12" :lg="8" class="el_form_item_warp">
				<el-form-item label="歌曲名称" prop="song_title">
												<el-input id="song_title" v-model="form['song_title']" placeholder="请输入歌曲名称"
							  v-if="user_group === '管理员' || (form['music_information_id'] && $check_field('set','song_title')) || (!form['music_information_id'] && $check_field('add','song_title'))" :disabled="disabledObj['song_title_isDisabled']"></el-input>
					<div v-else-if="$check_field('get','song_title')">{{form['song_title']}}</div>
											</el-form-item>
			</el-col>
								<el-col v-if="user_group === '管理员' || $check_field('get','singer_name') || $check_field('add','singer_name') || $check_field('set','singer_name')" :xs="24" :sm="12" :lg="8" class="el_form_item_warp">
				<el-form-item label="歌手名称" prop="singer_name">
												<el-input id="singer_name" v-model="form['singer_name']" placeholder="请输入歌手名称"
							  v-if="user_group === '管理员' || (form['music_information_id'] && $check_field('set','singer_name')) || (!form['music_information_id'] && $check_field('add','singer_name'))" :disabled="disabledObj['singer_name_isDisabled']"></el-input>
					<div v-else-if="$check_field('get','singer_name')">{{form['singer_name']}}</div>
											</el-form-item>
			</el-col>
								<el-col v-if="user_group === '管理员' || $check_field('get','album_name') || $check_field('add','album_name') || $check_field('set','album_name')" :xs="24" :sm="12" :lg="8" class="el_form_item_warp">
				<el-form-item label="专辑名称" prop="album_name">
												<el-input id="album_name" v-model="form['album_name']" placeholder="请输入专辑名称"
							  v-if="user_group === '管理员' || (form['music_information_id'] && $check_field('set','album_name')) || (!form['music_information_id'] && $check_field('add','album_name'))" :disabled="disabledObj['album_name_isDisabled']"></el-input>
					<div v-else-if="$check_field('get','album_name')">{{form['album_name']}}</div>
											</el-form-item>
			</el-col>
								<el-col v-if="user_group === '管理员' || $check_field('get','release_time') || $check_field('add','release_time') || $check_field('set','release_time')" :xs="24" :sm="12" :lg="8" class="el_form_item_warp">
				<el-form-item label="发布时间" prop="release_time">
												<el-input id="release_time" v-model="form['release_time']" placeholder="请输入发布时间"
							  v-if="user_group === '管理员' || (form['music_information_id'] && $check_field('set','release_time')) || (!form['music_information_id'] && $check_field('add','release_time'))" :disabled="disabledObj['release_time_isDisabled']"></el-input>
					<div v-else-if="$check_field('get','release_time')">{{form['release_time']}}</div>
											</el-form-item>
			</el-col>
								<el-col v-if="user_group === '管理员' || $check_field('get','song_image') || $check_field('add','song_image') || $check_field('set','song_image')" :xs="24" :sm="12" :lg="8" class="el_form_item_warp">
				<el-form-item label="歌曲图片" prop="song_image">
								<el-upload :disabled="disabledObj['song_image_isDisabled']" id="song_image" class="avatar-uploader" drag
						accept="image/gif, image/jpeg, image/png, image/jpg" action="" :http-request="upload_song_image"
						:show-file-list="false" v-if="user_group === '管理员' || (form['music_information_id'] && $check_field('set','song_image')) || (!form['music_information_id'] && $check_field('add','song_image'))">
						<img v-if="form['song_image']" :src="$fullUrl(form['song_image'])" class="avatar">
						<i v-else class="el-icon-plus avatar-uploader-icon"></i>
					</el-upload>
					<el-image v-else-if="$check_field('get','song_image')" style="width: 100px; height: 100px"
						:src="$fullUrl(form['song_image'])" :preview-src-list="[$fullUrl(form['song_image'])]">
						<div slot="error" class="image-slot">
							<img src="../../../public/img/error.png" style="width: 90px; height: 90px" />
						</div>
					</el-image>
							</el-form-item>
			</el-col>
								<el-col v-if="user_group === '管理员' || $check_field('get','lyrics_content') || $check_field('add','lyrics_content') || $check_field('set','lyrics_content')" :xs="24" :sm="12" :lg="8" class="el_form_item_warp">
				<el-form-item label="歌词内容" prop="lyrics_content">
												<el-input id="lyrics_content" v-model="form['lyrics_content']" placeholder="请输入歌词内容"
							  v-if="user_group === '管理员' || (form['music_information_id'] && $check_field('set','lyrics_content')) || (!form['music_information_id'] && $check_field('add','lyrics_content'))" :disabled="disabledObj['lyrics_content_isDisabled']"></el-input>
					<div v-else-if="$check_field('get','lyrics_content')">{{form['lyrics_content']}}</div>
											</el-form-item>
			</el-col>
					
	
	
	
	
	
	
		</el-row>
			<el-col :xs="24" :sm="12" :lg="8" class="el_form_btn_warp">
				<el-form-item v-if="$check_action('/music_information/view','set') || $check_action('/music_information/view','add') || $check_option('/music_information/table','examine')">
					<el-button type="primary" @click="submit()">提交</el-button>
					<el-button @click="cancel()">取消</el-button>
				</el-form-item>
				<el-form-item v-else>
					<el-button @click="cancel()">返回</el-button>
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
				field: "music_information_id",
				url_add: "~/api/music_information/add?",
				url_set: "~/api/music_information/set?",
				url_get_obj: "~/api/music_information/get_obj?",
				url_upload: "~/api/music_information/upload?",

				query: {
					"music_information_id": 0,
				},

				form: {
								"song_title":  '', // 歌曲名称
										"singer_name":  '', // 歌手名称
										"album_name":  '', // 专辑名称
										"release_time":  '', // 发布时间
										"song_image":  '', // 歌曲图片
										"lyrics_content":  '', // 歌词内容
											"music_information_id": 0, // ID
						
				},
				disabledObj:{
								"song_title_isDisabled": false,
										"singer_name_isDisabled": false,
										"album_name_isDisabled": false,
										"release_time_isDisabled": false,
										"song_image_isDisabled": false,
										"lyrics_content_isDisabled": false,
										},

	
		
		
		
		
		
	
			}
		},
		methods: {


	
	
			
	
			
	
			
	
						/**
			 * 上传歌曲图片
			 * @param {Object} param 图片参数
			 */
			upload_song_image(param){
						this.uploadFile(param.file, "song_image");
					},
	
	
			
	
		
			/**
			 * 获取对象之前
			 * @param {Object} param
			 */
			get_obj_before(param) {
				var form = "";
										
				if(this.form && form){
					Object.keys(this.form).forEach(key => {
						Object.keys(form).forEach(dbKey => {
							// if(dbKey === "charging_standard"){
							// 	this.form['charging_rules'] = form[dbKey];
							// 	this.disabledObj['charging_rules_isDisabled'] = true;
							// };
							if(key === dbKey){
								this.disabledObj[key+'_isDisabled'] = true;
							}
						})
					})
				}
																$.db.del("form");

				return param;
			},

			/**
			 * 获取对象之后
			 * @param {Object} json
			 * @param {Object} func
			 */
			get_obj_after(json, func){
																								

			},

			/**
			 * 提交前验证事件
			 * @param {Object} 请求参数
			 * @return {String} 验证成功返回null, 失败返回错误提示
			 */
			submit_check(param) {
																																																												return null;
			},

			is_view(){
				var bl = this.user_group == "管理员";

				if(!bl){
					bl = this.$check_action('/music_information/table','add');
					console.log(bl ? "你有表格添加权限视作有添加权限" : "你没有表格添加权限");
				}
				if(!bl){
					bl = this.$check_action('/music_information/table','set');
					console.log(bl ? "你有表格添加权限视作有修改权限" : "你没有表格修改权限");
				}
				if(!bl){
					bl = this.$check_action('/music_information/view','add');
					console.log(bl ? "你有视图添加权限视作有添加权限" : "你没有视图添加权限");
				}
				if(!bl){
					bl = this.$check_action('/music_information/view','set');
					console.log(bl ? "你有视图修改权限视作有修改权限" : "你没有视图修改权限");
				}
				if(!bl){
					bl = this.$check_action('/music_information/view','get');
					console.log(bl ? "你有视图查询权限视作有查询权限" : "你没有视图查询权限");
				}

				console.log(bl ? "具有当前页面的查看权，请注意这不代表你有字段的查看权" : "无权查看当前页，请注意即便有字段查询权限没有页面查询权限也不行");

				return bl;
			},
			/**
			 * 上传文件
			 * @param {Object} param
			 */
			uploadimg(param) {
				this.uploadFile(param.file, "avatar");
			},

		},
		created() {
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
