<template>
	<el-main class="bg edit_wrap">
		<el-form ref="form" :model="form" status-icon label-width="120px" v-if="is_view()">
		<el-row class="row_ce">
							<el-col v-if="user_group === '管理员' || $check_field('get','song_title') || $check_field('add','song_title') || $check_field('set','song_title')" :xs="24" :sm="12" :lg="8" class="el_form_item_warp">
				<el-form-item label="歌曲名称" prop="song_title">
												<el-input id="song_title" v-model="form['song_title']" placeholder="请输入歌曲名称"
							  v-if="user_group === '管理员' || (form['popular_songs_id'] && $check_field('set','song_title')) || (!form['popular_songs_id'] && $check_field('add','song_title'))" :disabled="disabledObj['song_title_isDisabled']"></el-input>
					<div v-else-if="$check_field('get','song_title')">{{form['song_title']}}</div>
											</el-form-item>
			</el-col>
								<el-col v-if="user_group === '管理员' || $check_field('get','music_genre') || $check_field('add','music_genre') || $check_field('set','music_genre')" :xs="24" :sm="12" :lg="8" class="el_form_item_warp">
				<el-form-item label="音乐类型" prop="music_genre">
								<el-select id="music_genre" v-model="form['music_genre']"						v-if="user_group === '管理员' || (form['popular_songs_id'] && $check_field('set','music_genre')) || (!form['popular_songs_id'] && $check_field('add','music_genre'))">
						<el-option v-for="o in list_music_genre" :key="o['music_genre']" :label="o['music_genre']"
							:value="o['music_genre']">
						</el-option>
					</el-select>
					<div v-else-if="$check_field('get','music_genre')">{{form['music_genre']}}</div>
							</el-form-item>
			</el-col>
								<el-col v-if="user_group === '管理员' || $check_field('get','singer_name') || $check_field('add','singer_name') || $check_field('set','singer_name')" :xs="24" :sm="12" :lg="8" class="el_form_item_warp">
				<el-form-item label="歌手姓名" prop="singer_name">
												<el-input id="singer_name" v-model="form['singer_name']" placeholder="请输入歌手姓名"
							  v-if="user_group === '管理员' || (form['popular_songs_id'] && $check_field('set','singer_name')) || (!form['popular_songs_id'] && $check_field('add','singer_name'))" :disabled="disabledObj['singer_name_isDisabled']"></el-input>
					<div v-else-if="$check_field('get','singer_name')">{{form['singer_name']}}</div>
											</el-form-item>
			</el-col>
								<el-col v-if="user_group === '管理员' || $check_field('get','release_time') || $check_field('add','release_time') || $check_field('set','release_time')" :xs="24" :sm="12" :lg="8" class="el_form_item_warp">
				<el-form-item label="发行时间" prop="release_time">
								<el-date-picker :disabled="disabledObj['release_time_isDisabled']" v-if="user_group === '管理员' || (form['popular_songs_id'] && $check_field('set','release_time')) || (!form['popular_songs_id'] && $check_field('add','release_time'))" id="release_time"
						v-model="form['release_time']" type="date" placeholder="选择日期">
					</el-date-picker>
					<div v-else-if="$check_field('get','release_time')">{{form['release_time']}}</div>
							</el-form-item>
			</el-col>
								<el-col v-if="user_group === '管理员' || $check_field('get','singer_photos') || $check_field('add','singer_photos') || $check_field('set','singer_photos')" :xs="24" :sm="12" :lg="8" class="el_form_item_warp">
				<el-form-item label="歌手照片" prop="singer_photos">
								<el-upload :disabled="disabledObj['singer_photos_isDisabled']" id="singer_photos" class="avatar-uploader" drag
						accept="image/gif, image/jpeg, image/png, image/jpg" action="" :http-request="upload_singer_photos"
						:show-file-list="false" v-if="user_group === '管理员' || (form['popular_songs_id'] && $check_field('set','singer_photos')) || (!form['popular_songs_id'] && $check_field('add','singer_photos'))">
						<img v-if="form['singer_photos']" :src="$fullUrl(form['singer_photos'])" class="avatar">
						<i v-else class="el-icon-plus avatar-uploader-icon"></i>
					</el-upload>
					<el-image v-else-if="$check_field('get','singer_photos')" style="width: 100px; height: 100px"
						:src="$fullUrl(form['singer_photos'])" :preview-src-list="[$fullUrl(form['singer_photos'])]">
						<div slot="error" class="image-slot">
							<img src="../../../public/img/error.png" style="width: 90px; height: 90px" />
						</div>
					</el-image>
							</el-form-item>
			</el-col>
								<el-col v-if="user_group === '管理员' || $check_field('get','album_name') || $check_field('add','album_name') || $check_field('set','album_name')" :xs="24" :sm="12" :lg="8" class="el_form_item_warp">
				<el-form-item label="专辑名称" prop="album_name">
												<el-input id="album_name" v-model="form['album_name']" placeholder="请输入专辑名称"
							  v-if="user_group === '管理员' || (form['popular_songs_id'] && $check_field('set','album_name')) || (!form['popular_songs_id'] && $check_field('add','album_name'))" :disabled="disabledObj['album_name_isDisabled']"></el-input>
					<div v-else-if="$check_field('get','album_name')">{{form['album_name']}}</div>
											</el-form-item>
			</el-col>
								<el-col v-if="user_group === '管理员' || $check_field('get','playback_quantity') || $check_field('add','playback_quantity') || $check_field('set','playback_quantity')" :xs="24" :sm="12" :lg="8" class="el_form_item_warp">
				<el-form-item label="播放数量" prop="playback_quantity">
								<el-input-number id="playback_quantity" v-model.number="form['playback_quantity']"
						v-if="user_group === '管理员' || (form['popular_songs_id'] && $check_field('set','playback_quantity')) || (!form['popular_songs_id'] && $check_field('add','playback_quantity'))" :disabled="disabledObj['playback_quantity_isDisabled']"></el-input-number>
					<div v-else-if="$check_field('get','playback_quantity')">{{form['playback_quantity']}}</div>
							</el-form-item>
			</el-col>
								<el-col v-if="user_group === '管理员' || $check_field('get','music_audio') || $check_field('add','music_audio') || $check_field('set','music_audio')" :xs="24" :sm="12" :lg="8" class="el_form_item_warp">
				<el-form-item label="音乐音频" prop="music_audio">
												<el-upload v-if="user_group === '管理员' || (form['popular_songs_id'] && $check_field('set','music_audio')) || (!form['popular_songs_id'] && $check_field('add','music_audio'))" class="upload-demo" drag
						action="" style="max-width: 300px;width: 100%;" :http-request="upload_music_audio" :limit="1" accept="audio/ogg,audio/mp3,audio/wav">
						<i class="el-icon-upload"></i>
						<div class="el-upload__text">将音频拖到此处，或<em>点击上传</em></div>
					</el-upload>
					<div v-else-if="$check_field('get','music_audio')">
						<el-button type="primary" @click="download(form['music_audio'])">下载<i
								class="el-icon-download el-icon--right"></i></el-button>
					</div>
											</el-form-item>
			</el-col>
								<el-col v-if="user_group === '管理员' || $check_field('get','music_introduction') || $check_field('add','music_introduction') || $check_field('set','music_introduction')" :xs="24" :sm="12" :lg="8" class="el_form_item_warp">
				<el-form-item label="音乐简介" prop="music_introduction">
								<el-input type="textarea" id="music_introduction" v-model="form['music_introduction']" placeholder="请输入音乐简介"
						v-if="user_group === '管理员' || (form['popular_songs_id'] && $check_field('set','music_introduction')) || (!form['popular_songs_id'] && $check_field('add','music_introduction'))" :disabled="disabledObj['music_introduction_isDisabled']"></el-input>
					<div v-else-if="$check_field('get','music_introduction')">{{form['music_introduction']}}</div>
							</el-form-item>
			</el-col>
								<el-col v-if="user_group === '管理员' || $check_field('get','music_content') || $check_field('add','music_content') || $check_field('set','music_content')" :xs="24" :sm="12" :lg="8" class="el_form_item_warp">
				<el-form-item label="音乐内容" prop="music_content">
								<el-input type="textarea" id="music_content" v-model="form['music_content']" placeholder="请输入音乐内容"
						v-if="user_group === '管理员' || (form['popular_songs_id'] && $check_field('set','music_content')) || (!form['popular_songs_id'] && $check_field('add','music_content'))" :disabled="disabledObj['music_content_isDisabled']"></el-input>
					<div v-else-if="$check_field('get','music_content')">{{form['music_content']}}</div>
							</el-form-item>
			</el-col>
					
	
	
	
	
	
	
	</el-row>
			<el-col :xs="24" :sm="12" :lg="8" class="el_form_btn_warp">
				<el-form-item v-if="$check_action('/popular_songs/view','set') || $check_action('/popular_songs/view','add') || $check_option('/popular_songs/table','examine')">
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
				field: "popular_songs_id",
				url_add: "~/api/popular_songs/add?",
				url_set: "~/api/popular_songs/set?",
				url_get_obj: "~/api/popular_songs/get_obj?",
				url_upload: "~/api/popular_songs/upload?",

				query: {
					"popular_songs_id": 0,
				},

				form: {
								"song_title":  '', // 歌曲名称
										"music_genre":  '', // 音乐类型
										"singer_name":  '', // 歌手姓名
										"release_time":  '', // 发行时间
										"singer_photos":  '', // 歌手照片
										"album_name":  '', // 专辑名称
										"playback_quantity":  0, // 播放数量
										"music_audio":  '', // 音乐音频
										"music_introduction":  '', // 音乐简介
										"music_content":  '', // 音乐内容
											"popular_songs_id": 0, // ID
						
				},
				disabledObj:{
								"song_title_isDisabled": false,
										"music_genre_isDisabled": false,
										"singer_name_isDisabled": false,
										"release_time_isDisabled": false,
										"singer_photos_isDisabled": false,
										"album_name_isDisabled": false,
					          			"playback_quantity_isDisabled": false,
										"music_audio_isDisabled": false,
										"music_introduction_isDisabled": false,
										"music_content_isDisabled": false,
										},

	
								// 音乐类型选项列表
				list_music_genre: [""],
	
		
		
		
		
		
		
		
		
	
			}
		},
		methods: {


	
	
			
				/**
			 * 获取音乐类型列表
			 */
			async get_list_music_genre() {
				var json = await this.$get("~/api/music_classification/get_list?");
				if(json.result && json.result.list){
					this.list_music_genre = json.result.list;
				}
				else if(json.error){
					console.error(json.error);
				}
			},
					
			
	
			
	
						/**
			 * 上传歌手照片
			 * @param {Object} param 图片参数
			 */
			upload_singer_photos(param){
						this.uploadFile(param.file, "singer_photos");
					},
	
	
			
	
			
	
						/**
			 * 上传音乐音频
			 * @param {Object} param 音频参数
			 */
			upload_music_audio(param){
						this.uploadFile(param.file, "music_audio");
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
								        if (this.form["release_time"] && this.form["release_time"].indexOf("-")===-1){
          this.form["release_time"] = this.$toTime(parseInt(this.form["release_time"]),"yyyy-MM-dd")
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

																		if(json.result.obj["release_time"]=="0000-00-00"){
				  json.result.obj["release_time"] = null;
				}
				if(parseInt(json.result.obj["release_time"]) > 9999){
					json.result.obj["release_time"] = this.$toTime(parseInt(json.result.obj["release_time"]),"yyyy-MM-dd")
				}
																											

			},

			/**
			 * 提交前验证事件
			 * @param {Object} 请求参数
			 * @return {String} 验证成功返回null, 失败返回错误提示
			 */
			submit_check(param) {
																																			if (!param.release_time){
					return "发行时间不能为空";
				}
																																																																			return null;
			},

			is_view(){
				var bl = this.user_group == "管理员";

				if(!bl){
					bl = this.$check_action('/popular_songs/table','add');
					console.log(bl ? "你有表格添加权限视作有添加权限" : "你没有表格添加权限");
				}
				if(!bl){
					bl = this.$check_action('/popular_songs/table','set');
					console.log(bl ? "你有表格添加权限视作有修改权限" : "你没有表格修改权限");
				}
				if(!bl){
					bl = this.$check_action('/popular_songs/view','add');
					console.log(bl ? "你有视图添加权限视作有添加权限" : "你没有视图添加权限");
				}
				if(!bl){
					bl = this.$check_action('/popular_songs/view','set');
					console.log(bl ? "你有视图修改权限视作有修改权限" : "你没有视图修改权限");
				}
				if(!bl){
					bl = this.$check_action('/popular_songs/view','get');
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
						this.get_list_music_genre();
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
